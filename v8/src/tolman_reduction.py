#!/usr/bin/env python3
"""Static-frame Tolman reduction of Lubin & Sandage 2001 (Papers I + IV).

Executes preregistration/tolman_static_reanalysis.md (Branches Z and E,
Amendment 1). Data: data_ls2001/*.tex (arXiv sources; PROVENANCE.md).

Method (exactly L&S Paper IV, with one substitution):
  per galaxy, per Petrosian eta: Delta<SB> = <SB>_obs(K-corrected)
  - <SB>_local(log R), with the Paper I local relation (z=0 zero points,
  nonlinearity correction of their Table 3; I band offset by <R-I> =
  0.62). n = Delta<SB> / (2.5 log10(1+z)). Final n per band = mean over
  clusters and eta in {1.7, 2.0} (their procedure).
  The static frame enters ONLY through log R -> log R + DlogR_TL, using
  L&S's OWN Table 8 "Tired Light" conversion column (their tired-light
  d_A is identical in form to the model's d_A = (c/H0)ln(1+z); verified
  0.305 vs 0.3046 at z = 0.7565).

VALIDATION GATE (must pass before the static branch is computed): with
zero frame shift the machinery must reproduce L&S's published Tables
5-7 per-eta Delta<SB> to |diff| <= 0.06 mag and the final n_R = 2.59,
n_I = 3.37 to |diff| <= 0.10.

BRANCH E COMMITTED INPUTS (written before any static-frame number was
seen; external stellar-physics values, never fitted to Tolman
residuals): passive-evolution brightening of cluster early-types,
empirical z-scaling from fundamental-plane M/L evolution
(van Dokkum-type dln(M/L_B)/dz ~ -0.46 +/- 0.05, converted to red bands
with single-burst color evolution):
  dM_R_evol(z) = -(0.40 +/- 0.10) * z  mag  (brighter in the past)
  dM_I_evol(z) = -(0.33 +/- 0.08) * z  mag
Under Branch E the model's predicted exponent becomes
n_pred_E = n_eff(z, band) - |dM_evol|/(2.5 log10(1+z)).
"""
from __future__ import annotations

import os
import re

import numpy as np

from rawframe.da_tolman import n_eff

DDIR = os.path.join(os.path.dirname(__file__), "..", "..", "data_ls2001")

ETAS = (1.0, 1.3, 1.5, 1.7, 2.0)
FINAL_ETAS = (1.7, 2.0)
R_MINUS_I = 0.62

# Paper I Table 2 (R band, z=0 zero points): eta -> (slope a, zeropoint b)
LOCAL = {1.0: (2.97, 7.93), 1.3: (3.46, 5.73), 1.5: (3.39, 6.13),
         1.7: (3.11, 7.62), 2.0: (2.97, 8.53)}
# Paper I Table 3: nonlinearity correction Delta<SB>(log R)
NL_X = np.array([3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0,
                 4.1, 4.2, 4.3, 4.4, 4.5])
NL_Y = np.array([-1.07, -0.97, -0.86, -0.76, -0.67, -0.57, -0.48, -0.39,
                 -0.30, -0.22, -0.13, -0.05, 0.02])

# Paper IV: clusters (table number in tolman4.tex, z, band, tired-light
# Dlog R from their Table 8, published per-eta (DSB, n) from Tables 5-7)
CLUSTERS = {
    "Cl1604+4321": dict(tab=2, z=0.9243, band="R", dlogR_TL=0.354,
                        pub={1.0: (2.44, 3.43), 1.3: (2.24, 3.15),
                             1.5: (2.21, 3.11), 1.7: (1.96, 2.76),
                             2.0: (1.76, 2.48)}),
    "Cl1324+3011": dict(tab=3, z=0.7565, band="I", dlogR_TL=0.305,
                        pub={1.0: (2.54, 4.15), 1.3: (2.33, 3.81),
                             1.5: (2.33, 3.81), 1.7: (2.13, 3.48),
                             2.0: (1.99, 3.25)}),
    "Cl1604+4304": dict(tab=4, z=0.8967, band="I", dlogR_TL=0.346,
                        pub={1.0: (2.92, 4.20), 1.3: (2.73, 3.93),
                             1.5: (2.72, 3.91), 1.7: (2.43, 3.50),
                             2.0: (2.29, 3.29)}),
}
PUBLISHED_FINAL = {"R": (2.59, 0.17), "I": (3.37, 0.13)}
BAND_LAM = {"R": 658.0, "I": 806.0}

DM_EVOL = {"R": (0.40, 0.10), "I": (0.33, 0.08)}  # per unit z, committed


def nl_corr(logR):
    """Nonlinearity correction: per Paper IV's text, the Paper I linear
    lines 'need to be made FAINTER by the absolute value of the
    corrections listed in Table 3' (extension to small radii via
    Sandage & Perelmuter 1991)."""
    return abs(float(np.interp(logR, NL_X, NL_Y, right=0.02)))


def sb_local(eta, logR, band):
    a, b = LOCAL[eta]
    # Paper I Table 2: the eta = 1.0 relation is valid to log R > 3.0 and
    # needs no small-radius extension; the Table 3 fainter-correction
    # applies to the eta >= 1.3 relations (valid range log R > 4.4).
    sb = a * logR + b + (nl_corr(logR) if eta >= 1.3 else 0.0)
    if band == "I":
        sb -= R_MINUS_I
    return sb


def parse_cluster_table(texpath, tablenum):
    """Parse a Paper IV per-galaxy deluxetable -> list of eta->(SB, logR)."""
    tex = open(texpath).read()
    m = re.search(r"\\tablenum\{%d\}(.*?)\\enddata" % tablenum, tex, re.S)
    block = m.group(1)
    body = block.split(r"\startdata")[1]
    gals = []
    for line in body.strip().splitlines():
        line = line.strip().rstrip("\\").strip()
        if not line or line.startswith("%"):
            continue
        line = re.sub(r"\\tablenotemark\{\w\}", "", line)
        cells = [c.strip() for c in line.split("&")]
        if len(cells) != 16:
            continue
        row = {}
        for i, eta in enumerate(ETAS):
            sb_s, lr_s = cells[2 + 3 * i], cells[3 + 3 * i]
            if r"\nodata" in sb_s or r"\nodata" in lr_s:
                continue
            row[eta] = (float(sb_s), float(lr_s))
        gals.append(row)
    return gals


def reduce(shift=0.0, verbose=True):
    """Run the reduction with log R -> log R + shift_cluster.
    shift=0 -> q0=1/2 frame (validation); shift='TL' -> static frame."""
    out = {}
    for name, c in CLUSTERS.items():
        gals = parse_cluster_table(
            os.path.join(DDIR, "tolman4.tex"), c["tab"])
        dl = c["dlogR_TL"] if shift == "TL" else float(shift)
        fac = 1.0 / (2.5 * np.log10(1.0 + c["z"]))
        res = {}
        for eta in ETAS:
            dsb = [sb - sb_local(eta, lr + dl, c["band"])
                   for g in gals if eta in g for sb, lr in [g[eta]]]
            dsb = np.array(dsb)
            m, e = dsb.mean(), dsb.std(ddof=1) / np.sqrt(len(dsb))
            res[eta] = (m, e, m * fac, e * fac, len(dsb))
        out[name] = res
        if verbose:
            tag = "static" if shift == "TL" else "q0=1/2"
            print(f"  {name} ({c['band']}, z={c['z']}, {tag}):")
            for eta in ETAS:
                m, e, n, ne, N = res[eta]
                pub = c["pub"][eta]
                extra = (f"  [pub {pub[0]:.2f}/{pub[1]:.2f}]"
                         if shift == 0.0 else "")
                print(f"    eta={eta}: DSB={m:5.2f}+/-{e:.2f}  "
                      f"n={n:5.2f}+/-{ne:.2f}  N={N}{extra}")
    return out


def final_n(out):
    """Mean over clusters and eta in {1.7, 2.0}, per band (L&S procedure)."""
    fin = {}
    for band in ("R", "I"):
        vals, errs = [], []
        for name, c in CLUSTERS.items():
            if c["band"] != band:
                continue
            for eta in FINAL_ETAS:
                _, _, n, ne, _ = out[name][eta]
                vals.append(n)
                errs.append(ne)
        fin[band] = (float(np.mean(vals)),
                     float(np.mean(errs) / np.sqrt(len(vals))))
    return fin


def main():
    print("== VALIDATION GATE (q0=1/2 frame; must reproduce L&S) ==")
    out0 = reduce(0.0)
    ok = True
    for name, c in CLUSTERS.items():
        for eta in ETAS:
            if abs(out0[name][eta][0] - c["pub"][eta][0]) > 0.06:
                ok = False
                print(f"  MISMATCH {name} eta={eta}: "
                      f"{out0[name][eta][0]:.2f} vs pub {c['pub'][eta][0]:.2f}")
    f0 = final_n(out0)
    for band in ("R", "I"):
        pm, pe = PUBLISHED_FINAL[band]
        print(f"  final n_{band} (q0=1/2) = {f0[band][0]:.2f} +/- "
              f"{f0[band][1]:.2f}   [published {pm} +/- {pe}]")
        if abs(f0[band][0] - pm) > 0.10:
            ok = False
    print("VALIDATION", "PASS" if ok else "FAIL")
    if not ok:
        return

    print("\n== BRANCH Z: static frame (L&S Table 8 tired-light Dlog R), "
          "zero evolution ==")
    outS = reduce("TL")
    fS = final_n(outS)
    zbar = {b: np.mean([c["z"] for c in CLUSTERS.values() if c["band"] == b])
            for b in ("R", "I")}
    print("\n  Band Z results vs model prediction:")
    for band in ("R", "I"):
        n, ne = fS[band]
        pred = n_eff(zbar[band], BAND_LAM[band])
        t = (n - pred) / ne
        print(f"  n_{band}(static) = {n:.2f} +/- {ne:.2f}   "
              f"model n_eff = {pred:.2f}   tension = {t:+.1f} sigma")
    dspread = fS["I"][0] - fS["R"][0]
    espread = np.hypot(fS["I"][1], fS["R"][1])
    pspread = (n_eff(zbar["I"], BAND_LAM["I"])
               - n_eff(zbar["R"], BAND_LAM["R"]))
    print(f"  band spread n_I - n_R = {dspread:+.2f} +/- {espread:.2f}   "
          f"model predicts {pspread:+.2f}   "
          f"({abs(dspread - pspread)/espread:.1f} sigma)")

    print("\n== BRANCH E: committed passive-evolution correction over "
          "static lookback ==")
    for band in ("R", "I"):
        n, ne = fS[band]
        dm, dme = DM_EVOL[band]
        z = zbar[band]
        shift = dm * z / (2.5 * np.log10(1 + z))
        shifte = dme * z / (2.5 * np.log10(1 + z))
        pred = n_eff(z, BAND_LAM[band]) - shift
        t = (n - pred) / np.hypot(ne, shifte)
        print(f"  n_{band}(static) = {n:.2f} +/- {ne:.2f}   "
              f"pred(E) = {pred:.2f} +/- {shifte:.2f}   "
              f"tension = {t:+.1f} sigma")


if __name__ == "__main__":
    main()
