# T4 run report: secondary-maximum phase test (DES raw i/z)

**Run:** 2026-08-20. Pipeline: `src/rawframe/secondary_max_test.py`;
registration: `preregistration/secondary_maximum_phase.md` (Amendments 1–3).
Results JSON: `results/t4_secondary_max.json` (untracked, regenerable).

## Verdict

**INCONCLUSIVE. b₂ = +0.52 ± 0.78 (N = 120).** Consistent with the
universal remap (b₂ = 1, at −0.6σ) and with the no-dilation null
(b₂ = 0, at +0.7σ). Neither kill condition fires. Per the registered
no-third-reading rule this is reported as an uninformative measurement,
not as evidence for a mixture: the estimator worked, the data lack the
power.

- Detections 120 / censored 22 of 189 eligible (z ∈ [0.05, 0.30],
  IDSURVEY 10, PROBCC < 0.1, x1 present).
- **Detection-efficiency test: PASSED** — detection fraction 0.92 (low-z)
  vs 0.84 (high-z), difference +0.8σ binomial → no detection-conditioned
  selection flag.
- Intercept a = −0.09 (the template-phase nuisance, as designed);
  γ(x1) = +0.07.
- Robustness (frozen): b₂ = +0.60 without the x1 term; +0.73 on |x1| < 1.
- **Post-hoc, labeled:** inverse-variance-weighted regression (weights
  from the frozen per-SN σ(t₂), analysis chosen after unblinding):
  b₂ = 1.15 ± 0.87. Same conclusion: no discrimination.

## Why the forecast power was wrong

The registration forecast σ(b₂) ≈ 0.05–0.10 assuming ~2 d per-SN timing
error. Realized: **median σ(t₂) = 5.3 d** (55% of detections above 5 d)
and per-SN scatter sd(y) = 0.32 ln units ≈ 8 d equivalent — a
combination of DES ~7 d cadence in a 35 d window and genuine intrinsic
secondary-maximum diversity (the subtype effect flagged as C-e; DES
metadata carries no subtype column, so stratification was not
executable). With the z ≤ 0.30 lever arm (forced by the bump redshifting
out of griz — model visibility: desi to z ≈ 0.16, desz to z ≈ 0.32),
reaching a 3σ 0-vs-1 discrimination needs σ(b₂) ≈ 0.15, i.e. ~25× the
effective statistics. **DES griz alone cannot decide T4.**

## Amendment and defect trail (full disclosure)

- **Amendment 2 (pre-data):** intercept, frozen GP peak finder,
  censoring, detection-efficiency test, per-SN band averaging — from
  external review, before any measurement.
- **Amendment 3 (post-data, disclosed):** LOO 5σ epoch screening, after
  the first frozen run returned 1/189 detections and diagnosis found
  single-epoch difference-imaging artifacts hijacking t_peak (CID
  1280240: +26.6 d epoch at 3× peak flux; the raw table bypasses the
  release PHOTFLAG cuts). Chosen from the failure mode, not from any b₂
  (none existed — quality floor had voided the regression).
- **Three implementation bugs fixed during bring-up** (all with the
  quality floor still voiding any b₂, so no result-steering was
  possible): (1) single-pass LOO let the artifact condemn its genuine
  neighbor → greedy iterative form; (2) zero-mean GP prior on
  uncentered flux sagged between epochs → weighted-mean centering;
  (3) absolute Cholesky jitter (10⁻¹²) exceeded the kernel amplitude of
  Jy-scale fluxes (~10⁻¹⁴), collapsing the GP to the mean and making
  posterior draws pure noise → per-curve normalization to O(1).

## What survives, and the path

T4's *design* is validated: the finder detects the bump in 85% of
eligible light curves with no z-dependent selection, the intercept
absorbed the template normalization, and the model-referenced Δt_model
handled rest-band drift. What fails is the arithmetic of lever arm ×
per-object noise. Instruments that fix exactly that:

1. **Rest-NIR samples at higher z** — HST RAISIN-class data (rest-NIR
   light curves at z ≈ 0.2–0.6) double the lever arm where the bump is
   strong; CSP low-z NIR anchors the reference.
2. **LSST** — deeper griz+y, denser cadence: y-band extends bump
   visibility beyond z 0.3 and per-SN σ(t₂) shrinks with cadence.
3. Ensemble/stacked composite light curves in narrow z bins (would need
   a new registration; per-SN regression is then replaced by a
   population statistic with its own selection accounting).

T2 (Blondin spectral aging) therefore remains the strongest existing
species-clock universality evidence; T4 on DES griz is banked as an
executed, honestly-powered null instrument with a validated design.
