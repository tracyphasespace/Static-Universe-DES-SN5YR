# Pre-registration: CANDELS/3D-HST Tolman test (K2) — K-correction-free by design

**Registered:** 2026-08-20, BEFORE any surface-brightness statistic is
computed from the joined catalog. Blindness state disclosed exactly: the
angular-size test already published bin medians of r and used magnitudes
for faint-quartile cuts; **the SB combination μ = mag + 2.5·log(2πr²q)
and any z-trend of it have never been formed or inspected.**

## Why this is K2

The L&S verdict rests on a band spread carried by one cluster under a
1.89-mag K-correction that L&S Paper III documents as an
**evolution-adjusted Bruzual–Charlot template fit color-matched to
observed colors** — an FLRW-prior-laden SED extrapolation across the
Balmer break. This test removes that layer by construction: mean SB
inside the half-light ellipse in **angular units**
(μ̄_e = mag + 2.5·log₁₀(2π r² q), conventions constant so only the
z-trend matters), with rest wavelength pinned by the same band-per-z
windows as the angular test (rest ≈ 4800–6700 Å) — no distances, no
template SED transfer, only a small within-window rest-λ drift carried
as a systematic. Same early-type standard-rod subsample (Sérsic
n ≥ 2.5, logM ≥ 10.3, N = 628), same fields, same quality cuts.

## Estimator (frozen)

1. Per galaxy: μ̄_e = mag(F) + 2.5·log₁₀(2·π·r²·q), r in arcsec, band F
   per the registered z-windows (Y/J/H).
2. Registered bins (same four as the angular test): median μ̄_e,
   bootstrap errors (500, seed 20260820).
3. Fit μ̄_med(z) = μ₀ + 2.5·n_meas·log₁₀(1+z): **n_meas with error is
   the result.** Late-type subsample reported alongside
   (anti-cherry-pick), interpreted with the same geometry-blind caveat
   as the angular test.
4. Robustness (frozen): (a) faintest-quartile removal; (b) narrow mass
   slice 10.3 ≤ logM < 10.8; (c) Kormendy-adjusted variant (μ̄ regressed
   on log θ within bins, evaluated at the sample-median θ) to control
   SB–size population drift.
5. **In-sample band-spread test (the L&S-artifact discriminator):**
   repeat n_meas on a BLUE rest-λ ladder (windows shifted so Y/J/H pin
   rest ≈ 4300–4900 Å; requires extending the catalog join above
   z = 2.2 — a plumbing amendment, hypothesis-neutral). Statistic:
   **S = n(red ladder) − n(blue ladder).** If the L&S I−R spread
   (+0.78 ± 0.21 over ~1500 Å) is real propagation/astrophysics, a
   crude linear extrapolation predicts S ≈ +0.6 ± 0.3 here; if it is a
   2001 template artifact, S ≈ 0. The model predicts S ≈ −0.03.

## Predictions (Branch Z, zero evolution; opacity at matched rest-λ ≈ 0.2)

| reading | n_pred (Branch Z) | n_pred (Branch E, committed ΔM_R = 0.40z) |
|---|---|---|
| A: truly static (no rate factor — continuity theorem) | **≈ 1.2** | ≈ 0.7 |
| A′: energy + rate | **≈ 2.2** | ≈ 1.7 |
| coasting / ΛCDM (expanding) | **≈ 4.0** | ≈ 3.5 |

Forecast precision: with N = 628, per-bin σ_med ≈ 0.06 mag and a
0.55-mag lever arm, σ(n_meas) ≈ 0.10–0.15 — adjacent readings separated
by ≥ 5σ. This test CAN pick a reading.

## Kill conditions (pre-committed)

- **K2-T-select:** if n_meas lies within 3σ of exactly one reading's
  band (Z or its committed-E variant) and > 3σ from the others, that
  reading is empirically selected for the D-M ruling; the others'
  Tolman faces are killed. This applies with full symmetry — n_meas ≈ 4
  selects the expanding reading and kills both static readings' Tolman
  face outright.
- **K2-S (spread):** S consistent with 0 (|S| < 0.2) ⇒ the L&S band
  spread is adjudicated a template/systematic artifact of the 2001
  design; the original K1 verdict's driving discrepancy is retired and
  the Tolman ledger row is re-scored on this dataset. S ≈ +0.6 ⇒ the
  spread is real, the model has no chromatic account of it (anti-Kelvin
  slope), and the spread becomes a standing kill regardless of reading.
- Intermediate outcomes reported as measured; no third narrative.
- **No-freedom clause:** bins, windows, cuts, statistics, and both
  ladders frozen now; deviations are documented amendments labeled
  pre/post-data.

## Registered relation to the record

This is the K2 anticipated by `tolman_static_reanalysis.md` and the
"cleaner move" proposed in external review: same instrument family as
the executed angular-size test, same subsample, the K-correction
confound removed by design rather than modeled. Execution on the
author's GO.
