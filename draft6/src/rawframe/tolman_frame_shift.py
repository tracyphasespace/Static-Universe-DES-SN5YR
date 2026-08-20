#!/usr/bin/env python3
"""Frame-dependence of the Lubin & Sandage Tolman exponents — analytic estimate.

L&S 2001 (Paper IV, AJ 122, 1084) fit n in <SB> ~ (1+z)^(-n) for 34 early-type
galaxies in three clusters (z = 0.76, 0.90, 0.92), assigning linear radii with
FLRW angular-diameter distances. They publish n for three deceleration
parameters, which measures the bundled sensitivity of n to the assumed
distance scale:

    q0:     0       1/2     1
    n_R:    2.28    2.59    2.81   (+/- 0.17)
    n_I:    3.06    3.37    3.55   (+/- 0.13)

This script (1) calibrates S = dn/dlog10(d_A) per band from those three points
(linearity check included), (2) extrapolates to the static-frame distance
d_A = D = (c/K) ln(1+z) with K = H0, (3) compares to the two-channel
prediction n_eff(z, lam) = 2 + (tau_inf(lam)/2)(1+z)^(-1/2), and (4) reports
the frame-INVARIANT discriminant: the I-R band spread, which no distance
reassignment can move (distance shifts are band-independent).

Caveat printed with the result: the calibration spans ~0.1 dex in d_A and the
static frame sits ~0.35 dex away — a 3.5x linear extrapolation. It licenses
"the face-value 9.2 sigma is frame-fragile", NOT "the tension is resolved".
The full reduction (preregistration/tolman_static_reanalysis.md) decides.
"""
from __future__ import annotations

import numpy as np

from rawframe.da_tolman import n_eff, BANDS

CLUSTER_Z = (0.76, 0.90, 0.92)
Q0_GRID = (0.0, 0.5, 1.0)
LS_N = {"rest-R": (2.28, 2.59, 2.81), "rest-I": (3.06, 3.37, 3.55)}
LS_ERR = {"rest-R": 0.17, "rest-I": 0.13}
LS_BAND_LAM = {"rest-R": BANDS["rest-R"], "rest-I": BANDS["rest-I"]}


def d_a_mattig(z: float, q0: float) -> float:
    """FLRW angular-diameter distance, units c/H0 (Mattig; q0=0 -> Milne)."""
    if q0 == 0.0:
        dl = z * (1.0 + z / 2.0)
    else:
        dl = (q0 * z + (q0 - 1.0) * (np.sqrt(2.0 * q0 * z + 1.0) - 1.0)) / q0**2
    return dl / (1.0 + z) ** 2


def d_a_static(z: float) -> float:
    """Static Euclidean d_A = D = (c/K) ln(1+z), K = H0, units c/H0."""
    return np.log(1.0 + z)


def mean_logd(dist_fn) -> float:
    return float(np.mean([np.log10(dist_fn(z)) for z in CLUSTER_Z]))


def main():
    logd_flrw = {q0: mean_logd(lambda z, q0=q0: d_a_mattig(z, q0)) for q0 in Q0_GRID}
    logd_stat = mean_logd(d_a_static)
    zbar = float(np.mean(CLUSTER_Z))

    print("Mean log10 d_A over clusters z =", CLUSTER_Z, "(units c/H0):")
    for q0 in Q0_GRID:
        print(f"  FLRW q0={q0:<4}: {logd_flrw[q0]:+.4f}")
    print(f"  static d=ln(1+z): {logd_stat:+.4f}"
          f"   (offset from q0=1/2: {logd_stat - logd_flrw[0.5]:+.4f} dex)")

    print("\nCalibration of S = dn/dlog10(d_A) from L&S's own q0 grid:")
    x = np.array([logd_flrw[q] for q in Q0_GRID])
    results = {}
    for band, ns in LS_N.items():
        y = np.array(ns)
        slope, icpt = np.polyfit(x, y, 1)
        resid = y - (slope * x + icpt)
        n_stat = slope * logd_stat + icpt
        pred = n_eff(zbar, LS_BAND_LAM[band])
        err = LS_ERR[band]
        results[band] = (n_stat, pred, err)
        print(f"  {band}: S = {slope:+.2f} per dex (linearity residual "
              f"{np.max(np.abs(resid)):.3f});  n_static = {n_stat:.2f} +/- {err} (stat)")
        print(f"        prediction n_eff(z={zbar:.2f}) = {pred:.2f}"
              f"  -> static-frame tension {(n_stat - pred) / err:+.1f} sigma"
              f"  (was {(ns[1] - pred) / err:+.1f} sigma in the q0=1/2 frame)")

    dI, dR = LS_N["rest-I"][1] - LS_N["rest-R"][1], 0.0
    spread_err = float(np.hypot(LS_ERR["rest-I"], LS_ERR["rest-R"]))
    spread_pred = (n_eff(zbar, LS_BAND_LAM["rest-I"])
                   - n_eff(zbar, LS_BAND_LAM["rest-R"]))
    print(f"\nFrame-INVARIANT discriminant — the I-R band spread:")
    print(f"  measured n_I - n_R = {dI:.2f} +/- {spread_err:.2f} "
          f"(shifts by <0.05 across the whole q0 grid)")
    print(f"  model predicts     = {spread_pred:+.2f}")
    print(f"  -> {abs(dI - spread_pred) / spread_err:.1f} sigma in ANY distance frame;"
          f" this, not the 9.2, is the irreducible Tolman discrepancy.")
    print("\nCaveat: 3.5x linear extrapolation of a 0.1-dex calibration; the full")
    print("static-frame reduction (preregistered) is the decisive test.")


if __name__ == "__main__":
    main()
