#!/usr/bin/env python3
"""
sne_wien_realSED.py — Real-SED update of the pre-registered chromatic
fingerprints (PREREGISTRATION_chromatic_fingerprints_2026-08-03.md, e2e78a0).

Replaces the toy blackbody with the Hsiao SN Ia spectral template and the
top-hat bands with real DES griz throughput curves (both via sncosmo).
Everything else follows the registered construction:

  tau(lambda_obs, z) = eta * (1 - 1/sqrt(1+z)) * (lambda_obs/700nm)^(-1/2),
  eta = pi^2/beta^2 (geometric), b = 1 envelope (Branch B [OPEN]).

Outputs the two registered fingerprints at template precision:
  1. rise/decay differential extinction per band/z (mmag)
  2. effective per-band width perturbation Delta-b (differential form)
plus |Delta t_peak| and the band-ordering ratios, for direct comparison
against the registered toy tables. This run UPDATES registered magnitudes;
the form was registered first.
"""

import json
import numpy as np
from pathlib import Path
import sncosmo

PI = np.pi
ALPHA = 1.0 / 137.035999177

def solve_golden_loop(alpha):
    target = (1.0 / alpha) - 1.0
    C = 2.0 * PI ** 2
    b = 3.0
    for _ in range(100):
        eb = np.exp(b)
        step = (C * eb / b - target) / (C * eb * (b - 1.0) / b ** 2)
        b -= step
        if abs(step) < 1e-15:
            break
    return b

BETA = solve_golden_loop(ALPHA)
ETA = PI ** 2 / BETA ** 2
LAM_REF = 7000.0                                   # Angstrom (700 nm)

SOURCE = sncosmo.get_source("hsiao")               # SN Ia spectral template
BANDS = {b: sncosmo.get_bandpass(f"des{b}") for b in "griz"}

def tau_lam(lam_obs, z):
    return ETA * (1.0 - 1.0 / np.sqrt(1.0 + z)) * np.sqrt(LAM_REF / lam_obs)

def band_curve(z, band, chromatic=True):
    """Observed-band photon-count light curve vs OBSERVED time (b = 1 envelope).
    Rest-frame template flux F_lam(phase, lam_rest); observed lam = lam_rest(1+z).
    Achromatic drag scales all photon energies equally (shape-irrelevant here);
    the chromatic channel applies exp(-tau(lam_obs)) across the band."""
    bp = BANDS[band]
    lam_obs = np.linspace(bp.minwave(), bp.maxwave(), 300)
    trans = bp(lam_obs)
    lam_rest = lam_obs / (1.0 + z)
    phase = np.linspace(-15.0, 80.0, 2000)          # template phase (rest frame)
    F = SOURCE.flux(phase, lam_rest)                # erg/s/cm^2/A, shape (nph, nlam)
    F = np.clip(F, 0.0, None)
    if chromatic:
        att = np.exp(-tau_lam(lam_obs, z))[None, :]
    else:
        att = np.exp(-tau_lam(np.mean(lam_obs), z))
    # photon-count integrand: F_lam * lam * throughput
    counts = np.trapezoid(F * att * (trans * lam_obs)[None, :], lam_obs, axis=1)
    t_obs = phase * (1.0 + z)
    return t_obs, counts

def timing_metrics(t, F):
    F = F / F.max()
    ipk = int(np.argmax(F))
    t_pk = t[ipk]
    def rise_cross(tt, ff):
        idx = np.where(np.diff(ff >= 0.5))[0]
        if not len(idx):
            return np.nan
        i = idx[0]
        return tt[i] + (0.5 - ff[i]) * (tt[i + 1] - tt[i]) / (ff[i + 1] - ff[i])
    t_r = rise_cross(t[:ipk + 1], F[:ipk + 1])
    seg_t, seg_F = t[ipk:], F[ipk:]
    idx = np.where(np.diff(seg_F < 0.5))[0]
    t_f = (seg_t[i] + (seg_F[i] - 0.5) * (seg_t[i + 1] - seg_t[i]) / (seg_F[i] - seg_F[i + 1])
           if len(idx) and (i := idx[0]) is not None else np.nan)
    return t_pk, t_r, t_f

def eff_tau_series(z, band):
    """Band-averaged effective optical depth vs phase (for the flux fingerprint)."""
    bp = BANDS[band]
    lam_obs = np.linspace(bp.minwave(), bp.maxwave(), 300)
    trans = bp(lam_obs)
    lam_rest = lam_obs / (1.0 + z)
    phase = np.linspace(-15.0, 80.0, 400)
    F = np.clip(SOURCE.flux(phase, lam_rest), 0.0, None)
    w = F * (trans * lam_obs)[None, :]
    t_l = tau_lam(lam_obs, z)[None, :]
    att = np.trapezoid(w * np.exp(-t_l), lam_obs, axis=1) / \
          np.clip(np.trapezoid(w, lam_obs, axis=1), 1e-300, None)
    return phase, -np.log(np.clip(att, 1e-300, None))

MAG_PER_TAU = 2.5 / np.log(10.0)
Z_GRID = [0.1, 0.3, 0.5, 0.8, 1.0]
RES = {"fingerprint1_mmag": {}, "fingerprint2_db": {}, "dt_peak_days": {}}

print(f"β = {BETA:.6f}  η = {ETA:.6f}   template: Hsiao, bands: DES griz\n")
print("Fingerprint 1 — rise-minus-decay differential extinction (mmag):")
print(f"{'band':>4} " + " ".join(f"z={z:<4}" for z in Z_GRID))
for band in "griz":
    row = []
    for z in Z_GRID:
        phase, tau_eff = eff_tau_series(z, band)
        # weight phases by the band light curve itself
        t_obs, F = band_curve(z, band, chromatic=True)
        Fw = np.interp(phase, t_obs / (1.0 + z), F)
        rise = phase < 0.0
        decay = phase > 0.0
        d = MAG_PER_TAU * (np.average(tau_eff[rise], weights=Fw[rise])
                           - np.average(tau_eff[decay], weights=Fw[decay])) * 1e3
        row.append(d)
    RES["fingerprint1_mmag"][band] = dict(zip(map(str, Z_GRID), map(float, row)))
    print(f"{band:>4} " + " ".join(f"{v:6.2f}" for v in row))

g05 = RES["fingerprint1_mmag"]["g"]["0.5"]
print("\nBand ordering at z = 0.5 (registered toy: 1.00 : 0.38 : 0.14 : 0.08):")
print("  " + " : ".join(f"{RES['fingerprint1_mmag'][b]['0.5']/g05:.2f}" for b in "griz"))

print("\nFingerprint 2 — width perturbation Δb_eff and |Δt_peak|:")
print(f"{'band':>4} {'z':>4} {'Δt_peak[d]':>11} {'Δwidth/width':>13} {'Δb_eff':>10}")
for band in "griz":
    for z in Z_GRID:
        t_obs, Fc = band_curve(z, band, chromatic=True)
        _,     F0 = band_curve(z, band, chromatic=False)
        pk_c, r_c, f_c = timing_metrics(t_obs, Fc)
        pk_0, r_0, f_0 = timing_metrics(t_obs, F0)
        dw = ((f_c - r_c) - (f_0 - r_0)) / (f_0 - r_0)
        db = dw / np.log(1.0 + z)
        RES["fingerprint2_db"].setdefault(band, {})[str(z)] = float(db)
        RES["dt_peak_days"].setdefault(band, {})[str(z)] = float(pk_c - pk_0)
        if z == 0.5:
            print(f"{band:>4} {z:>4} {pk_c-pk_0:>11.4f} {dw:>13.2e} {db:>10.2e}")

db_g, db_z = RES["fingerprint2_db"]["g"]["0.5"], RES["fingerprint2_db"]["z"]["0.5"]
print(f"\nRegistered differential test, template precision: "
      f"b(g) − b(z-band) ≈ {db_g - db_z:+.2e}  (toy: +8×10⁻⁴)")
print(f"Achromaticity budget: max per-band Δb = {max(abs(v) for d in RES['fingerprint2_db'].values() for v in d.values()):.2e} "
      f"vs White σ_b = 0.0112 — consistency gate re-checked at template precision.")

out = Path(__file__).resolve().parent / "sne_wien_realSED_results.json"
out.write_text(json.dumps(RES, indent=2))
print(f"\nresults written to {out.name}")
