# Pre-registration: the angular-size–redshift test (scoring EGG-19)

**Registered:** 2026-08-20, before fetching or inspecting any size
catalog. Purpose: convert the D-M fork's angular-size sector from
argument to measurement. This is the counterpart of the Tolman
reduction: Tolman tested the surface-brightness face of d_A; this tests
the angular face directly.

## Hypotheses (shapes, one amplitude each; amplitude is never scored)

For a galaxy population of statistically fixed linear size ℓ:

- **H_A (Euclidean, readings A/A′):** d_A = (c/K)·ln(1+z), so
  **θ(z) = A / ln(1+z)** — monotonically decreasing, no turnover,
  **zero shape freedom** (the no-size-evolution stance is forced by the
  static model's z-invariance claim, so H_A-strict carries no evolution
  parameter).
- **H_B (coasting/Gordon, reading B):** d_A = (c/K)·ln(1+z)/(1+z) —
  turnover at z = e−1 ≈ 1.72; scored both strict (no evolution) and
  with a power-law size evolution (1+z)^{βs}, βs free (the form the
  FLRW literature uses).
- **Reference (ΛCDM, Ωm = 0.33):** d_A^{FLRW}(z), strict and with
  (1+z)^{βs} evolution.

Parameter counts are part of the scoring: H_A-strict has 1 parameter
(amplitude); evolution variants have 2. A model with more parameters
must win by more than the AIC penalty to claim preference.

## The honest framing (registered up front)

Like Tolman, this test discriminates **geometry ⊗ evolution packages**,
not geometry alone. FLRW survives small high-z sizes by fitting βs ≈
−0.75 to −1.5; H_A-strict claims the same data with βs ≡ 0. The
registered question is therefore: *does the raw angular shape θ_med(z)
match 1/ln(1+z) with no evolution freedom, or does it require the
turnover-plus-evolution package?* A naive conversion of published
FLRW-frame evolution results suggests the observed shape may fall
between the two strict shapes — the fit decides, and intermediate
outcomes are reported as measured (no third narrative).

## Data (fetch after this registration; schema-only inspection before running)

1. **Primary (anchor, z ≈ 0.25–3):** van der Wel et al. 2014
   3D-HST/CANDELS structural catalog (public, VizieR J/ApJ/788/28):
   GALFIT effective radii in ANGULAR units (or convertible), F125W/F160W,
   redshifts, stellar masses, flags. Rest-frame ~5000 Å sizes via the
   catalog's prescription.
2. **Extension (z ≈ 3–8, if a public catalog is fetchable):** a JWST
   NIRCam structural catalog (CEERS/JADES-class) with angular R_e and z.
   If none is cleanly fetchable, the extension bin is dropped and the
   test runs on the primary range — where the strict shapes already
   differ by a factor ≈ 1.4 in θ(z=1)/θ(z=3).
3. All size measurements are used in **angular units in the observer
   frame** — the catalogs' own kpc conversions (FLRW-baked) are never
   used.

## Estimator (frozen)

1. Subsamples: the catalog's quiescent/early-type and star-forming
   classes, separately (both reported — anti-cherry-pick).
2. Selection: the catalog's own stated mass-completeness limits define
   the sample per z-bin. (Stellar masses carry FLRW-frame contamination
   through luminosity distances; this is disclosed as the test's
   residual frame-dependence, and a robustness variant selects instead
   on observed flux at fixed rest wavelength.)
3. Statistic: median angular effective radius θ_med in pre-set z bins
   (Δz = 0.25 below z = 1, Δz = 0.5 above), bootstrap errors.
4. Fits: each hypothesis's shape, one free amplitude (plus βs where
   declared), χ² over bins; report χ², AIC, and the shape residuals.
5. Systematics band: surface-brightness incompleteness assessed by
   re-running with the faintest quartile of each bin removed; K-band
   morphological drift noted; AGN/point-source flags applied.

## Kill conditions (pre-committed)

- **K1-ang:** if H_A-strict loses to (ΛCDM or coasting) + evolution by
  ΔAIC > 10 with the systematics band applied, the Euclidean
  no-evolution claim fails: the angular sector's "naturalness" advantage
  is dead, and with Tolman already adverse, reading A/A′ loses its last
  empirical asset. Recorded as such.
- **K2-ang:** if H_A-strict is competitive or better (ΔAIC ≤ 4 against
  all evolution variants), EGG-19 scores FOR Euclidean angles: a
  one-parameter shape matching data that the alternatives fit only with
  evolution freedom. Recorded as a genuine discriminant in the D-M
  ledger.
- Intermediate: reported as measured; feeds the D-M ruling as a
  weighted, not decisive, entry.
- **No-freedom clause:** bins, subsamples, shapes, and the AIC rule are
  frozen now; any forced deviation (e.g., catalog schema surprises) is
  a documented amendment labeled pre/post-data.

## Relation to the standing docket

This test scores the angular face of D-M; the Tolman K2 dataset scores
the surface-brightness face; Dovekie scored the flux face (robust). The
D-M ruling should wait for at least this test's result, since it is the
Euclidean reading's principal remaining empirical asset.
