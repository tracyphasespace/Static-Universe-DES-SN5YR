# Pre-registration: the chromatic side channel's two fingerprints

**Date: 2026-08-03.** Registered BEFORE (a) any Rubin/LSST supernova sample exists at the
required depth, and (b) the real-SED (Hsiao-template) rerun of the toy computation — this
document is committed first so the amended signature cannot be accused of being informed by
the numbers that follow it. The real-SED pass UPDATES the registered magnitudes; it does not
establish the form.

Provenance: `sne_open_items_b1.py` (commit 4c8432f) and `sne_wien_lightcurve_shift.py`
(commit fc2db63), toy model = blackbody photosphere 15,000 → 5,000 K, top-hat DES bands,
η = π²/β² geometric, b = 1 envelope. No dust/CSM systematics floor included (owed).

## Amendment to the registered signature (logged with cause)

The book's prior register (§10.6.3, §10.8.4a) stated the rise/decay asymmetry "scales as
λ^(−1/2)". **That is superseded.** The program's own computation found the band dependence
far steeper: the asymmetry tracks the SED's *within-band Wien sweep* — the flux-weighted
mean frequency of the cooling photosphere moving across the filter's internal ν^(1/2)
opacity gradient — which is violent on the Wien side (g) and nearly nil in the
Rayleigh–Jeans tail (z band). The λ^(−1/2) law describes the opacity, not the asymmetry.
Error found by the program's own computation; amendment logged before any confronting data.

## Fingerprint 1 — flux: rise/decay differential extinction (mmag)

Rise-phase minus decay-phase band-averaged extra dimming (toy precision):

| band | z=0.1 | z=0.3 | z=0.5 | z=0.8 | z=1.0 |
|------|-------|-------|-------|-------|-------|
| g | 0.40 | 1.28 | 2.23 | 3.70 | 4.68 |
| r | 0.15 | 0.48 | 0.85 | 1.46 | 1.89 |
| i | 0.05 | 0.17 | 0.31 | 0.54 | 0.70 |
| z | 0.03 | 0.10 | 0.19 | 0.33 | 0.43 |

Band ordering at z = 0.5: g : r : i : z = 1.00 : 0.38 : 0.14 : 0.08
(vs λ^(−1/2)'s 1.00 : 0.86 : 0.78 : 0.72 — the superseded form).

## Fingerprint 2 — timing: band-ordered width perturbation (differential form ONLY)

The chromatic channel perturbs the apparent width on top of the shared achromatic (1+z)
envelope by an effective per-band Δb (toy precision, z = 0.5):

| band | Δb_eff |
|------|--------|
| g | +9.4×10⁻⁴ |
| r | +4.6×10⁻⁴ |
| i | +1.9×10⁻⁴ |
| z | +1.3×10⁻⁴ |

The curve center does not move (|Δt_peak| < 0.03 d at all bands/z ≤ 1).

**Registered test (differential only):** b(g) − b(z-band) ≈ +8×10⁻⁴ measured *within the
same supernovae*, where band-shared systematics (template choice, selection, redshift
errors) cancel. NOT registered as an absolute per-band b measurement: White et al.'s error
is ±0.005 (stat) ± 0.010 (sys); systematics do not shrink with √N, and the absolute signal
sits ~12× below the current systematic floor. The differential test is live if and only if
the dominant terms in the 0.010 are band-shared — **follow-up owed:** decompose White et
al.'s systematics table into band-shared vs band-dependent (calibration, filter-throughput
drift) components; if band-dependent terms dominate, the test needs more statistics or a
smarter estimator, and this registration says so in advance.

## Consistency gate already passed (with teeth)

If the chromatic channel's width contamination had exceeded ~0.5% band-differentially, the
confluence model was dead on arrival against the measured achromaticity. Computed
contamination: 1–8% of the current bound. The model could not have been tuned to pass —
the contamination is derived from η = π²/β² and the Wien sweep, not fitted.

## What the rivals predict

Expansion: exactly zero for both fingerprints (achromatic, symmetric dilation by
construction). Dust: λ^(−1) extinction with no band-ordered *width* effect and no
rise/decay phase correlation. Both fingerprints are currently invisible (mmag flux,
10⁻⁴ timing) and both are predicted, band-ordered, and dated before the data.

## Scope statement

What the confluence model reproduces today, conditionally: the three measured envelope
statistics ((1+z) width, band-equality to 0.5%, symmetry) and the Hubble diagram at equal
fitted-parameter count — NOT per-supernova flux time series. The (1+z) envelope rests on
cycle conservation under Branch B [OPEN author ruling]. The honest verb is "reproduces,
conditionally," with the ruling named.

---

## ADDENDUM (2026-08-03, post-registration): real-SED update — Hsiao template, DES throughputs

Committed after the registration above, as required. `sne_wien_realSED.py`.

**What survives at template precision:**
- All magnitudes: flux fingerprint 0.5–3.4 mmag (valid range), timing perturbation
  5×10⁻⁴–4×10⁻³ in b. **Consistency gate re-passed**: max Δb = 3.2×10⁻³ = 29% of White's
  σ_b — derived, not fitted, and still could not have been tuned.
- Curve center immobile: centroid shift ≈ 0.01 d at all valid band/z.
- Flux-fingerprint band ordering at z = 0.5: 1.00 : 0.78 : 0.45 : 0.10 — monotonic and
  steeper than λ^(−1/2), consistent with the registered amendment.

**What does NOT survive:**
- The toy's clean Wien-sweep ordering in the TIMING channel. With the real template and a
  morphology-robust (second-moment) estimator, r-band exceeds g-band at valid redshifts and
  the registered differential b(g) − b(z-band) ≈ +8×10⁻⁴ is sign- and estimator-dependent
  (template: −7×10⁻⁴ with half-max widths; −1.0×10⁻³ g−r with moments). Causes identified:
  (i) g band samples rest-frame < 3000 Å (template-UV-limited) already at z = 0.5;
  (ii) SN Ia secondary maxima in i/z wreck half-max width metrics; (iii) real
  spectral-phase evolution (line blanketing) modulates the within-band sweep at its own order.

**Revised registration status of Fingerprint 2:** the *scale* (band differentials of order
10⁻³ in b) and the *existence* of a band-patterned width perturbation remain registered;
the *sign/ordering* is withdrawn from registration pending a fitter-grade estimator on a
modern template ensemble (SALT3/BayeSN) with the UV-coverage mask applied. Fingerprint 1
(mmag rise/decay flux asymmetry, monotonic ordering steeper than λ^(−1/2) at moderate z)
stands as registered.

**Follow-ups owed:** (1) decompose White et al.'s ±0.010 systematic into band-shared vs
band-dependent terms; (2) fitter-grade width estimator; (3) dust/CSM floor; (4) replace
Hsiao UV with a UV-constrained template before quoting any g-band number beyond z ≈ 0.3.
