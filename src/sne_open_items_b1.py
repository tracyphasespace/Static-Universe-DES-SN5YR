#!/usr/bin/env python3
"""
sne_open_items_b1.py — Post-reconciliation register (b = 1) update of
sne_open_items.py.

SUPERSEDES the q = 2/3 register of sne_open_items.py (2026-07-15), which
predates the 2026-07-27/28 exponent reconciliation (book §10.6.3 / §10.8.4b;
SNe_FINDINGS_2026-07-27.md). What changed and why:

  - Arrival-envelope dilation is b = 1 via cycle conservation under Branch B
    [OPEN author ruling — conditional register carried throughout]. The
    (1+z)^(1/3) wavepacket factor is linewidth/coherence physics and appears
    in NO photometric quantity here (its old arrival-rate role gave b = 4/3,
    excluded at 29.5σ).
  - Luminosity-distance exponent: q = (1+b)/2 = 1 (flux-budget identity).
  - Chromatic erosion is NOT the dilation. It survives only as a predicted
    rise/decay ASYMMETRY on top of the properly dilated envelope; its
    amplitude is the number §10.6.3 says must exist before any survey
    significance claim. ITEM 1 computes it (toy SED + top-hat bands; the
    dust/CSM systematics floor is NOT included and is still owed).
  - Tolman: the repo carries TWO accounts — SB ∝ (1+z)^-2 (book v11f,
    no angular-size shrinkage) vs SB ∝ (1+z)^-4 (tolman_test.py, Etherington
    via photon conservation). That is an OPEN carrier ruling (TODOS §2.69);
    ITEM 4 computes BOTH branches and adjudicates NEITHER.

Data: in-repo copy data/DES-SN5YR_HD.csv (the hardcoded SupernovaSrc path of
the predecessor is dead). MUERR_FINAL is a DIAGONAL error column; the
canonical χ² = 1641.94 on 1766 dof is reported against the full STAT+SYS
covariance, so ITEM 3's refit doubles as a provenance probe: if the diagonal
refit reproduces 1641.94 the canonical fit was diagonal after all.

Run: python3 sne_open_items_b1.py        (writes sne_open_items_b1_results.json)
"""

import json
import numpy as np
from pathlib import Path
from scipy.optimize import minimize
from scipy.integrate import quad

PI = np.pi
C_KM_S = 299792.458
MAG_PER_TAU = 2.5 / np.log(10.0)          # 1.0857 mag per unit optical depth
RESULTS = {}

# ── Golden Loop: beta from alpha (unchanged) ────────────────────────────────
ALPHA = 1.0 / 137.035999177

def solve_golden_loop(alpha):
    target = (1.0 / alpha) - 1.0
    C = 2.0 * PI ** 2
    b = 3.0
    for _ in range(100):
        eb = np.exp(b)
        val = C * (eb / b) - target
        deriv = C * eb * (b - 1.0) / b ** 2
        step = val / deriv
        b -= step
        if abs(step) < 1e-15:
            break
    return b

BETA = solve_golden_loop(ALPHA)
ETA_GEO = PI ** 2 / BETA ** 2             # geometric value; the FIT uses eta free
print(f"β = {BETA:.10f}   η_geo = π²/β² = {ETA_GEO:.10f}")

# ── Data (in-repo copy; z ≥ 0.01 cut as in §10.8.4b) ───────────────────────
DATA = Path(__file__).resolve().parent / "data" / "DES-SN5YR_HD.csv"
raw = np.genfromtxt(DATA, delimiter=",", names=True)
m = (raw["zHD"] > 0.01) & (raw["MUERR_FINAL"] > 0) & np.isfinite(raw["MU"])
z_d, mu_d, sig_d = raw["zHD"][m], raw["MU"][m], raw["MUERR_FINAL"][m]
N = len(z_d)
print(f"N = {N} SNe after z > 0.01 cut (file total {len(raw)})\n")

# ════════════════════════════════════════════════════════════════════════════
# ITEM 1 — The rise/decay skew amplitude (the §10.6.3 owed number)
# ════════════════════════════════════════════════════════════════════════════
# Register: within a single band the optical depth is phase-independent at
# leading order; the effect enters only through the SED's flux-weighted mean
# frequency sweeping the filter's internal ν^(1/2) opacity gradient as the
# photosphere cools (Wien evolution 15,000 K → 5,000 K). We compute the
# band-averaged effective depth vs light-curve phase and report the rise-vs-
# decay differential in mmag. TOY MODEL: blackbody SED, top-hat DES bands,
# no dust/CSM floor — an amplitude ESTIMATE, not a survey forecast.
print("=" * 72)
print("ITEM 1: RISE/DECAY SKEW AMPLITUDE AT b = 1  (toy-SED estimate)")
print("=" * 72)

H_over_K = 4.799243e-11                    # h/k_B in s·K^-1... (only ratios used)

def planck_shape(nu, T):
    """B_nu shape (arbitrary normalisation), overflow-safe."""
    x = np.clip(H_over_K * nu / T, 1e-12, 500.0)
    return nu ** 3 / np.expm1(x)

def sn_temperature(t, T_peak=15000.0, T_late=5000.0, t_cool=20.0, t_rise=5.0):
    """Photosphere temperature vs phase t (days, peak at t=0).
    Rise phase held at T_peak (shock-heated), exponential Wien cooling after."""
    t = np.asarray(t, dtype=float)
    return np.where(t <= 0.0, T_peak, T_late + (T_peak - T_late) * np.exp(-t / t_cool))

def sn_lightcurve(t, t_rise=5.0, t_fall=30.0):
    t = np.asarray(t, dtype=float)
    return np.where(t <= 0.0, np.exp(t / t_rise), np.exp(-t / t_fall))

# DES top-hat bands (observed frame), nm
BANDS = {"g": (400.0, 550.0), "r": (560.0, 720.0),
         "i": (710.0, 850.0), "z": (850.0, 1000.0)}
NU_REF = C_KM_S * 1e12 / 700.0             # reference frequency at 700 nm (arbitrary anchor)

def tau_of_z(z, eta):
    return eta * (1.0 - 1.0 / np.sqrt(1.0 + z))

def band_eff_tau(T_emit, z, band, eta, ngrid=400):
    """Effective optical depth of a top-hat observed band for a blackbody SED
    emitted at T_emit and redshifted by (1+z) (achromatic drag: T_obs = T/(1+z)),
    with chromatic depth tau(nu_o) = tau_of_z * (nu_o/NU_REF)^(1/2)."""
    lo, hi = BANDS[band]
    nu = np.linspace(C_KM_S * 1e12 / hi, C_KM_S * 1e12 / lo, ngrid)  # observed
    S = planck_shape(nu, T_emit / (1.0 + z))                          # observed-frame shape
    t_nu = tau_of_z(z, eta) * np.sqrt(nu / NU_REF)
    att = np.trapezoid(S * np.exp(-t_nu), nu) / np.trapezoid(S, nu)
    return -np.log(att)

skew = {}
Z_GRID = [0.1, 0.3, 0.5, 0.8, 1.0]
print(f"{'band':>4} " + " ".join(f"z={z:<4}" for z in Z_GRID) + "   (rise-minus-decay extra dimming, mmag)")
for band in BANDS:
    row = []
    for z in Z_GRID:
        # flux-weighted mean depth over rise (t<0) and decay (t>0), envelope
        # dilated by (1+z)^b with b = 1 — dilation cancels in the phase means
        # (both phases stretch equally); it is retained for the record.
        b_exp = 1.0
        t_rise_grid = np.linspace(-10.0, 0.0, 60) * (1.0 + z) ** b_exp
        t_decay_grid = np.linspace(0.5, 60.0, 120) * (1.0 + z) ** b_exp
        t_emit_r = t_rise_grid / (1.0 + z) ** b_exp     # emitted-frame phase
        t_emit_d = t_decay_grid / (1.0 + z) ** b_exp
        w_r = sn_lightcurve(t_emit_r)
        w_d = sn_lightcurve(t_emit_d)
        tau_r = np.array([band_eff_tau(T, z, band, ETA_GEO)
                          for T in sn_temperature(t_emit_r)])
        tau_d = np.array([band_eff_tau(T, z, band, ETA_GEO)
                          for T in sn_temperature(t_emit_d)])
        d_mmag = MAG_PER_TAU * (np.average(tau_r, weights=w_r)
                                - np.average(tau_d, weights=w_d)) * 1e3
        row.append(d_mmag)
    skew[band] = dict(zip([str(z) for z in Z_GRID], row))
    print(f"{band:>4} " + " ".join(f"{v:6.2f}" for v in row))

# lambda^(-1/2) scaling check across bands at z = 0.5
lam_eff = {b: 0.5 * (BANDS[b][0] + BANDS[b][1]) for b in BANDS}
a_g = skew["g"]["0.5"]
print("\nλ^(-1/2) register check at z = 0.5 (amplitude ratio vs (λ_g/λ_band)^(1/2)):")
for b in BANDS:
    pred = np.sqrt(lam_eff["g"] / lam_eff[b])
    got = skew[b]["0.5"] / a_g if a_g else float("nan")
    print(f"  {b}: computed {got:5.3f}   λ-scaling {pred:5.3f}")
RESULTS["item1_skew_mmag"] = skew
RESULTS["item1_register"] = ("toy blackbody SED + top-hat bands; no dust/CSM floor; "
                             "rise-minus-decay band-averaged extinction differential; "
                             "eta at geometric value pi^2/beta^2")

# ════════════════════════════════════════════════════════════════════════════
# ITEM 2 — Wien displacement with no frequency remapping (§10b, in code)
# ════════════════════════════════════════════════════════════════════════════
# Achromatic drag multiplies every photon energy by 1/(1+z) while conserving
# photon number/occupation. Claim: a Planck spectrum maps EXACTLY onto a
# Planck spectrum at T/(1+z) — an apparent Wien displacement with no
# frequency remapping. Verified numerically: scale a T_emit blackbody,
# refit a blackbody, report the fractional shape residual.
print("\n" + "=" * 72)
print("ITEM 2: ACHROMATIC DRAG MAPS PLANCK -> PLANCK (Wien, no remapping)")
print("=" * 72)
T_emit, z_test = 6000.0, 1.0
nu = np.logspace(11.5, 15.5, 2000)
# occupation-conserving map: n_obs(nu) = n_emit((1+z) nu)
occ_emit = 1.0 / np.expm1(np.clip(H_over_K * (1 + z_test) * nu / T_emit, 1e-12, 500))
occ_planck = 1.0 / np.expm1(np.clip(H_over_K * nu / (T_emit / (1 + z_test)), 1e-12, 500))
resid = np.max(np.abs(occ_emit - occ_planck) / occ_planck)
print(f"T_emit = {T_emit} K at z = {z_test}: max fractional occupation residual "
      f"vs Planck(T/(1+z)) = {resid:.2e}  (machine-precision => exact)")
print("Register: this shows the FORWARD channel preserves Planck SHAPE (why an")
print("already-thermal spectrum stays FIRAS-clean under drag). Whether the")
print("side-scattered bath BECOMES Planckian is the separate OPEN derivation")
print("(derive_cmb_equilibrium.py lists thermalization as its assumption #3).")
RESULTS["item2_planck_map_residual"] = float(resid)

# ════════════════════════════════════════════════════════════════════════════
# ITEM 3 — b -> q identity and the DES refit at q = 1 (diagonal errors)
# ════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 72)
print("ITEM 3: q = (1+b)/2 IDENTITY + DES-SN5YR REFIT (q = 1, n = 1/2, η free)")
print("=" * 72)
b_meas, sb = 1.003, np.sqrt(0.005 ** 2 + 0.010 ** 2)
q_obs, sq = (1 + b_meas) / 2, np.sqrt(0.005 ** 2 + 0.010 ** 2) / 2
print(f"White et al. 2024: b = {b_meas} ± {sb:.4f}  =>  q_obs = {q_obs} ± {sq:.4f}"
      f"  ({abs(q_obs-1)/sq:.2f}σ from the Branch-B prediction q = 1)")

def mu_qfd(z, eta, M, KJ=70.0):
    D = (C_KM_S / KJ) * np.log(1.0 + z)            # Mpc
    mu_geom = 5.0 * np.log10(D * (1.0 + z)) + 25.0  # q = 1
    return mu_geom + M + MAG_PER_TAU * tau_of_z(z, eta)

def chi2_qfd(p):
    eta, M = p
    r = mu_d - mu_qfd(z_d, eta, M)
    return np.sum((r / sig_d) ** 2)

def mu_lcdm(z, Om, M, H0=70.0):
    zz = np.atleast_1d(z)
    dl = np.empty_like(zz)
    for i, zi in enumerate(zz):
        I, _ = quad(lambda x: 1.0 / np.sqrt(Om * (1 + x) ** 3 + 1 - Om), 0.0, zi)
        dl[i] = (C_KM_S / H0) * (1 + zi) * I
    return 5.0 * np.log10(dl) + 25.0 + M

def chi2_lcdm(p):
    Om, M = p
    return np.sum(((mu_d - mu_lcdm(z_d, Om, M)) / sig_d) ** 2)

fit_q = minimize(chi2_qfd, [1.0, 0.0], method="Nelder-Mead",
                 options={"xatol": 1e-8, "fatol": 1e-8})
fit_l = minimize(chi2_lcdm, [0.3, 0.0], method="Nelder-Mead",
                 options={"xatol": 1e-6, "fatol": 1e-6})
dof = N - 2
print(f"QFD  (q=1, n=1/2, η fitted): η = {fit_q.x[0]:.4f}   "
      f"χ² = {fit_q.fun:.4f} on {dof} dof  (χ²/dof = {fit_q.fun/dof:.4f})")
print(f"ΛCDM (Ωm fitted):            Ωm = {fit_l.x[0]:.4f}  "
      f"χ² = {fit_l.fun:.4f} on {dof} dof  (χ²/dof = {fit_l.fun/dof:.4f})")
print(f"Δχ² (QFD − ΛCDM) = {fit_q.fun - fit_l.fun:+.2f}   — equal parameter count; "
      f"no model-selection claim either way (§10.8.4b register).")
print("PROVENANCE PROBE: canonical table quotes χ² = 1641.9350/1766 with 'full")
print("STAT+SYS covariance'; this refit is DIAGONAL (MUERR_FINAL). Agreement to")
print("~1 in χ² would indicate the canonical fit was effectively diagonal;")
print("disagreement bounds what the off-diagonal terms contributed.")
RESULTS["item3"] = {"eta_fit": float(fit_q.x[0]), "chi2_qfd": float(fit_q.fun),
                    "Om_fit": float(fit_l.x[0]), "chi2_lcdm": float(fit_l.fun),
                    "dof": int(dof), "N": int(N), "q_obs": q_obs, "sigma_q": sq,
                    "note": "diagonal MUERR_FINAL; canonical number used STAT+SYS"}

# ════════════════════════════════════════════════════════════════════════════
# ITEM 4 — Tolman on BOTH carrier branches (OPEN — no adjudication here)
# ════════════════════════════════════════════════════════════════════════════
print("\n" + "=" * 72)
print("ITEM 4: TOLMAN SB — BOTH CARRIER BRANCHES  [OPEN author ruling, TODOS §2.69]")
print("=" * 72)
eta_use = fit_q.x[0]

def n_eff(branch_exp, z1=0.03, z2=0.5):
    """Effective SB power-law exponent over [z1, z2] including the extinction
    survival factor S(z) = exp(-tau(z))."""
    def sb(z):
        return (1.0 + z) ** (-branch_exp) * np.exp(-tau_of_z(z, eta_use))
    return -np.log(sb(z2) / sb(z1)) / np.log((1 + z2) / (1 + z1))

nA = n_eff(2.0)
nB = n_eff(4.0)
print(f"Branch BOOK   (no angular shrinkage, d_A = D):        SB ∝ (1+z)^-2 × S(z)  "
      f"=> n_eff = {nA:.2f} over 0.03<z<0.5")
print(f"Branch SCRIPT (Etherington holds, d_A = r/(1+z)):     SB ∝ (1+z)^-4 × S(z)  "
      f"=> n_eff = {nB:.2f} over 0.03<z<0.5")
print(f"Lerner et al. 2014 measurement: n = 2.6 ± 0.5")
print(f"  Branch BOOK   sits {(2.6-nA)/0.5:+.1f}σ from the central value")
print(f"  Branch SCRIPT sits {(2.6-nB)/0.5:+.1f}σ from the central value")
print("This script adjudicates NEITHER: the exponent is the open carrier ruling")
print("(book v11f (1+z)^-2 vs tolman_test.py (1+z)^-4); it interacts with the")
print("Branch B / cycle-conservation decision and must be ruled once, in canon.")
RESULTS["item4"] = {"n_eff_book_branch": float(nA), "n_eff_script_branch": float(nB),
                    "lerner": "2.6 ± 0.5", "status": "OPEN carrier ruling"}

out = Path(__file__).resolve().parent / "sne_open_items_b1_results.json"
out.write_text(json.dumps(RESULTS, indent=2))
print(f"\nresults written to {out.name}")
