# Spectral clocks: showing that individual productions ride the same remap

**Session:** 2026-08-20. Answers the author's question: *"How do we show that
individual productions also get shifted by the same apparent Wien
Displacement?"* Producer for all computed numbers:
`src/rawframe/transfer_integral.py` (Hsiao template, real DES griz
throughputs via sncosmo).

---

## 1. By construction: the transfer operator factorizes

The static-model propagation operator acts per photon, multiplicatively in
the (λ, t) plane:

  F_obs(λ_o, t_o) = A(z) · e^{−τ(λ_o/(1+z), z)} · S(λ_o/(1+z), t_o/(1+z))

The achromatic drag supplies the coordinate remap λ_o = (1+z)λ_em (the
apparent Wien displacement) and the wake supplies t_o = (1+z)t_em; the
Kelvin channel supplies only the amplitude weight e^{−τ}. **No factor knows
the emission mechanism.** A nickel line, a cobalt line, the continuum, and
the light-curve envelope are all functions on the same (λ, t) plane and
inherit the identical remap; a line cannot opt out. So "individual
productions shift the same way" is not an extra assumption to defend — it is
a *universality prediction*, and any species-level clock observed to violate
it would falsify the model. The task is to test universality with
observables instruments actually measure well.

(One species note: the SN Ia iron-group chain is ⁵⁶Ni → ⁵⁶Co → ⁵⁶Fe;
cobalt, not copper, is the intermediate — and its 77.2-day half-life is the
best clock in the list below.)

## 2. The author's instrument caution is ratified — quantitatively

The amplitude route (the 341/660 nm ratio) faces a real floor:
single-epoch wide-baseline spectrophotometry carries 5–15% systematics
(differential slit loss, UV throughput falloff), while the predicted signal
is **2.0% at z = 0.25, 3.4% at z = 0.5, 5.4% at z = 1** (verified;
Δτ_∞ = 0.675 − 0.485 = 0.190). Worse, classification pipelines
continuum-warp (spline-divide) spectra before measuring features, absorbing
exactly this tilt into extinction/color — the artifact-by-extraction the
author identified. So the amplitude test is real but must be run on
**unwarped, ensemble-stacked** spectra or space-based (HST/JWST, <1%)
spectrophotometry — it is a campaign, not a lookup. Do not build the
universality case on amplitudes first.

**Amendment (same day — the caution was partly too pessimistic):** the
instrument population splits into two classes. Survey/classification
spectroscopy (Berkeley SNDB ~0.05–0.1 mag across wide baselines; OzDES
relative-only with polynomial warping tied to broadband photometry) cannot
see a 2–5% gradient — as stated. But **dedicated spectrophotometric
datasets can**: HST/STIS quotes ~2% relative within-exposure;
SNIFS/SNfactory delivered true spectrophotometric time series
(3300–9700 Å, e.g. 32 epochs of SN 2011fe, ~percent-level calibration via
SCALA, worse below 4000 Å). Feasibility upgraded from "campaign only" to
"testable statistically on existing dedicated datasets" — with the caveat
that SNfactory lives at z ≈ 0.03–0.08 where the signal is only ~0.5%
(ensemble-level), so the decisive leverage still needs moderate-z
spectrophotometry (HST-class).

**Amendment 2 — the estimator, corrected:** 341/660 nm must NOT be
described as a clean pair of nickel lines. The 3200–3400 Å region is an
iron-group **blend**; ~6600 Å is Si II λ6355 near maximum and a Co/Fe
blend in nebular phases. A single-SN 90-day ratio track mixes the
cosmological transfer with Ni→Co→Fe evolution, ionization changes, and
photospheric recession — too easy to fool ourselves with. The registered
estimator is instead **phase-matched across redshift**: at fixed
rest-frame phases (t = −5, 0, +10, +20 d), form
R(z,t) = F(3200–3400 Å)/F(6200–6800 Å) and normalize by a shape- and
color-matched low-z reference: Q(z,t) = R(z,t)/R(0,t). The model predicts
**Q(z,t) = e^{−Δτ(z)} with Δτ_∞ = 0.197 (effective 330/650 nm):
Q = 0.979 / 0.964 / 0.944 at z = 0.25 / 0.5 / 1.0 — and, critically,
PHASE-FLAT**: τ carries no time dependence, so the suppression is
identical at every epoch. Every astrophysical confound in the list above
varies with phase; phase-flatness is the confound discriminant, and no
calibration tilt naturally produces a phase-independent, λ^{−1/2}-shaped,
z-monotonic suppression.

## 3. Timing and wavelength: what instruments do measure well

Line **centroids** are measured to ~0.01%; **epochs** to fractions of a day.
Five clocks, ordered by availability:

- **T1 — shared centroid redshift (done).** All species in one spectrum
  share a single z to line-centroid precision — our achromaticity test
  already passed this. This is the wavelength half of universality.
- **T2 — whole-spectrum aging (literature, passed).** Blondin et al. 2008
  measured the *rate of spectral feature evolution* in high-z SNe Ia:
  aging slows by exactly (1+z). Every feature's appearance/disappearance is
  a species-level clock, and they all dilate together. Honest register:
  this confirms wake-vs-nothing, not wake-vs-FLRW — both predict (1+z).
- **T3 — the ⁵⁶Co radioactive clock.** Late-time decline slope must appear
  dilated by (1+z) in the observer frame. A nuclear-physics clock attached
  to a specific production; measurable photometrically, no amplitude
  calibration across bands needed (it is a slope in time). **Caution
  (adopted from review):** the textbook 0.98 mag/100 d corresponds to
  complete trapping of the decay energy; the observed optical slope also
  depends on γ-ray escape, positron deposition, ionization, and spectral
  redistribution. T3 must fit a physically parameterized deposition curve
  whose *timescale* is tested for (1+z) scaling — not naively compare raw
  slopes to 0.98/(1+z). T4 is cleaner and runs first.
- **T4 — the secondary-maximum phase (NEW, in-house, preregistered).**
  The i/z-band secondary maximum is an **iron-group recombination clock**
  (Fe III → Fe II recombination plus opacity/flux redistribution; a blend,
  not a single transition — hence the subtype control), sitting at rest phase
  **+25.5 d (i), +26.5 d (z)** in the Hsiao template. The transfer integral
  shows the bump survives in DES griz only to z ≈ 0.3 (it redshifts out of
  the z band beyond), but within that window the discriminant is large:
  at z = 0.3 the wake predicts the bump at ≈ 31.5 observer days
  post-peak, the no-dilation null at ≈ 24.3 — a **7-day separation** at
  DES cadence, measurable in the raw photometry we already hold.
  Registration: `preregistration/secondary_maximum_phase.md`.
- **T5 — Si II velocity gradient.** dv/dt (km/s/day) of the λ6355 feature
  scales as 1/(1+z); centroid-based, amplitude-free.

T1–T5 together demonstrate "individual productions get the same shift"
using only centroids and epochs. The amplitude erosion (§2) is then the
*discriminating* channel: baseline FLRW contains no cosmological λ^{−1/2}
propagation-opacity term (intrinsic SN evolution, host/intergalactic
dust, and calibration effects are the competing chromatic backgrounds),
while the static model's signature is the rigid combination — τ ∝
λ^{−1/2}, monotonic in z, phase-flat at fixed rest wavelengths — with
**no additional parameter fitted to the spectral tests**: the amplitude
τ_∞,B = 0.594 is fixed in advance by the independently fitted
Hubble-diagram curvature. The spectral test does not get to choose its
opacity; that is cross-validation, not a free fit.

## 4. Transfer-integral results (computed through real DES filters)

1. **The "amplitude flattening broadens the light curve" mechanism is
   dead.** With the wake off, the full chromatic erosion + SED shift +
   filter slicing changes the fitted stretch by **≤ 0.0005 (0.05%)** at all
   z ≤ 0.8 in all griz bands — five hundred times too small to mimic the
   measured b = 1. This is the transfer-integral confirmation of the
   registered inverse-injection result (b̂ = 0.0000): a time-independent
   amplitude weight cannot broaden a light curve. **All of b = 1 is
   carried by the time remap (the wake); none by opacity.**
2. **With the wake on, the recovered stretch is (1+z) to ≤ 0.05%** in every
   band — the chromatic reweighting perturbs the shape negligibly, so the
   b = 1 identity of WAKE_FIELD_FORMULATION.md survives the full band
   convolution, achromatically. This is the model's answer to "does the
   flattening + filter sweep account for b ≈ 1?": no — and it doesn't
   need to; the wake does, exactly.
3. **The color artifact is quantified**: chromatic erosion shifts peak
   g−r by +0.010 mag at z = 0.3, +0.024 mag at z = 0.8 — the redward
   drift that SALT's continuum machinery absorbs into c (broadband
   counterpart of the +0.019 mag/z rest-frame prediction; readable only
   through static-BBC, as registered).
4. Secondary-maximum visibility window and phases per band per z: printed
   by the producer; basis of the T4 registration.

## 5. The "Universe A / Universe B" adjudication — already run, outcome 1

An external review proposed generating the same intrinsic SN with **no
time remap** (Universe B: t_e = t_o, λ_o = (1+z)λ_e, τ ∝ λ^{−1/2} path
factor), feeding it through the measured DECam griz throughputs, and
measuring b_apparent — before "inventing a vacuum-memory mechanism." The
record shows this experiment was run **before** the wake was formalized,
twice, pre-registered:

1. **Inverse injection** (registered c8c69cd, run 908e546, 2026-08-19):
   every static-time model — achromatic and chromatic at p = 0.5 and 1.0,
   up to 300× the fitted opacity — recovers **b̂ = 0.0000 exactly**, with
   the structural theorem: a time-independent τ(z, λ) factorizes out of
   every band light curve; width estimators are blind to it.
2. **This transfer integral** (wake-OFF column, §4.1): the full Eq.-(2)
   convolution — Hsiao SED, real DECam system responses, chromatic
   erosion, spectral coordinate shift — moves the fitted stretch by
   ≤ 0.0005 and the per-band **peak epoch by ≤ 0.05 d** at all z ≤ 0.8.

So of the review's three outcomes, the data give the first:
**b_apparent ≈ 0. Filter/SED erosion cannot explain time dilation, and
the independent-photon timing mechanism is genuinely required.** That
null result is *why* the wake exists (WAKE_FIELD_FORMULATION.md); the
chronology is the discipline working as intended — the artifact
hypothesis was tested and killed before the mechanism was built. The
third outcome (b_apparent ≈ 1 from transfer alone) is not merely absent;
it is impossible for any time-independent weight.

The review's one-coefficient unification demand is accepted and is
already the model's structure — a single τ_∞,B = 0.594 with λ^{−1/2}
shape must simultaneously give: **zero** width distortion (measured
≤ 0.05%), **zero** peak-time displacement (≤ 0.05 d), the g−r color
drift (+0.010 mag at z = 0.3), and the phase-flat spectral ratio
Q(z) = 0.979/0.964/0.944 — while the wake alone carries the universal
(1+z) on every timing axis, achromatically. The joint trajectory
[ΔF_peak(λ,z), Δt_peak(λ,z), Δw(λ,z)] is therefore maximally rigid:
amplitude moves, timing does not (beyond the universal remap), with no
per-observable parameters. Remaining honest delta: our width estimator is
matched-rest, not White et al.'s exact pipeline; replicating their
analysis end-to-end on synthetic DES cadence is the first module of
static-BBC.

## 6. Order of execution

1. **T4 now** — uses raw DES photometry already on disk; preregistered.
2. **T3** on well-sampled low-z + literature late-time slopes.
3. **Amplitude campaign** (stacked unwarped spectra; HST/JWST UV) — the
   ΛCDM discriminator, after the universality clocks are banked.
