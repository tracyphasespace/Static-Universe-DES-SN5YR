#!/usr/bin/env python3
"""Observer-frame transfer integral through real DES griz filters.

Implements the full static-model transfer operator on the Hsiao SN Ia
template (sncosmo) and real DES bandpasses:

  F_b(t_obs; z) = A(z) * INT T_b(lam_o) e^{-tau(lam_o/(1+z), z)}
                          S(lam_o/(1+z), t_obs/(1+z)) lam_o dlam_o

(wake ON: t_rest = t_obs/(1+z); wake OFF: t_rest = t_obs; photon-counting
weight lam_o; achromatic normalization A(z) drops out of every measurement
below). tau is the non-forward Kelvin opacity, tau_inf,B = 0.594,
tau ~ lam^(-1/2) (from rawframe.da_tolman).

Measurements per (band, z), against a MATCHED-REST reference (same rest
wavelength coverage, opacity off, no time remap — this removes the
band-ladder quantization identified in the inverse-injection campaign):

  1. Fitted stretch s-hat. Wake ON: s-hat/(1+z) - 1 = shape residual from
     chromatic reweighting (expected small). Wake OFF: s-hat - 1 = the
     apparent broadening from amplitude erosion + filter slicing alone
     (the reviewer's 'flattening' mechanism) — expected ~0, consistent
     with the registered inverse-injection result b-hat = 0.0000.
  2. Secondary-maximum phase (i/z bands): t2_obs/(1+z) vs the reference
     t2 — the FeIII->FeII recombination clock riding the same remap.
  3. Peak-epoch g-r color with opacity on vs off — the erosion the SALT
     machinery absorbs into c.
  4. The 341/660 nm line-amplitude erosion table (analytic).
"""
from __future__ import annotations

import numpy as np
import scipy.optimize as so
import scipy.signal as ss

from rawframe.da_tolman import tau as kelvin_tau

REST_WIN = (-10.0, 45.0)  # rest-frame fit window, days
ZS = (0.1, 0.3, 0.5, 0.8)
BANDS = "griz"


def _sed():
    import sncosmo
    return (sncosmo.get_source("hsiao"),
            {b: sncosmo.get_bandpass(f"des{b}") for b in BANDS})


def band_curve(src, bp, z, t_rest, opacity=True):
    """Integrated band flux at rest phases t_rest for a source at z."""
    lam_o = np.linspace(bp.minwave(), bp.maxwave(), 300)
    lam_r = lam_o / (1.0 + z)
    w = bp(lam_o) * lam_o
    if opacity:
        w = w * np.exp(-kelvin_tau(z, lam_r / 10.0))  # tau takes nm
    return np.array([np.trapezoid(src.flux(p, lam_r) * w, lam_o)
                     for p in t_rest])


def fit_stretch(t_obs, f_obs, t_ref, f_ref):
    """LSQ stretch/amplitude of obs curve onto reference."""
    fr = f_ref / f_ref.max()
    fo = f_obs / f_obs.max()

    def resid(p):
        s, a = p
        return a * np.interp(t_obs / s, t_ref, fr, left=np.nan,
                             right=np.nan) - fo

    def cost(p):
        r = resid(p)
        return np.nansum(r * r)

    res = so.minimize(cost, x0=[1.0, 1.0], method="Nelder-Mead",
                      options={"xatol": 1e-6, "fatol": 1e-12})
    return res.x[0]


def secondary_max(t, f):
    pk, _ = ss.find_peaks(f)
    late = [i for i in pk if t[i] > 10.0]
    return t[late[0]] if late else np.nan


def main():
    src, bps = _sed()
    t_rest = np.linspace(*REST_WIN, 221)

    print("Stretch recovered against matched-rest reference"
          " (values are s-hat/(1+z) for wake ON, s-hat for wake OFF):")
    print(f"  {'z':>4} " + "".join(f"{b + ' ON':>9}" for b in BANDS)
          + "".join(f"{b + ' OFF':>9}" for b in BANDS))
    for z in ZS:
        row_on, row_off = [], []
        for b in BANDS:
            ref = band_curve(src, bps[b], z, t_rest, opacity=False)
            obs = band_curve(src, bps[b], z, t_rest, opacity=True)
            # wake ON: observer curve is obs sampled at t_obs=(1+z)t_rest
            s_on = fit_stretch((1 + z) * t_rest, obs, t_rest, ref)
            # wake OFF: no time remap — same rest phases
            s_off = fit_stretch(t_rest, obs, t_rest, ref)
            row_on.append(s_on / (1 + z))
            row_off.append(s_off)
        print(f"  {z:>4} " + "".join(f"{v:>9.4f}" for v in row_on)
              + "".join(f"{v:>9.4f}" for v in row_off))

    print("\nSecondary-maximum clock (rest phase of the FeIII->FeII bump,")
    print("observer value divided by (1+z); reference in parentheses):")
    for b in ("i", "z"):
        ref0 = band_curve(src, bps[b], 0.0, t_rest, opacity=False)
        t2_0 = secondary_max(t_rest, ref0)
        vals = []
        for z in ZS:
            obs = band_curve(src, bps[b], z, t_rest, opacity=True)
            t2 = secondary_max((1 + z) * t_rest, obs) / (1 + z)
            vals.append(f"z={z}: {t2:5.2f}d")
        print(f"  des{b} (ref {t2_0:5.2f}d at z=0): " + "  ".join(vals))

    print("\nPeak-epoch g-r color shift from chromatic opacity (mag):")
    for z in ZS:
        d = {}
        for b in ("g", "r"):
            on = band_curve(src, bps[b], z, np.array([0.0]), opacity=True)
            off = band_curve(src, bps[b], z, np.array([0.0]), opacity=False)
            d[b] = -2.5 * np.log10(on[0] / off[0])
        print(f"  z={z}: Delta(g-r) = {d['g'] - d['r']:+.4f}")

    print("\nPer-band PEAK-TIME displacement from opacity alone (days; wake off,")
    print("opacity-on peak epoch minus opacity-off peak epoch — the 'joint")
    print("trajectory' timing axis; nonzero only via phase-dependent SED color):")
    tf = np.linspace(-8.0, 8.0, 321)
    for z in ZS:
        row = []
        for b in BANDS:
            on = band_curve(src, bps[b], z, tf, opacity=True)
            off = band_curve(src, bps[b], z, tf, opacity=False)
            row.append(tf[on.argmax()] - tf[off.argmax()])
        print(f"  z={z}: " + "  ".join(f"{b}:{v:+.2f}" for b, v in zip(BANDS, row)))

    print("\nBlue/red spectral-interval ratio Q(z,t) = exp(-Delta tau), using the")
    print("broad intervals 3200-3400 / 6200-6800 A (NOT clean Ni lines — blended;")
    print("effective 330/650 nm). Model predicts Q PHASE-FLAT (tau has no t):")
    dt_inf = 0.594 * (np.sqrt(440 / 330.0) - np.sqrt(440 / 650.0))
    print(f"  Delta tau_inf(330,650) = {dt_inf:.3f}")
    for z in (0.25, 0.5, 1.0):
        path = 1.0 - (1.0 + z) ** -0.5
        dtau = dt_inf * path
        print(f"  z={z}: Q = {np.exp(-dtau):.3f}  "
              f"(suppression {100 * (1 - np.exp(-dtau)):.1f}%, {1.0857 * dtau:.3f} mag)"
              f" — identical at every phase")

    print("\n341nm/660nm single-line illustration (analytic, tau_inf 0.675/0.485):")
    for z in (0.25, 0.5, 1.0):
        dtau = float(kelvin_tau(z, 341.0) - kelvin_tau(z, 660.0))
        print(f"  z={z}: ratio suppressed by {100 * (1 - np.exp(-dtau)):.1f}%"
              f"  ({1.0857 * dtau:.3f} mag)")


if __name__ == "__main__":
    main()
