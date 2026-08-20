#!/usr/bin/env python3
"""
sne_wien_lightcurve_shift.py — What the confluence does to light-curve TIMING.

Companion to sne_open_items_b1.py (which computed the rise/decay magnitude
differential). Here the chromatic side channel is applied to a template
light curve and the induced TIMING observables are measured per band and z:

  - Δt_peak : shift of the curve center ("curve center shift")
  - Δs/s    : fractional change of the apparent width (half-max duration)
              relative to the clean b = 1 envelope — must sit inside White
              et al.'s band-flexible achromaticity budget (σ_b ≈ 0.011) or
              the chromatic channel would already be excluded
  - rise/fall asymmetry change

Register (arrival_envelope_term, canon 2026-08-03): the achromatic forward
channel supplies the (1+z) arrival-envelope broadening and the Wien-displaced
SED; the chromatic side channel removes blue amplitude progressively with
distance; the observed curve is the confluence on the survivor beam. This
script quantifies the chromatic channel's timing imprint on that confluence.
Toy model: blackbody photosphere (15,000 -> 5,000 K), top-hat DES bands,
no dust/CSM floor.
"""

import json
import numpy as np
from pathlib import Path

PI = np.pi
C_KM_S = 299792.458
H_over_K = 4.799243e-11
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
ETA = PI ** 2 / BETA ** 2                 # geometric opacity normalisation
BANDS = {"g": (400.0, 550.0), "r": (560.0, 720.0),
         "i": (710.0, 850.0), "z": (850.0, 1000.0)}
NU_REF = C_KM_S * 1e12 / 700.0

def planck_shape(nu, T):
    x = np.clip(H_over_K * nu / T, 1e-12, 500.0)
    return nu ** 3 / np.expm1(x)

def sn_temperature(t, T_peak=15000.0, T_late=5000.0, t_cool=20.0):
    t = np.asarray(t, dtype=float)
    return np.where(t <= 0.0, T_peak, T_late + (T_peak - T_late) * np.exp(-t / t_cool))

def sn_lbol(t, t_rise=5.0, t_fall=30.0):
    t = np.asarray(t, dtype=float)
    return np.where(t <= 0.0, np.exp(t / t_rise), np.exp(-t / t_fall))

def tau_z(z):
    return ETA * (1.0 - 1.0 / np.sqrt(1.0 + z))

def band_flux(t_emit, z, band, chromatic=True, ngrid=300):
    """Observed-band photon-flux light curve (arbitrary norm) at emitted phase
    t_emit. chromatic=True applies tau(nu) = tau_z * (nu/NU_REF)^(1/2) inside
    the band; chromatic=False applies the same tau at the band's mean nu only
    (pure achromatic reference — identical envelope, no internal gradient)."""
    lo, hi = BANDS[band]
    nu = np.linspace(C_KM_S * 1e12 / hi, C_KM_S * 1e12 / lo, ngrid)
    T = sn_temperature(t_emit)
    S = planck_shape(nu[None, :], (T / (1.0 + z))[:, None])   # observed frame
    if chromatic:
        att = np.exp(-tau_z(z) * np.sqrt(nu / NU_REF))[None, :]
    else:
        att = np.exp(-tau_z(z) * np.sqrt(np.mean(nu) / NU_REF))
    F = np.trapezoid(S * att, nu, axis=1)
    return sn_lbol(t_emit) * F / np.max(F)

def timing_metrics(t_obs, F):
    """Peak time, half-max rise and fall times (linear interpolation)."""
    F = F / F.max()
    ipk = int(np.argmax(F))
    t_pk = t_obs[ipk]
    def cross(seg_t, seg_F):
        idx = np.where(np.diff(seg_F >= 0.5))[0]
        if len(idx) == 0:
            return np.nan
        i = idx[0]
        f0, f1 = seg_F[i], seg_F[i + 1]
        return seg_t[i] + (0.5 - f0) * (seg_t[i + 1] - seg_t[i]) / (f1 - f0)
    t_half_rise = cross(t_obs[:ipk + 1], F[:ipk + 1])
    t_half_fall = cross(t_obs[ipk:], -F[ipk:] + 1.0) if False else None
    # falling crossing: find where F drops below 0.5 after peak
    seg_t, seg_F = t_obs[ipk:], F[ipk:]
    idx = np.where(np.diff(seg_F < 0.5))[0]
    if len(idx):
        i = idx[0]
        f0, f1 = seg_F[i], seg_F[i + 1]
        t_half_fall = seg_t[i] + (f0 - 0.5) * (seg_t[i + 1] - seg_t[i]) / (f0 - f1)
    else:
        t_half_fall = np.nan
    return t_pk, t_half_rise, t_half_fall

print(f"β = {BETA:.6f}  η_geo = {ETA:.6f}")
print("Chromatic-channel timing imprint on the b = 1 confluence (toy SED):\n")
print(f"{'band':>4} {'z':>4} {'Δt_peak[d]':>11} {'Δwidth/width':>13} {'Δ(rise/fall)':>13}")

RES = {}
for band in BANDS:
    for z in (0.1, 0.3, 0.5, 0.8, 1.0):
        t_emit = np.linspace(-15.0, 80.0, 4000)
        t_obs = t_emit * (1.0 + z)                    # b = 1 envelope (both cases)
        Fc = band_flux(t_emit, z, band, chromatic=True)
        F0 = band_flux(t_emit, z, band, chromatic=False)
        pk_c, r_c, f_c = timing_metrics(t_obs, Fc)
        pk_0, r_0, f_0 = timing_metrics(t_obs, F0)
        w_c, w_0 = f_c - r_c, f_0 - r_0
        asym_c = (pk_c - r_c) / (f_c - pk_c)
        asym_0 = (pk_0 - r_0) / (f_0 - pk_0)
        d_pk = pk_c - pk_0
        d_w = (w_c - w_0) / w_0
        d_as = asym_c - asym_0
        RES.setdefault(band, {})[str(z)] = {
            "dt_peak_days": float(d_pk), "dwidth_frac": float(d_w),
            "dasym": float(d_as), "width_days": float(w_c)}
        print(f"{band:>4} {z:>4} {d_pk:>11.4f} {d_w:>13.2e} {d_as:>13.2e}")
    print()

# Achromaticity budget check: the width perturbation acts like a band-dependent
# delta_b ~ dwidth/width / ln(1+z). Compare to White's sigma_b = 0.0112.
print("Effective per-band Δb vs White et al. σ_b = 0.0112 (must be well inside):")
for band in BANDS:
    z = 0.5
    dw = RES[band]["0.5"]["dwidth_frac"]
    db = dw / np.log(1.0 + z)
    print(f"  {band}: Δb_eff ≈ {db:+.2e}  ({abs(db)/0.0112:.1%} of σ_b)")

out = Path(__file__).resolve().parent / "sne_wien_lightcurve_shift_results.json"
out.write_text(json.dumps(RES, indent=2))
print(f"\nresults written to {out.name}")
print("\nRegister: curve-center shift and width perturbation are the chromatic")
print("channel's timing imprint ON the achromatic b = 1 envelope — the confluence.")
print("They are predictions layered on a shared envelope, not the envelope's cause.")
