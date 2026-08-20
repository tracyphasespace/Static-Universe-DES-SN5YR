# Pre-registration: secondary-maximum phase as a species clock (DES raw i/z)

**Registered:** 2026-08-20, before any measurement on data.
**Amended:** 2026-08-20 (same day, still pre-data) per external review:
estimator corrected to log–log form, feature-search window made
hypothesis-neutral, subtype stratification added, clock renamed. No DES
measurement has been inspected.
**Model producer:** `src/rawframe/transfer_integral.py` (Hsiao + real DES
throughputs). **Companion:** SPECTRAL_CLOCKS.md §3–4 (test T4).

## Claim

The i/z-band secondary maximum (an **iron-group recombination clock** —
driven by Fe III → Fe II recombination and the resulting opacity/flux
redistribution, with blended Fe II emission near 7500 Å an identified
contributor; not a single atomic transition — at rest phase ≈ +25.5 d in
i, +26.5 d in z in the Hsiao template)
rides the same (1+z) time remap as the primary light-curve envelope. In DES
raw photometry at z ≤ 0.3 (the visibility window — the bump redshifts out
of griz beyond), the observer-frame separation Δt = t₂ − t_peak satisfies

  Δt_obs(z) = (1+z) · Δt_model(z, band)

where Δt_model(z, band) is the transfer-integral prediction *at that z and
band* (this already contains the rest-coverage drift of the bump within the
filter — comparing to a fixed rest number is NOT valid; the model value at
z = 0.3 in desz is 24.25 d rest, i.e. 31.5 d observer).

**Null (no dilation of species clocks):** Δt_obs = Δt_model — undilated.
At z = 0.3 the hypotheses differ by ≈ 7 observer days, large against DES
~7-day cadence with multi-epoch spline fitting across many SNe.

## Estimator

1. Sample: spectroscopically/photometrically confirmed Ia
   (PROBCC_BEAMS < 0.1), z ≤ 0.3, tier-1 coherent light curves, ≥ 3 epochs
   in the window +15 to +45 observer days post-peak in i or z.
2. Per SN per band: spline/GP fit of raw flux; t_peak and t₂ = first local
   maximum in the **hypothesis-neutral observer-frame window
   +10 d < t_o − t_peak < +45 d** (the union of both hypotheses' predicted
   ranges over z ≤ 0.3: null ≈ 24–27 d, wake ≈ 25–33 d, with margin;
   neither hypothesis informs the search domain); Δt = t₂ − t_peak.
3. Regression (log–log, corrected pre-data):
   **ln[Δt_obs / Δt_model(z, band)] = b₂ · ln(1+z).**
   Wake/FLRW prediction b₂ = 1; no-dilation null b₂ = 0. (The previously
   written "slope through origin vs (1+z)" form was mathematically
   inconsistent with the b₂ = 0 null — under no dilation the ratio is
   constant at 1, which that form does not map to slope 0. Corrected
   before any measurement.)

## Confound controls (committed)

- **C-a Intrinsic stretch:** secondary-max phase correlates with luminosity
  and x1 (brighter-slower → later bump). Control: regress out SALT x1, or
  compare x1-matched subsamples across z bins. Report both.
- **C-b Rest-coverage drift:** handled by construction — the comparison is
  to Δt_model(z, band), never to a fixed rest phase.
- **C-c Selection:** high-z sub-sample is intrinsically brighter/slower
  (Malmquist), pushing later rest bumps at high z — degenerate with
  dilation sign. The x1-matching of C-a is the control; report the
  unmatched result too, labeled.
- **C-d Template dependence:** Hsiao bump phases carry ~1–2 d template
  uncertainty; enters Δt_model as a common-mode systematic, largely
  cancelling in the z-trend. Report sensitivity by recomputing Δt_model
  with SALT3-NIR if available.
- **C-e Spectroscopic subtype:** the secondary maximum shows substantial
  intrinsic diversity between SN Ia subclasses (iron-recombination
  physics varies by subtype). Where sample size permits, match or
  stratify by spectroscopic subtype in addition to x1; report stratified
  and pooled results.

## Amendment 2 (2026-08-20, pre-data — only the photometry table's schema/
## column names had been inspected when this was written; no light-curve
## measurement had been made)

1. **Intercept added (statistical correction from external review).**
   Primary regression:
   **y = a + b₂·x + γ·(x1 − x̄1)**, with y = ln(Δt_obs/Δt_model),
   x = ln(1+z). The intercept a is free under BOTH hypotheses: it absorbs
   the common-mode template-phase normalization error (~1–2 d, C-d) so it
   cannot masquerade as dilation over the short z ≤ 0.3 lever arm. C-d's
   "cancels in the z-trend" is true only WITH the intercept. The
   x1-MATCHED comparison of C-a is demoted to robustness check; the
   regression on all usable SNe is primary.
2. **Peak finder frozen.** Gaussian-process regression, Matérn-3/2
   kernel, length scale fixed at 10 observer days (hypothesis-neutral,
   identical for all SNe), signal variance = sample variance of the
   band's flux, noise = reported per-epoch errors (valid_err rows only);
   posterior mean evaluated on a 0.25 d grid. t_peak = global maximum of
   the posterior mean, required ≥ 5 d interior to the observed span.
   t₂ = FIRST local maximum of the posterior mean in the neutral window
   (t_peak+10, t_peak+45) with prominence ≥ 1× the median epoch flux
   error in that window. σ(t₂) = standard deviation of t₂ over 64 GP
   posterior draws (seed 20260820); draws with no qualifying peak are
   dropped from the σ computation but if > 32 draws fail, the detection
   is voided (censored).
3. **Non-detections**: logged as censored, excluded from the primary
   fit. Predefined detection-efficiency test: detection fraction and
   mean x1 / median SNR compared between z bins [0.05, 0.15) and
   [0.15, 0.30]; a binomial-test difference in detection fraction at
   > 2σ flags detection-conditioned selection in the report.
4. **i/z correlation**: per-SN y = unweighted mean over the SN's valid
   band detections — one point per SN in the regression.
5. **Quality cuts (frozen)**: IDSURVEY = 10; PROBCC_BEAMS < 0.1;
   0.05 ≤ z ≤ 0.30; x1 present; band ∈ {i, z} with the model bump
   visible at that z (Δt_model finite from the producer); ≥ 5 valid
   epochs in the band; ≥ 3 valid epochs in (t_peak+15, t_peak+45);
   ≥ 1 epoch within 7 d of t_peak.
6. **Uncertainty on b₂**: bootstrap over SNe, 2000 resamples,
   seed 20260820.

## Amendment 3 (2026-08-20, POST-DATA — disclosed)

The frozen pipeline's first run returned 1 detection / 148 censored of
189 eligible, and diagnosis on censored objects found the cause: the raw
photometry (which deliberately bypasses the release pipeline's PHOTFLAG
epoch quality cuts) contains single-epoch difference-imaging artifacts
with small reported errors. Example, CID 1280240 (z = 0.060): the z-band
epoch at +26.6 d reads 3× peak flux at SNR ≈ 40; the error-weighted GP
places the global maximum on the artifact, mis-identifying t_peak and
sliding the search window onto the monotone tail — while the true
secondary bump IS present in the surrounding epochs (+19.7 → +30.5 d
rise at SNR ≈ 100). This is a data-integrity defect interacting with the
finder, not an estimator-sensitivity issue.

**Fix (as narrow as possible, hypothesis- and z-blind, identical for all
SNe):** leave-one-out epoch screening before the GP stage — for each
epoch, fit the frozen GP to the remaining epochs, predict at the held-out
time, and reject the epoch if its standardized LOO residual
|f − μ_LOO| / √(σ² + σ²_LOO) > 5. Single pass. Nothing else changes:
kernel, length scale, prominence rule, window, censoring, regression,
seeds all as in Amendment 2.

Evidentiary note: this amendment was written AFTER data inspection, in
response to a discovered artifact class, and its cost is disclosed
rather than hidden. The trigger (t_peak hijacking by > 5σ single-epoch
outliers) and the fix threshold were chosen from the diagnosed failure
mode, not from any b₂ value — no regression result existed at decision
time (the quality floor had voided it, N = 1).

## Kill conditions

- **K1:** b₂ consistent with 0 and excluding 1 at > 3σ (after the
  predefined controls) → this species clock does NOT dilate → the
  single-remap universality prediction is killed for the static model,
  and — *provided the secondary-maximum population and measurement
  systematics have actually been controlled* — it stands in strong
  conflict with universal metric dilation as well (White's envelope
  b = 1.003 ± 0.005 would then disagree with an internal clock).
- **K2:** b₂ = 1 within errors → "individual productions ride the same
  remap" is demonstrated with DES's own raw data; T4 is banked and cited in
  Draft 6.
- **No third reading:** an intermediate b₂ (e.g. 0.5 ± 0.1) is reported as
  a failure of the universality prediction, not reinterpreted.

## Magnitudes expected

Window z ∈ [0.05, 0.3]: lever arm in (1+z) is only 1.05–1.30, but the
clock is ~25 d long, so the dilation signal is 1.3–7.5 observer days —
resolvable by ensemble. Forecast before running: with N ≈ 100–300 usable
low-z Ia and per-SN t₂ precision ~2 d, σ(b₂) ≈ 0.05–0.10.
