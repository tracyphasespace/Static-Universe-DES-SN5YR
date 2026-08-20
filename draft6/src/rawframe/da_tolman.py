#!/usr/bin/env python3
"""Producer for DA_TOLMAN_DERIVATION.md — every number in that document.

Model inputs (canon):
  - Non-forward Kelvin channel: tau(z, lam) = tau_inf(lam) * [1 - (1+z)^(-1/2)]
    with tau_inf(lam) = TAU_INF_B * (440 nm / lam)^(1/2)  (sigma_nf ~ E^1/2).
  - Opacity convention (referee Issue 6): Delta_m = (2.5/ln10) * tau, so the
    fitted eta = 0.297 (a magnitude coefficient) corresponds to a physical
    optical depth TAU_INF_B = 2 * eta = 0.594 at rest-B.
  - Geometry: static Euclidean, d_A = D = (c/K) ln(1+z)  (derived, Section 1).

Outputs: tau ledger, Tolman n_eff per band vs Lubin & Sandage 2001,
color-drift prediction E(B-V)(z) + effective R_V, raw DES c(z) slope
(selection-confounded — comparison requires a selection model), and the
(1+z)^2 radiance excess over a true blackbody at T/(1+z).
"""
from __future__ import annotations

import numpy as np

ETA_FIT = 0.297           # magnitude-space coefficient from the released-vector fit
TAU_INF_B = 2.0 * ETA_FIT  # physical optical depth at rest-B (440 nm)
LAM_B, LAM_V = 440.0, 550.0
BANDS = {"rest-B": 440.0, "rest-R": 658.0, "rest-I": 806.0}
MAG_PER_TAU = 2.5 / np.log(10.0)

# Lubin & Sandage (2001, Paper IV) measured Tolman exponents
LS = {"rest-R": (2.59, 0.17), "rest-I": (3.37, 0.13)}


def tau_inf(lam_nm: float) -> float:
    return TAU_INF_B * np.sqrt(LAM_B / lam_nm)


def tau(z, lam_nm: float):
    return tau_inf(lam_nm) * (1.0 - (1.0 + np.asarray(z)) ** -0.5)


def n_eff(z: float, lam_nm: float) -> float:
    """Local Tolman exponent: n = -d ln SB / d ln(1+z) = 2 + (1+z) dtau/dz."""
    return 2.0 + 0.5 * tau_inf(lam_nm) * (1.0 + z) ** -0.5


def ebv(z) -> np.ndarray:
    """Predicted mean reddening drift in magnitudes (rest B-V)."""
    return MAG_PER_TAU * (tau(z, LAM_B) - tau(z, LAM_V))


def raw_c_slope():
    """Raw SALT-c vs zHD slope on the DES subset (selection-confounded)."""
    from rawframe.data import load_hd
    hd = load_hd(metadata=True)
    des = hd[hd.IDSURVEY == 10]
    z, c = des.zHD.to_numpy(), des.c.to_numpy()
    A = np.column_stack([np.ones_like(z), z])
    coef, res, *_ = np.linalg.lstsq(A, c, rcond=None)
    dof = len(z) - 2
    sig2 = res[0] / dof
    cov = sig2 * np.linalg.inv(A.T @ A)
    return len(z), coef[1], np.sqrt(cov[1, 1])


def main():
    print(f"tau_inf(rest-B 440nm) = {TAU_INF_B:.3f}  (= 2*eta, eta = {ETA_FIT})")
    for z in (0.5, 1.0):
        t = float(tau(z, LAM_B))
        print(f"  tau(z={z}) = {t:.3f} -> beam fraction removed = {1 - np.exp(-t):.3f}")

    print("\nTolman n_eff at z=0.5 (prediction) vs Lubin & Sandage 2001:")
    for band, lam in BANDS.items():
        n = n_eff(0.5, lam)
        line = f"  {band:7s} ({lam:.0f}nm): n_eff = {n:.2f}"
        if band in LS:
            m, s = LS[band]
            line += f"   L&S: {m:.2f} +/- {s:.2f}  -> tension {abs(m - n) / s:.1f} sigma"
        print(line)
    dn = LS["rest-I"][0] - LS["rest-R"][0]
    sn = np.hypot(LS["rest-I"][1], LS["rest-R"][1])
    print(f"  L&S internal I-R spread: {dn:.2f} +/- {sn:.2f} "
          f"({dn / sn:.1f} sigma under any single-exponent law; model predicts I < R)")

    print("\nColor drift prediction (rest B-V reddening from lam^(-1/2) opacity):")
    for z in (0.25, 0.5, 1.0):
        print(f"  E(B-V)(z={z}) = {float(ebv(z)):+.4f} mag")
    zg = np.linspace(0.0, 1.0, 201)
    slope = np.polyfit(zg, ebv(zg), 1)[0]
    rv = tau_inf(LAM_V) / (tau_inf(LAM_B) - tau_inf(LAM_V))
    print(f"  linear slope z in [0,1]: {slope:+.4f} mag/z (REDWARD); effective R_V = {rv:.1f}")

    try:
        n, b, se = raw_c_slope()
        print(f"\nRaw DES c(z) slope ({n} SNe, IDSURVEY=10): {b:+.4f} +/- {se:.4f} mag/z"
              f"  (BLUEWARD -- selection-confounded; not comparable without a selection model)")
    except Exception as e:  # data not present on this machine
        print(f"\nRaw DES c(z) slope: skipped ({e})")

    print("\nRadiance excess over true blackbody at T/(1+z): 5*log10(1+z) =")
    for z in (0.1, 0.3, 0.5):
        print(f"  z={z}: {5 * np.log10(1 + z):.2f} mag")


if __name__ == "__main__":
    main()
