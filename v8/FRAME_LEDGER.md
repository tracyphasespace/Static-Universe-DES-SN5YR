# The Frame Ledger — assumption-tagging standard for this campaign

**Adopted:** 2026-08-20. Motivation: the βs = −1.00 identity (the FLRW
literature's "size evolution" turned out to be the frame-conversion
factor to two decimals) and the L&S K-correction finding (evolution
templates color-matched to observed colors) both show that cosmological
priors enter analyses as *nouns and default units*, not as stated
premises. This standard makes the frame of every quantity explicit and
lintable. Enforced by `src/rawframe/frame_lint.py`; adopt into repo CI
alongside the numeric manifest checks.

## 1. Frame-free observables (no tag required)

Angular sizes and separations (arcsec); observed fluxes and magnitudes
in named observed bandpasses; measured redshifts (wavelength ratios);
arrival times and cadences (MJD); line centroids and line ratios at
stated observed wavelengths; Petrosian η and other flux-ratio radii;
axis ratios, Sérsic indices, position angles from angular fits; counts
per solid angle per observed-flux bin.

## 2. Frame-valued quantities (tag mandatory)

Anything in kpc, Mpc, L☉, M☉, Gyr, SFR, comoving volume; any
"rest-frame band X" magnitude produced through a template K-correction;
any luminosity or absolute magnitude; any age or epoch; any selection
threshold defined in a frame-valued unit (e.g., a stellar-mass cut).

**Tag syntax** (inline, next to first use in any analysis doc):
`[frame: FLRW-Om0.3]`, `[frame: static-ln(1+z)]`, `[frame: coasting]`,
`[frame: template-BC96-evolved]`, `[frame: mixed — see note]`.
A derived quantity inherits the union of its inputs' tags. A quantity
whose tag would be "mixed" with an FLRW component may not be used to
*discriminate* frames — only within-frame or with the contamination
bounded.

## 3. Banned vocabulary in analysis text (each asserts t = t(z) under FLRW)

"early universe", "young galaxy" (as a z-statement), "evolved system",
"progenitor of", "epoch of", "lookback time" (untagged), "the universe
was N Gyr old", "still forming", "had not yet grown".
Replacements: "at z = …", "in the higher-z sample", "the z-trend of
parameter P", "under [frame] this corresponds to t = …". The word
"evolution" is permitted only as a *named fit parameter with a frame
tag* (e.g., "βs [frame: FLRW]"), never as an unqualified fact.

## 4. Known frame leaks in this campaign's own inputs (standing register)

- **τ∞,B = 0.594** (the Kelvin normalization): fitted on the released
  DES MU vector, which carries the BBC correction layer
  [frame: FLRW-sim-conditioned; leverage measured: L_BBC = −11.7 (v1.2),
  −2.4 (Dovekie)]. Every prediction using τ∞ inherits this tag until a
  raw-photometry refit exists.
- **Skelton stellar masses** (logM cuts): FAST fits using FLRW d_L
  [frame: FLRW]. Flux-selected robustness variants required wherever a
  mass cut gates a frame-discriminating result.
- **L&S K-corrected ⟨SB⟩**: [frame: template-BC96-evolved,
  color-matched] — documented in Paper III's own text.
- **L&S Paper I local zero points**: the ⟨z⟩ = 0.037 → z = 0 correction
  assumed n = 4 [frame: FLRW]; under n ≈ 2.2 the correction halves →
  ~0.07 mag common-mode systematic in every ΔSB (Δn ≈ 0.1).
- **Branch-E evolution priors**: FP M/L rates measured with FLRW d_L
  [frame: FLRW]; adopted as empirical z-scalings — first-order
  frame-agnostic, tag retained.
- **Photometric redshifts** (zpk): template-fitted; nearly frame-free
  (wavelength ratios) but template-age priors can shift tails
  [frame: weak-template].

## 5. The invariants program (the productive direction)

Quantities algebraically invariant under the frame change cannot be
argued with in either vocabulary. Current inventory: the Tolman band
spread (invariant under d_A reassignment and gray evolution); the
Etherington ratio d_L/d_A; the βs = −1.00 identity (an invariance
*violation* detector — it exposed a frame conversion posing as an
observable); line-redshift concordance across bands; the K2-S
band-spread statistic on rest-matched angular data. Finding more
invariants outranks running more frame-valued fits.


## 6. Standing rule: forecast honesty (adopted 2026-08-20)

Three consecutive ~10x optimistic power forecasts (T4, K2-SB, σ(b₂))
shared a cause: error budgets propagated measurement error while
omitting intrinsic population scatter and selection covariance.
**Rule: multiply every forecast σ by 3 before deciding whether a test
is worth running.** Record the forecast and the realized σ in every run
report so the multiplier can be recalibrated.
