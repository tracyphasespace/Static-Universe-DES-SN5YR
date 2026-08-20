# Pre-registration: static-law rerun on the DES-Dovekie recalibrated vector

**Registered:** 2026-08-20, before fetching or inspecting any Dovekie
data values. Data location confirmed (file names only):
`github.com/des-science/DES-SN5YR/4_DISTANCES_COVMAT/` now contains
`DES-Dovekie_HD.csv`, `DES-Dovekie_Metadata.csv`, `STAT+SYS.npz`
(1820 SNe; Popovic et al. 2026, arXiv 2511.07517 — flat-ΛCDM Ωm moves
0.352 → 0.330 ± 0.015 after cross-calibration and SALT3 retraining).
Upstream HEAD supersedes the original SN5YR products; our published
results remain reproducible because all fetches are pinned at tag v1.2.

## Why this matters

V8's headline near-degeneracy (Δχ² = +1.1) is a statement about the
frozen v1.2 vector, and says so. If the near-degeneracy **persists under
an independently revised DES calibration**, it is substantially harder
to dismiss as an accident of one released Hubble diagram. If it
**breaks**, that is an adverse result and will be reported as such.

## Estimator (frozen — identical to the methods-paper machinery)

1. Same two one-parameter distance laws as the methods paper: flat ΛCDM
   (Ωm free) vs the static probe law (η free, probe law fixed as
   published — no new parameters, no shape changes).
2. Official DES redshift convention: μ ∝ 5·log₁₀[(1+z_HEL)·D_M(z_HD)]
   (z_HEL from the Dovekie metadata; if absent, the fallback and its
   effect are documented as an amendment).
3. Full released STAT+SYS covariance; fit by the same χ² machinery
   (`bracket.py` lineage), Dovekie vector swapped in, nothing else
   changed.
4. Report: χ²_ΛCDM, χ²_static, **Δχ² = χ²_static − χ²_ΛCDM**, best-fit
   (Ωm, η), and N used.
5. Secondary (descriptive, if the released columns permit): the
   pre-correction leverage L_BBC on the Dovekie vector, same
   MU + biasCor reconstruction as the methods paper.

## Pre-committed reading (no post-hoc reinterpretation)

- **|Δχ²| ≲ 5:** the near-degeneracy is robust to the DES recalibration
  — the strongest available upgrade to the SN-sector claim.
- **Δχ² ≳ +25:** the static law is disfavored by the recalibrated data;
  reported as an adverse result in the falsification ledger, alongside
  the v1.2 number, without reweighting or new freedom.
- **Δχ² strongly negative:** reported with caution and an explicit
  search for calibration-systematic explanations before any favorable
  claim is made.
- Intermediate values: reported as measured; no third narrative.
- **No-freedom clause:** no added parameters, no SN cuts beyond DES's
  own Dovekie selection, no convention changes after data inspection.
  Any forced deviation is a documented amendment, labeled pre/post-data.

## Context note

Popovic et al. 2026 report evidence for *evolving dark energy* within
the FLRW framing — i.e., the recalibrated data moved *away* from the
cosmological constant in the standard analysis. Whatever Δχ² the static
law returns, the comparison target is flat ΛCDM on the same vector, per
the frozen estimator; w₀wₐ comparisons are out of scope here.


---

## RESULT (2026-08-20, POST-UNBLIND — appended after the author's unblind ruling)

Validation gate re-passed at run time (v1.2 manifest reproduced exactly:
1640.1 / 1641.1, Delta chi2 = +1.1). Then, on the frozen Dovekie files
(sha256 in data/dovekie/SHA256SUMS):

- **N = 1820. chi2_LCDM = 1631.4 (Omega_m = 0.330). chi2_static = 1633.2
  (eta = 0.332). Delta chi2 = +1.8.**
- Pre-committed reading: |Delta chi2| <~ 5 -> **the near-degeneracy is
  ROBUST to the independent DES recalibration.** No other reading applies.
- Pipeline cross-check: the recovered Omega_m = 0.330 equals the published
  Dovekie flat-LCDM value (0.330 +/- 0.015) independently of our model.
- Parameter drift under recalibration: eta 0.297 -> 0.332 (~12%), Omega_m
  0.352 -> 0.330 — both models absorbed the calibration shift; the
  comparison did not move outside the band.
- **Secondary (registered, descriptive): Dovekie pre-BBC margin = +4.2
  (Omega_m = 0.394, eta = 0.215), so L_BBC = 1.8 - 4.2 = -2.4** — down
  from -11.7 on v1.2. The correction layer's leverage on this comparison
  fell by ~5x in the recalibrated release; released and pre-correction
  margins are now same-sign and both within the robust band. The
  methods-paper concern (correction-dominated comparison) is materially
  reduced in Dovekie, which strengthens the robustness reading.

Scope kept: flat LCDM is the frozen comparison target; Dovekie's own
w0wa/evolving-DE analysis is out of scope. No amendments were needed; the
estimator ran exactly as frozen.
