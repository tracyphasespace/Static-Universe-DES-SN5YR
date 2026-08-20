# d_A(z), duality, Tolman, color, and the energy ledger — derived, with the bad news stated first

**Session:** 2026-08-20. Executes the referee-response proof program (items
3–6 of the order of battle). Consumes: the two-channel canon, the wake
(b = 1), the corrected opacity convention (referee Issue 6:
Δm = (2.5/ln10)τ, so the fitted η = 0.297 corresponds to a physical
**τ_∞ = 0.594** at rest-B — this resolves docket D-6's convention question
in the 2.5/ln10 direction for the physical reading).

**Executive summary.** d_A = D is *derived*, not assumed — the model
violates Etherington duality by exactly one factor of (1+z), which is its
geometric signature. The resulting Tolman prediction n_eff ≈ 2.2 is in
**9σ tension with Lubin & Sandage's I-band measurement** under the model's
own no-evolution constraint; this is now the thesis's gravest standing
threat and goes into Draft 6 as such, with the one legitimate completion
(a static-frame end-to-end Tolman reanalysis) named. The color test is
computed and turns out to be selection-dominated (predicted +0.019 mag/z
vs raw −0.096 mag/z, both frameworks needing a selection model to read
it). The energy ledger closes only through the prompt-frequency-cascade
mechanism and the D-K gates.

---

## 1. The angular-diameter distance: d_A = D, derived

Premises, all already canon:
1. Spatial geometry static and Euclidean.
2. The forward channel is strictly forward — no angular deflection
   (EGG-33's no-blur budget, θ_rms < 10⁻¹² rad, is a *requirement* of the
   channel, independently constrained by image sharpness).
3. The wake modifies the corridor's phase velocity *longitudinally and
   homogeneously* across the beam; with no transverse index gradient
   (beam edges at parsec scales), rays do not bend.
4. Propagation is dispersionless (the ξ = 0 topological protection).

Under 1–4, light from a source of physical extent ℓ at path distance D
reaches the observer along straight lines: **θ = ℓ/D exactly**, hence

  **d_A(z) = D(z) = (c/K)·ln(1+z).**

There is no escape through the wake: corridor conditioning is a
time-dependence, not a refractive gradient, and cannot magnify solid
angles. The v8.5-era code's import of FLRW reciprocity
(d_A = D/(1+z)) was unjustified — Etherington's theorem is a statement
about null geodesics of a metric with photon conservation, and a
non-metric propagation law is not bound by it. **Docket D-M resolves:
d_A = D** (pending author ratification, since it retires the old code's
claim and fixes EGG-19's exponent).

**Duality signature.** With d_L = (1+z)·D (energy + arrival-rate factors):

  **d_L / d_A = (1+z)** — not FLRW's (1+z)².

One clean, falsifiable, model-defining statement: any measurement of the
duality ratio at the (1+z)-vs-(1+z)² level discriminates the frameworks.

## 2. Tolman surface brightness — the confrontation, honestly

Bolometric surface brightness of a resolved thermal source:
SB ∝ F/θ² ∝ (1+z)^(−2)·e^(−τ(z,λ)). The effective Tolman exponent is

  n_eff(z, λ) = 2 + (τ_∞,λ / 2)·(1+z)^(−1/2),  τ_∞,λ = 0.594·(440nm/λ)^(1/2).

Computed at z = 0.5: **n_eff = 2.24 (rest-B), 2.20 (rest-R), 2.18
(rest-I)** — weakly chromatic, and *decreasing* redward.

Measured (Lubin & Sandage 2001, Paper IV, AJ 122, 1084; three clusters at
z = 0.76, 0.90, 0.92 — 34 early-type galaxies):
**n_R = 2.59 ± 0.17, n_I = 3.37 ± 0.13** (q₀ = 1/2 frame).

Confrontation, with the eternal universe's own hands tied: the model
*predicts z-invariance of the galaxy population* (no cosmic clock → no
luminosity evolution), so the evolution escape valve that ΛCDM uses to
bridge its geometric 4 down to the measured 2.6–3.4 is **not available**
to this model. At face value:

- rest-R: 2.3σ tension — uncomfortable, survivable.
- rest-I: **9.2σ — excluded at face value.**
- Worse, the *sign* of the model's chromatic trend is wrong: it predicts
  n_I slightly BELOW n_R; the measurement has n_I − n_R = 0.78 ± 0.21
  above it.

What keeps this a live confrontation rather than a closed verdict, stated
without special pleading:
1. The measurement's internal R–I spread (0.78 ± 0.21, 3.6σ under *any*
   single-exponent law) signals band-dependent systematics or genuinely
   band-dependent astrophysics in the measurement itself — under ΛCDM it
   is absorbed as band-dependent evolution, which is exactly the degree
   of freedom the static model forfeits.
2. The L&S analysis is performed end-to-end in the FLRW frame: angular
   apertures, K-corrections, and selection are all computed with
   expanding-frame distances. The legitimate completion — before the
   verdict is executed — is a **static-frame Tolman reanalysis**: same
   photometry, apertures and K-corrections recomputed with d_A = D and
   the two-channel transfer. That instrument is hereby named; it is the
   Tolman analogue of the static-frame BBC rerun.
3. Additional, independent SB datasets (Sandage 2010; deep-survey
   photometric SB profiles; JWST counts per EGG-19) should enter the
   same comparison — one measurement pair should not carry a verdict of
   this size alone.

**Register:** the Tolman test is the thesis's most serious standing
challenge. Draft 6 must present the prediction, the face-value exclusion,
and the named reanalysis — in that order, without softening.

**Addendum (same day, later):** the frame-shift analysis
(`preregistration/tolman_static_reanalysis.md`, producer
`src/rawframe/tolman_frame_shift.py`) calibrates dn/dlog d_A from L&S's own
published q₀ grid (n varies 2.28→2.81 in R, 3.06→3.55 in I between q₀ = 0
and 1; linear to ≤0.011). Extrapolated to the static frame (+0.335 dex in
d_A): **n_I → 2.30 ± 0.13 (+1.1σ vs prediction), n_R → 1.45 ± 0.17
(−4.3σ)**. The face-value 9.2σ is an EdS-frame artifact; the constraint
migrates to R-band, and the **frame-invariant** discrepancy is the band
spread n_I − n_R = 0.78 ± 0.21 vs predicted −0.02 (3.7σ in any frame).
Kill conditions pre-committed in the registration before any data reduction.

**Correction (2026-08-20, later):** this document's claim that "the
eternal universe forbids luminosity evolution — the escape valve is not
available" was too strong. Static geometry has finite lookback
t_lb = K⁻¹ln(1+z); evolution is forbidden only under strict ensemble
stationarity. See WAKE_CONSISTENCY.md §5 (the stationarity fork) and the
Tolman registration's pre-reduction Amendment 1 (Branch Z / Branch E).

## 3. Secondary geometric discriminator: the angular-size–redshift relation

With θ ∝ 1/D = K/(c·ln(1+z)), apparent sizes decrease monotonically for
all z. FLRW predicts a minimum near z ≈ 1.6 with θ *increasing* beyond.
A robust standard-rod population at z > 1.5 (compact radio sources,
BAO-scale features read as angles, strong-lens image separations)
discriminates directly. Historical compact-source data (Kellermann 1993;
Gurvits et al.) are ambiguous; modern samples deserve the comparison.
Listed as the second geometric test; not yet computed against data.

## 4. Radiance normalization (the referee's blackbody point, conceded and quantified)

A source redshifted by frequency scaling has Planck *shape* at
T/(1+z) but radiance (1+z)² **brighter** than a true blackbody at that
temperature (FLRW preserves exact Planckness; the static model does not).
Computed excess: 0.21 mag at z = 0.1, 0.57 mag at z = 0.3, 0.88 mag at
z = 0.5. Consequences:
- **Wien displacement statements are hereby rescoped** to
  spectral-coordinate mapping only (per the referee); no claim of full
  blackbody normalization survives.
- **Testable via the expanding-photosphere method**: EPM assumes
  blackbody normalization; the static model predicts EPM distances
  skewed by (1+z) relative to other indicators — ~10% at z = 0.1
  (inside current EPM scatter), ~30% at z = 0.3. EPM on SNe II at
  z ≳ 0.2 is a live discriminator; current samples sit mostly below it.
- The CMB is exempt *only* under the equilibrium reading (generated in
  equilibrium, not redshifted from a surface) — an exemption that itself
  stands or falls with the D-K gates.

## 5. The color law — computed, and selection-dominated

With τ_λ ∝ λ^(−1/2) (rest frame; R_V ≈ 8.5), the predicted mean SALT-c
drift is E(B−V)(z) = +0.007 at z = 0.25, +0.0125 at z = 0.5, +0.020 at
z = 1 — slope **+0.019 mag/z, redward**.

Measured raw DES c(z) slope (1,635 DES-subset SNe, producer
`src/rawframe/da_tolman.py`):
**−0.0963 ± 0.0140 mag/z — blueward, 8σ from the prediction in the raw
data.** Stated honestly and symmetrically: the raw trend is
selection-dominated in *both* frameworks (Malmquist selects blue at high
z at exactly this magnitude; ΛCDM attributes the raw slope to selection
via its BBC simulations). The predicted signal is 5× smaller than the
selection effect, so this test **cannot be read without a selection
model** — it folds into the static-frame selection instrument
(static-BBC), which is now load-bearing for *three* tests (Hubble
verdict, color law, population z-invariance). Harder than the referee
implied, and said so.

## 6. The energy ledger

With τ_∞ = 0.594: beam fraction removed = 10.3% at z = 0.5, **16.0% at
z = 1** (the referee's "quarter or more" overstated it; 16% is still an
unpayable debt without a destination). The model's destination chain:

1. **No optical halos, by mechanism not by fiat**: the non-forward
   channel deposits the photon's energy into soft filament modes — the
   scattered quantum leaves the optical band *promptly* (frequency
   cascade), so there is no optical photon at small angle to form a PSF
   wing, and no optical EBL excess. This converts the referee's halo/EBL
   objection into a sharp prediction: **zero redshift-correlated PSF
   wings (EGG-33) and no optical EBL contribution — the removed energy
   reappears only in the microwave bath.** The prompt-cascade rate is an
   owed microphysical number (it must beat the re-scatter rate).
2. **The equilibrium budget**: injection from starlight scattering is
   ~7×10⁻³³ erg cm⁻³ s⁻¹ against u_CMB/t_H ~ 10⁻³⁰ — starlight cannot
   *maintain* the CMB on Hubble timescales. In the eternal-equilibrium
   framing no maintenance is required (equilibrium decays only through
   its loss channel — BH absorption — which must be correspondingly
   slow); the quantitative closure is exactly D-K's three gates
   (equilibrium theorem, FIRAS μ rate-ratio, anisotropy). The ledger is
   consistent *only if* those gates pass; they remain the debt.

## 7. Status board after this derivation

| observable | model prediction | status |
|---|---|---|
| redshift achromaticity | exact | data-validated (lines) |
| b = 1 timing | wake, coefficient 1 | derived; vertex microphysics owed; unique steady-source prediction |
| Hubble diagram | Δχ² = +1.1 | done, CI-locked |
| duality ratio | (1+z) | derived; clean discriminator |
| Tolman n_eff | ≈ 2.2, weakly chromatic | **9σ face-value tension (I-band)**; static-frame reanalysis named |
| angular sizes | θ monotone ∝ 1/ln(1+z) | derived; not yet confronted |
| radiance norm. | (1+z)² excess | derived; EPM z ≳ 0.2 discriminator |
| color law | +0.019 mag/z redward | computed; selection-dominated, needs static-BBC |
| energy ledger | prompt cascade, no optical halos | prediction stated; D-K gates owed |

The thesis now owes, in order: the static-frame Tolman reanalysis (or it
dies on L&S I-band), the static-BBC selection instrument (three tests
blocked on it), the vertex phase-continuity proof, and the D-K gates.
