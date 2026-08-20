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

**LaTeX source:** [`../paper/Static_Universe_DES_SN5YR_V8.tex`](../paper/Static_Universe_DES_SN5YR_V8.tex)
(SHA-256 `7a00004226f309f2f7f03c05001ea8d61c317d1cd52ab3b2caae98f136bb350e`).

**Scope note — DES-Dovekie (added 2026-08-20):** DES has superseded the
original SN5YR cosmology products with the recalibrated **DES-Dovekie**
analysis (Popovic et al. 2026, arXiv:2511.07517; flat-ΛCDM Ωm moves
0.352 → 0.330 ± 0.015; upstream repository HEAD now carries
`DES-Dovekie_HD.csv` + `STAT+SYS.npz`, 1820 SNe). V8's Δχ² = +1.1 is a
statement about the frozen v1.2 vector, exactly as the paper says — all
fetches in these repositories are pinned at tag v1.2, so the published
results remain reproducible. The static-law rerun on the Dovekie vector
was **pre-registered before any data inspection and has now been
executed** ([`DOVEKIE_RERUN_PREREG.md`](DOVEKIE_RERUN_PREREG.md), result
appended post-unblind): **Delta chi2 = +1.8** (N = 1820; recovered
Omega_m = 0.330 matches the published Dovekie value; eta = 0.332). Per
the pre-committed band |Delta chi2| <= ~5, **the near-degeneracy is
robust to the independent DES recalibration** — no longer attributable
to one released vector. Secondary registered measurement: the BBC-layer
leverage on this comparison fell from -11.7 (v1.2) to **-2.4**
(Dovekie); released and pre-correction margins are now same-sign and
both within the band.

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
