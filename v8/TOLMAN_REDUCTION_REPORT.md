# Tolman static-frame reduction — EXECUTED. K1 fires: the model fails its primary registered test.

**Run:** 2026-08-20, per `preregistration/tolman_static_reanalysis.md`
(Branches Z and E, Amendment 1, kill conditions K1/K2, anti-cherry-pick
clause). Producer: `src/rawframe/tolman_reduction.py`. Data:
`data_ls2001/` (L&S 2001 Papers I + IV arXiv source tables, PROVENANCE.md).
Frame conversion uses **L&S's own Table 8 "Tired Light" column**, whose
d_A is identical in form to the model's d_A = (c/H₀)ln(1+z) (verified to
3 decimals), making the frame arithmetic indisputable.

## Validation gate: PASSED, exactly

With zero frame shift the machinery reproduces every published L&S
value: all 15 cluster × η ΔSB entries to ≤ 0.03 mag, and the published
finals to the last digit — n_R = 2.60 ± 0.18 (published 2.59 ± 0.17),
n_I = 3.37 ± 0.13 (published 3.37 ± 0.13). Two implementation details
were fixed during bring-up, both from L&S's own text and both while the
gate still failed (no result-steering possible): the Table 3
nonlinearity correction makes the local lines *fainter* (their explicit
wording), and it applies only to the η ≥ 1.3 relations (η = 1.0 is
valid to log R > 3.0 unextended).

## Branch Z (primary registered analysis: static frame, zero evolution)

| | measured (static) | model n_eff | tension |
|---|---|---|---|
| n_R (Cl 1604+4321, z = 0.924) | **1.52 ± 0.17** | 2.18 | **−3.8σ** |
| n_I (two clusters, z̄ = 0.83) | **2.28 ± 0.13** | 2.16 | **+0.9σ** |
| spread n_I − n_R | **+0.76 ± 0.22** | −0.01 | **3.5σ** |

**Adjudication under the registered rules:**

- **K1 FIRES.** The joint (n_R, n_I) is inconsistent with the
  prediction at > 3σ, driven entirely by the R band, and the
  registration forbids an evolution rescue within Branch Z. Under the
  primary registered analysis, **the two-channel model fails the Tolman
  test.** The failure direction is noteworthy: the model predicts *more*
  R-band dimming than observed — the opposite of the classic tired-light
  failure mode.
- The pre-registered analytic forecast (committed before this reduction:
  n_I → 2.30 ± 0.13 at +1.1σ, n_R → 1.45 at −4.3σ, spread 3.7σ) is
  confirmed almost exactly (2.28 at +0.9σ, 1.52 at −3.8σ, 3.5σ). Both
  declared findings held: **the face-value 9.2σ I-band exclusion is
  dead** — in the model's own frame the I band agrees at 0.9σ — and the
  constraint migrated to R exactly as declared in advance.
- Per the anti-cherry-pick clause, these are reported together: the
  I-band success may not be cited without the R-band failure and the
  spread.

## Branch E (committed passive evolution over static lookback): no rescue

With the pre-committed evolution prescription (ΔM_R = −0.40 ± 0.10 z,
ΔM_I = −0.33 ± 0.08 z, from FP M/L-evolution literature, fixed before
any static number was seen): n_R becomes consistent (−0.6σ) but n_I
flips adverse (**+3.2σ** nominal; ~2.6σ adding the local-line and
K-correction systematic budget). **K1-E fires at nominal errors.** No
branch achieves joint consistency, because no gray mechanism can: the
data's band spread (+0.76 ± 0.22) is invariant under any distance
reassignment and any band-independent evolution, while the model
predicts ≈ 0.

## The irreducible obstruction — and its documented confound

The single fact no version of the model reproduces is the band spread.
To produce it via propagation the opacity would need to *rise* with
wavelength (more dimming in I than R) — opposite to the Kelvin λ^(−1/2)
law and fatal to the SN color sector; no rescue exists within the
model's structure. However, the reduction quantifies a confound that
was flagged (in general terms) before execution: **band is 100%
degenerate with cluster** in L&S's design — R was measured only in
Cl 1604+4321, I only in the other two. The whole model failure is
carried by the one cluster whose K-correction is the largest and most
SED-model-dependent in the study (K(R) = 1.89 ± 0.06 at z = 0.924,
where observed R samples rest ~3600 Å). Both I clusters independently
bracket the model prediction (η-averaged n = 2.17–2.38 vs 2.16). This
is stated as a confound requiring K2, not as a rescue.

## Benchmark: L&S's own tired-light computation (added to the registration pre-reduction)

Classic tired light (no time dilation, n = 1) remains excluded in this
reduction: 3.1σ high in R and **9.8σ high in I** — L&S's original
conclusion is confirmed by our machinery. The two-channel model
(n_eff ≈ 2.2) is a different theory and fares differently: it passes I
and fails R, as above.

## Standing verdict and the K2 path

Per the registration: **the model FAILED its primary Tolman test (K1,
Branch Z), and Branch E does not rescue it (K1-E nominal).** This goes
into the falsification ledger as an adverse executed result — the first
registered kill to fire in the program.

What remains open is exactly what K2 anticipated: the verdict rests on
a band spread carried by a single cluster with the study's most
uncertain K-correction. K2's terms: if an **independent modern
surface-brightness dataset** (multi-band per cluster, modern SED-based
K-corrections) reproduces a spread of this sign and size, the model is
dead on Tolman with no remaining outs; if the spread proves to be a
K-correction/systematic artifact of the 2001 single-band-per-cluster
design, the Tolman verdict reverts to the I-band-like agreement. Either
way the next step is data, not argument. Until K2 is executed, the
ledger row reads: **"Tolman: FAILED (K1) — confound documented, K2
pending."**
