# Retroactive frame audit of the two executed reports (per FRAME_LEDGER.md)

**Date:** 2026-08-20. Scope: TOLMAN_REDUCTION_REPORT.md and
ANGULAR_SIZE_REPORT.md. Mechanical pass: `frame_lint.py` (findings
reproduced by running it). Manual pass below lists every place a
frame-valued quantity entered a comparison, with two NEW leaks not named
by any reviewer.

## Tolman reduction — frame-valued entries

| quantity | tag | status in the report |
|---|---|---|
| log R (pc) from L&S tables | [frame: FLRW-q0.5], converted via their Table 8 | **labeled and un-baked** — clean |
| K-corrected ⟨SB⟩ | [frame: template-BC96-evolved, color-matched to observed colors] | entered the K1 verdict **as if frame-free**; documented only post-verdict (addendum). The R-band failure sits entirely under the largest such correction. |
| **NEW LEAK 1 — Paper I local zero points**: the ⟨z⟩ = 0.037 → z = 0 correction (0.16 mag) assumed n = 4 | [frame: FLRW] | unlabeled everywhere until now. Under n ≈ 2.2 the correction is ~0.09 → a **~0.07 mag common-mode systematic in every ΔSB (Δn ≈ +0.10 on all measured exponents; measured n values are biased HIGH by ~0.1 under non-FLRW readings)**. Direction: slightly relieves the A′ R-band tension, slightly worsens I. Small; now on the ledger. |
| **NEW LEAK 2 — τ∞,B = 0.594** (the opacity in every n_eff prediction) | [frame: FLRW-sim-conditioned via BBC; measured leverage L_BBC = −11.7 (v1.2) / −2.4 (Dovekie)] | the model's own prediction constant inherits the DES correction layer; unlabeled in all prediction tables. A raw-photometry η refit is the cure (the transfer_pipeline machinery exists). Magnitude on n_eff: the opacity term is ~0.2, so even a 30% η shift moves predictions by ~0.06 — small but must be tagged. |
| Branch-E evolution priors (0.40z / 0.33z) | [frame: FLRW] (FP M/L rates measured with FLRW d_L; adopted as empirical z-scalings) | partially labeled ("frame-agnostic at first order") — tag retained. |
| Linter: 4 mechanical findings (lookback untagged; "size evolution" as unqualified noun ×3) | | vocabulary violations of §3; the addendum text treats βs correctly as a parameter, but three sentences use "size evolution" as a fact-noun. |

## Angular-size test — frame-valued entries

| quantity | tag | status |
|---|---|---|
| angular r (arcsec), mag, Sérsic n, q, measured z | frame-free | clean — the test's design point |
| logM ≥ 10.3 selection | [frame: FLRW] (FAST masses via FLRW d_L) | **flagged in the report but load-bearing and unresolved**: the registered flux-selected robustness variant is owed before the K2-ang result is cited as decisive. This is the report's largest open frame leak. |
| photometric redshifts (zpk) | [frame: weak-template] | unlabeled; second-order (wavelength-ratio measurement), tag added to ledger. |
| ΛCDM/coasting d_A in the fitted shapes | hypothesis under test | correctly labeled by construction |
| "star-forming disks genuinely grow (inside-out growth astrophysically expected)" | vocabulary violation (§3): asserts a time-ordered growth narrative, i.e. t = t(z) | should read: "the late-type θ(z) trend requires a z-dependent population parameter in every frame." The geometry-blind conclusion is unchanged; the phrasing presumed the thing under test. |
| linter: "no catalog kpc conversions" and quoted "size evolution" hits | benign (mentions of avoidance/quotation) | linter v1 noise; acceptable |

## Consequences

1. Neither report's *verdict* changes: the Tolman K1 conditionality was
   already established via the reading fork, and both new leaks are
   ~0.1-level in n; the angular K2-ang result's exposure is the mass
   cut, already flagged, with the robustness variant registered.
2. **Actions opened:** (a) flux-selected rerun of the angular test
   (registered robustness, now elevated to required before D-M relies
   on K2-ang); (b) raw-photometry η refit to de-BBC the opacity
   constant [instrument exists: transfer_pipeline]; (c) apply the
   ~+0.10 Δn zero-point correction as a systematic band in any future
   use of the L&S exponents; (d) both reports' prose to be brought to
   FRAME_LEDGER §3 vocabulary at next edit (verdicts untouched;
   wording only — the record keeps originals, per provenance rules).
3. The CANDELS K2 test (`preregistration/candels_tolman_k2.md`) is
   frame-clean by design except the same mass cut — its registration
   already includes the narrow-mass and Kormendy robustness variants.
