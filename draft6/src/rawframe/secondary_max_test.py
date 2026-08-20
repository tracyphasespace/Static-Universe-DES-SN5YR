#!/usr/bin/env python3
"""T4: secondary-maximum phase test on raw DES i/z photometry.

Executes preregistration/secondary_maximum_phase.md (Amendment 2, frozen
BEFORE this script first ran). Estimator, peak finder, cuts, censoring,
and bootstrap are all as frozen there. Implementation details not covered
by the freeze, disclosed here and identical for every SN (hypothesis-
neutral): (a) multi-season raw photometry is windowed to
PKMJD-40 .. PKMJD+110 observer days before fitting (the raw table carries
all DES seasons; the window is a season selector, not part of the
estimator); (b) the regression is unweighted OLS (the freeze did not
specify weights); (c) spectroscopic subtype (C-e) is not available in the
DES HD metadata — stratification not executable, reported as such.

Outputs: per-SN measurements, censoring log, detection-efficiency test,
primary regression y = a + b2*x + gamma*(x1-x1bar), bootstrap sigma(b2).
Writes results JSON next to this package under results/.
"""
from __future__ import annotations

import json
import os

import numpy as np
import scipy.signal as ss

from rawframe.data import load_raw_photometry, load_hd
from rawframe.transfer_integral import _sed, band_curve

SEED = 20260820
GRID_STEP = 0.25          # d, GP posterior grid
GP_LEN = 10.0             # d, Matern-3/2 length scale (frozen)
N_DRAWS = 64              # posterior draws for sigma(t2) (frozen)
N_BOOT = 2000             # bootstrap resamples (frozen)
Z_RANGE = (0.05, 0.30)
SEASON = (-40.0, 110.0)   # around PKMJD (disclosed implementation detail)
BANDS_T4 = ("i", "z")


def matern32(t1, t2, ell):
    r = np.abs(t1[:, None] - t2[None, :]) / ell
    s = np.sqrt(3.0) * r
    return (1.0 + s) * np.exp(-s)


def gp_fit(t, f, sig, tg):
    """Posterior mean/cov of a Matern-3/2 GP (frozen hyperparameters).

    Centered on the inverse-variance-weighted mean (a zero-mean prior on
    raw flux sags toward zero between epochs — implementation bug fixed
    2026-08-20, documented in the run report)."""
    w = 1.0 / sig**2
    mu0 = float(np.sum(w * f) / np.sum(w))
    fc = f - mu0
    amp = np.var(fc)
    K = amp * matern32(t, t, GP_LEN) + np.diag(sig**2)
    Ks = amp * matern32(tg, t, GP_LEN)
    Kss = amp * matern32(tg, tg, GP_LEN)
    L = np.linalg.cholesky(K + 1e-12 * np.eye(len(t)))
    alpha = np.linalg.solve(L.T, np.linalg.solve(L, fc))
    V = np.linalg.solve(L, Ks.T)
    return Ks @ alpha + mu0, Kss - V.T @ V


def loo_clip(t, f, sig, thresh=5.0, max_iter=5):
    """Amendment 3: leave-one-out epoch screening at 5 sigma.

    Greedy iterative form: remove the single worst offender, refit,
    repeat (an artifact left in the reference set otherwise condemns its
    genuine neighbors — collateral-damage bug fixed 2026-08-20)."""
    keep = np.ones(len(t), bool)
    for _ in range(max_iter):
        idx = np.where(keep)[0]
        if len(idx) < 5:
            break
        worst_r, worst_i = 0.0, None
        w = 1.0 / sig[idx] ** 2
        mu0 = float(np.sum(w * f[idx]) / np.sum(w))
        for i in idx:
            m = keep.copy()
            m[i] = False
            amp = np.var(f[m] - mu0)
            K = amp * matern32(t[m], t[m], GP_LEN) + np.diag(sig[m] ** 2)
            Ks = amp * matern32(t[i:i + 1], t[m], GP_LEN)
            sol = np.linalg.solve(K, f[m] - mu0)
            mu = float((Ks @ sol).item()) + mu0
            var = float((amp - Ks @ np.linalg.solve(K, Ks.T)).item())
            r = abs(f[i] - mu) / np.sqrt(sig[i] ** 2 + max(var, 0.0))
            if r > worst_r:
                worst_r, worst_i = r, i
        if worst_r > thresh and worst_i is not None:
            keep[worst_i] = False
        else:
            break
    return keep


def first_peak(tg, mean, t_lo, t_hi, prom):
    """First local max of `mean` with tg in (t_lo, t_hi), prominence>=prom."""
    pk, props = ss.find_peaks(mean, prominence=prom)
    for i in pk:
        if t_lo < tg[i] < t_hi:
            return tg[i]
    return None


def model_dt_grid(src, bps):
    """Rest-frame peak-to-secondary separation Delta t_model(z, band)."""
    zg = np.arange(0.04, 0.325, 0.01)
    tr = np.arange(-10.0, 48.0, 0.1)
    out = {}
    for b in BANDS_T4:
        vals = []
        for z in zg:
            c = band_curve(src, bps[b], z, tr, opacity=True)
            tp = tr[c.argmax()]
            pk, _ = ss.find_peaks(c)
            t2s = [tr[i] for i in pk if tp + 8.0 < tr[i] < tp + 40.0]
            vals.append(t2s[0] - tp if t2s else np.nan)
        out[b] = (zg, np.array(vals))
    return out


def measure_sn(g, pkmjd, dt_model):
    """Measure y contributions for one SN. Returns (band_results, censor)."""
    res, censor = {}, {}
    for b in BANDS_T4:
        dm = dt_model.get(b)
        if dm is None or not np.isfinite(dm):
            continue
        d = g[(g.band == b) & g.valid_err].copy()
        d = d[(d.mjd > pkmjd + SEASON[0]) & (d.mjd < pkmjd + SEASON[1])]
        if len(d) < 5:
            continue
        t = d.mjd.to_numpy(float)
        f = d.flux_nu_jy.to_numpy(float)
        sig = d.flux_nu_jy_err.to_numpy(float)
        scale = np.abs(f).max()             # normalize to O(1): the GP/
        f, sig = f / scale, sig / scale     # clip jitters are absolute
        keep = loo_clip(t, f, sig)          # Amendment 3
        t, f, sig = t[keep], f[keep], sig[keep]
        if len(t) < 5:
            continue
        tg = np.arange(t.min(), t.max() + GRID_STEP, GRID_STEP)
        mean, cov = gp_fit(t, f, sig, tg)
        ipk = mean.argmax()
        t_peak = tg[ipk]
        if t_peak - t.min() < 5.0 or t.max() - t_peak < 5.0:
            continue  # peak not interior
        w15 = (t > t_peak + 15) & (t < t_peak + 45)
        if w15.sum() < 3 or np.min(np.abs(t - t_peak)) > 7.0:
            continue
        w10 = (t > t_peak + 10) & (t < t_peak + 45)
        prom = np.median(sig[w10]) if w10.any() else np.median(sig)
        t2 = first_peak(tg, mean, t_peak + 10, t_peak + 45, prom)
        if t2 is None:
            censor[b] = "no_significant_t2"
            continue
        rng = np.random.default_rng(SEED)
        cov = cov + 1e-12 * np.eye(len(tg))
        draws = rng.multivariate_normal(mean, cov, size=N_DRAWS,
                                        method="cholesky")
        t2d = [first_peak(tg, dr, t_peak + 10, t_peak + 45, prom)
               for dr in draws]
        t2d = [v for v in t2d if v is not None]
        if len(t2d) < N_DRAWS // 2:
            censor[b] = "draws_failed"
            continue
        res[b] = {"dt_obs": t2 - t_peak, "dt_model": dm,
                  "sig_t2": float(np.std(t2d))}
    return res, censor


def main():
    src, bps = _sed()
    print("Building Delta t_model(z, band) grid ...")
    grid = model_dt_grid(src, bps)
    for b in BANDS_T4:
        zg, v = grid[b]
        ok = np.isfinite(v)
        print(f"  des{b}: bump visible z in [{zg[ok].min():.2f}, "
              f"{zg[ok].max():.2f}]; Dt_model at edges "
              f"{v[ok][0]:.1f} -> {v[ok][-1]:.1f} d (rest)")

    hd = load_hd(metadata=True)
    hd = hd[(hd.IDSURVEY == 10) & (hd.PROBCC_BEAMS < 0.1)
            & hd.x1.notna() & hd.PKMJD.notna()
            & (hd.zHD >= Z_RANGE[0]) & (hd.zHD <= Z_RANGE[1])]
    print(f"\nSample after HD cuts: {len(hd)} SNe (z in {Z_RANGE})")

    raw = load_raw_photometry()
    raw["snid"] = raw.snid.astype(str)
    hd = hd.assign(CID=hd.CID.astype(str))
    raw_g = dict(list(raw.groupby("snid")))

    rows, censored, eligible = [], [], []
    for _, r in hd.iterrows():
        g = raw_g.get(str(r.CID))
        if g is None:
            continue
        dt_model = {b: float(np.interp(r.zHD, grid[b][0], grid[b][1],
                                       left=np.nan, right=np.nan))
                    for b in BANDS_T4}
        res, cen = measure_sn(g, float(r.PKMJD), dt_model)
        snr_med = float(np.median(g[g.valid_err].snr)) if g.valid_err.any() else 0.0
        if res:
            y = float(np.mean([np.log(v["dt_obs"] / v["dt_model"])
                               for v in res.values()]))
            rows.append({"cid": r.CID, "z": float(r.zHD), "x1": float(r.x1),
                         "y": y, "bands": {b: v for b, v in res.items()},
                         "snr": snr_med})
            eligible.append((float(r.zHD), float(r.x1), snr_med, 1))
        elif cen:
            censored.append({"cid": r.CID, "z": float(r.zHD),
                             "x1": float(r.x1), "why": cen})
            eligible.append((float(r.zHD), float(r.x1), snr_med, 0))

    n_det, n_cen = len(rows), len(censored)
    print(f"Detections: {n_det}   censored (window ok, no significant t2): {n_cen}")
    if n_det < 10:
        print("FEWER THAN 10 DETECTIONS — report and stop per quality floor.")

    # Detection-efficiency test (frozen): z bins [0.05,0.15) vs [0.15,0.30]
    el = np.array(eligible)
    for lo, hi, name in ((0.05, 0.15, "low-z"), (0.15, 0.301, "high-z")):
        m = (el[:, 0] >= lo) & (el[:, 0] < hi)
        if m.any():
            det = el[m, 3]
            print(f"  {name}: eligible {int(m.sum())}, detection frac "
                  f"{det.mean():.2f}, mean x1 (det) "
                  f"{el[m & (el[:, 3] == 1), 1].mean():+.2f}")
    m1, m2 = (el[:, 0] < 0.15), (el[:, 0] >= 0.15)
    if m1.any() and m2.any():
        p1, p2 = el[m1, 3].mean(), el[m2, 3].mean()
        n1, n2 = m1.sum(), m2.sum()
        p = el[:, 3].mean()
        se = np.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
        zstat = (p1 - p2) / se if se > 0 else 0.0
        flag = "FLAGGED" if abs(zstat) > 2 else "ok"
        print(f"  detection-fraction difference: {p1 - p2:+.2f} "
              f"({zstat:+.1f} sigma binomial) -> selection risk {flag}")

    # Primary regression (frozen): y = a + b2*x + gamma*(x1 - x1bar)
    y = np.array([r["y"] for r in rows])
    x = np.log1p(np.array([r["z"] for r in rows]))
    x1 = np.array([r["x1"] for r in rows])
    X = np.column_stack([np.ones_like(x), x, x1 - x1.mean()])
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    a, b2, gam = coef

    rng = np.random.default_rng(SEED)
    bs = []
    for _ in range(N_BOOT):
        i = rng.integers(0, len(y), len(y))
        c, *_ = np.linalg.lstsq(X[i], y[i], rcond=None)
        bs.append(c[1])
    sb2 = float(np.std(bs))

    print(f"\nPRIMARY: y = a + b2*ln(1+z) + gamma*(x1-x1bar), N = {len(y)}")
    print(f"  a  = {a:+.3f}")
    print(f"  b2 = {b2:+.3f} +/- {sb2:.3f}  (bootstrap, {N_BOOT})")
    print(f"  gamma(x1) = {gam:+.3f}")
    print(f"  H(remap) b2=1: {(b2 - 1) / sb2:+.1f} sigma"
          f"   H(null) b2=0: {b2 / sb2:+.1f} sigma")

    # Robustness: no-x1 regression, and x1-trimmed subset |x1|<1
    c2, *_ = np.linalg.lstsq(X[:, :2], y, rcond=None)
    mt = np.abs(x1) < 1.0
    if mt.sum() > 10:
        c3, *_ = np.linalg.lstsq(X[mt][:, :2], y[mt], rcond=None)
        print(f"  robustness: b2(no-x1 term) = {c2[1]:+.3f};"
              f" b2(|x1|<1, N={int(mt.sum())}) = {c3[1]:+.3f}")

    out = {"n_det": n_det, "n_censored": n_cen, "a": float(a),
           "b2": float(b2), "sigma_b2": sb2, "gamma_x1": float(gam),
           "rows": rows, "censored": censored, "seed": SEED}
    rdir = os.path.join(os.path.dirname(__file__), "..", "..", "results")
    os.makedirs(rdir, exist_ok=True)
    with open(os.path.join(rdir, "t4_secondary_max.json"), "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print(f"\nWrote results/t4_secondary_max.json")


if __name__ == "__main__":
    main()
