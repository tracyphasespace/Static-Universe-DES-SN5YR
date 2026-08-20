# V8 — human-circulation freeze

**Paper:** *A Static-Universe Two-Channel Photon Propagation Model
Confronted with DES-SN5YR* (T. McSheery, **Version 8.0 —
human-circulation freeze**, 20 August 2026), DOI
[10.5281/zenodo.22032094](https://doi.org/10.5281/zenodo.22032094).
PDF: [`../paper/Static_Universe_DES_SN5YR_V8_Zenodo.pdf`](../paper/Static_Universe_DES_SN5YR_V8_Zenodo.pdf)
(SHA-256 `8c86666b06e7090d892ebc2a640c7f8e66a2e9d320b1d56de7ab636757f42a16`,
verified against the Zenodo deposit). Prior records preserved as
provenance: V7 (22031627), Draft 6 (22031121), Draft 5 (22025329) — all
PDFs in `../paper/`.

V8 applies the four freeze edits of
[`V7_FREEZE_CHECKLIST.md`](../v7/V7_FREEZE_CHECKLIST.md) — all four
acceptance tests verified present in the published PDF:

1. **CMB bath = drifting self-similar Planck solution** — the measured
   T_CMB(z) = (2.725 ± 0.002)(1+z)^(1−β) K with β = −0.007 ± 0.027
   (CO+SZ) is a zero-additional-parameter consistency of the Face-1
   drift; the stationary fixed-point bath is excluded by the same data;
   the low-frequency-cutoff escape is disowned via the 21-cm/UV absorber
   concordance (~10⁻⁵); the photon-number relaxation at rate 3K remains
   the stated open barrier (Table 1, red).
2. **Wake = direction-resolved phase-space susceptibility**
   χ(x, k̂, t); n_g = 1 + κ_r·K·ξ is the one-ray characteristic.
3. **κ_r empirically constrained ≈ 1** (FLRW: predicted; static:
   fitted); timing parsimony credit removed.
4. **Steady-source under-dilation withdrawn**; Brewer et al. (2025)
   n = 1.14 ± 0.34 leads; quasars reframed as response-bandwidth
   constraints.

**Status: FROZEN for human circulation.** The three targeted reviewer
questions (kinetic/nonlinear-optics theorist; CMB/cosmology expert;
supernova observer) are in the checklist. No further synthetic-referee
iterations. The claim-to-source map of [`../v7/README.md`](../v7/README.md)
remains valid for V8 (section numbering unchanged in substance); the
frozen T4 output lives at `../v7/results/t4_secondary_max.json`.

Research running in parallel without blocking circulation: the
preregistered static-frame Tolman reduction
([`../draft6/prereg/tolman_static_reanalysis.md`](../draft6/prereg/tolman_static_reanalysis.md),
Branches Z/E + the L&S tired-light benchmark).
