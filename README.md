# Static Universe DES-SN5YR — Two-Component Scattering

Companion code repository for *"A Static-Universe Two-Channel Photon
Propagation Model Confronted with DES-SN5YR"* (T. McSheery, **Version 8.0
— human-circulation freeze**, 20 August 2026), published at DOI
[10.5281/zenodo.22032094](https://doi.org/10.5281/zenodo.22032094).
The PDF is in [`paper/`](paper/) (SHA-256-verified against the Zenodo
deposit); the V8 freeze summary is in [`v8/`](v8/) and the canonical
claim-to-source map in [`v7/`](v7/). Prior records are preserved as
provenance: V7
([10.5281/zenodo.22031627](https://doi.org/10.5281/zenodo.22031627)),
Draft 6
([10.5281/zenodo.22031121](https://doi.org/10.5281/zenodo.22031121)) and
Draft 5
([10.5281/zenodo.22025329](https://doi.org/10.5281/zenodo.22025329)),
all PDFs kept in `paper/`.

> **Draft 5 erratum — resolved in Draft 6:** the Draft 5 PDF's front
> matter cited the methods paper's DOI as its own; Draft 6's front matter
> carries the correct DOI chain (current 22031121, supersedes 22025329,
> companion methods 22022089).

The proof-ledger work behind V7 — the d_A = D derivation and
Etherington-duality signature, the two-faced forward vertex (temporal law
Δt_obs = Δt_em·(1+z)^{κ_r} with κ_r ≃ 1 *measured*; the equality of
timing and redshift rates is the open microscopic derivation, not an
assumed identity), the self-falsified passband-artifact hypothesis, the
pre-registered Tolman static-frame reduction (Branches Z and E), and the
executed T4 species-clock test (inconclusive, fully disclosed) — is in
[`draft6/`](draft6/) (chronological record) with the canonical V7 map in
[`v7/`](v7/).

## The two papers, and what lives where

| paper | claim | code |
|---|---|---|
| [Methods paper](https://doi.org/10.5281/zenodo.22022089) ([repo](https://github.com/tracyphasespace/Model-Discrimination-DES-SN5YR)) | BBC-layer leverage measurement — no cosmological claim | Hubble-diagram fits, bracket, projection, probes, Camilleri amplitude comparison, manifest CI |
| **This paper** ([Zenodo](https://doi.org/10.5281/zenodo.22032094), V8) | the static two-channel propagation interpretation | this repository |

The papers are logically independent: the leverage measurement stands
whatever one thinks of this interpretation.

## Claim-to-source map

**Canonical (V7): see [`v7/README.md`](v7/README.md).** The map below is
the Draft-6-era version, kept for the record; V7 renumbers sections and
replaces the "b = 1 identity" framing with the measured κ_r coefficient.

### Draft-6-era map (historical)

| Draft 6 section | claim | source |
|---|---|---|
| §3.1–3.2 | wake field; b = 1 as an identity in W = ∂t ln n | [`draft6/docs/WAKE_FIELD_FORMULATION.md`](draft6/docs/WAKE_FIELD_FORMULATION.md) |
| §3.3–3.4, Eq. (16) | chromatic depletion; phase-flat Q(z) = 0.979/0.964/0.944 at z = 0.25/0.5/1.0; τ∞,B = 0.594 | [`draft6/docs/SPECTRAL_CLOCKS.md`](draft6/docs/SPECTRAL_CLOCKS.md), `draft6/src/rawframe/da_tolman.py` |
| §4 | passbands cannot manufacture b = 1 (≤ 0.05% stretch, ≤ 0.05 d peak shift, remap off) | `draft6/src/rawframe/transfer_integral.py` |
| §5 | released Hubble diagram Δχ² = +1.1; BBC leverage L = −11.7 (methods layer) | **[companion methods repo](https://github.com/tracyphasespace/Model-Discrimination-DES-SN5YR)** — CI-verified there |
| §6.2 | T4 iron-group clock: b₂ = 0.52 ± 0.78, N = 120, inconclusive, full trail | [`draft6/prereg/secondary_maximum_phase.md`](draft6/prereg/secondary_maximum_phase.md), [`draft6/docs/T4_RUN_REPORT.md`](draft6/docs/T4_RUN_REPORT.md), `draft6/src/rawframe/secondary_max_test.py` |
| §7, Eq. (24)–(28) | Tolman: static-frame n_R ≃ 1.45, n_I ≃ 2.30; frame-invariant band spread 3.7σ; preregistered reduction | [`draft6/docs/DA_TOLMAN_DERIVATION.md`](draft6/docs/DA_TOLMAN_DERIVATION.md), [`draft6/prereg/tolman_static_reanalysis.md`](draft6/prereg/tolman_static_reanalysis.md), `draft6/src/rawframe/tolman_frame_shift.py` |
| §8 | energy/image ledger: 16% by z = 1, prompt cascade, no optical halos | `draft6/docs/DA_TOLMAN_DERIVATION.md` §6 |

## Draft 5 legacy map (scripts still shipped and runnable)

| Draft 5 section | claim | script / source |
|---|---|---|
| §5–6.2, Eq. (12)–(13) | static probe law; Δχ² = +1.1 released, +12.8 pre-BBC, L_BBC = −11.7; Camilleri amplitude comparison | **companion repo** — `bracket.py`, `envelope.py`, `probes.py` (CI-verified there) |
| §4 | chromatic rise/decay fingerprints: 0.5–3.4 mmag, g:r:i:z ≈ 1.00:0.78:0.45:0.10 at z = 0.5 | `src/sne_wien_lightcurve_shift.py` (toy blackbody), `src/sne_wien_realSED.py` (Hsiao real-SED pass), `src/sne_open_items_b1.py`; registered outputs + the 2026-08-03 pre-registration in [`registered/`](registered/) |
| §6.3 | SALT-free raw-photometry transfer fit | `src/transfer_pipeline.py` — the **b = 1 canon-updated pipeline** (see status note below) |

## Status note on Draft 5 §6.3 — read this before comparing numbers

The paper reports a prior fit (3,882 SNe, 0.40 mag scatter) and correctly
labels it *partial consistency*: that implementation used a since-withdrawn
(1+z)^(1/3) envelope, and the paper states the pipeline "must be rerun with
the coherent b = 1 envelope." **This repository ships that rerun.**
`src/transfer_pipeline.py` is the corrected instrument: b = 1 envelope
(parametrized via `QFD_B_EXP`), empirical k_geom, q = 1 distance, η as an
explicit parameter (`QFD_ETA`), canonical raw photometry with sentinel
handling, and an optional no-redshift Ia-purity filter (`QFD_IA_ONLY=1`,
Moller et al. 2024 light-curve-only classifier). Current reference numbers
(Ia-filtered, η = 0.3015): **N = 1,480 fitted, σ_clip = 0.484 mag, z-slope
−1.64 mag/z** — the residual slope is the expected uncorrected Malmquist
trend of a flux-limited raw sample (no selection correction is applied
here; that is the point). The paper's historical 0.40-mag figure came from
a different selection and the withdrawn envelope, and is superseded by this
pipeline.

## Run it

```bash
pip install -r requirements.txt
cd data && ./fetch.sh && cd ..   # raw light curves (from the companion repo,
                                 # sha256-verified there) + DES v1.2 files

# chromatic fingerprints (self-contained, no survey data needed):
python src/sne_wien_lightcurve_shift.py   # toy-model timing imprint
python src/sne_wien_realSED.py            # Hsiao real-SED pass (sncosmo)
python src/sne_open_items_b1.py           # rise/decay magnitude differential

# the b=1 SALT-free transfer fit (~3 min):
QFD_IA_ONLY=1 QFD_ETA=0.3015 python src/transfer_pipeline.py
```

Outputs can be compared against the frozen registered copies in
[`registered/`](registered/), which include the pre-registration document
committed **before** the real-SED pass (2026-08-03).

## Falsification (paper §8)

The paper names its kill conditions: (i) an observer-frame multiband
measurement of the chromatic rise/decay asymmetry below the registered
amplitude range falsifies the non-forward channel; (ii) a matched DES
bias-correction rerun with the static law as reference input measures the
currently unisolated conditioning component; (iii) coherence/image-quality
constraints must be satisfied simultaneously; (iv) the microscopic
normalization of η remains open and is stated as such.

## Data & license

Raw griz light curves for all 8,293 DES transient candidates are hosted
(gzipped + sha256) in the
[companion repository](https://github.com/tracyphasespace/Model-Discrimination-DES-SN5YR);
DES-SN5YR release files are fetched pinned at tag v1.2. DES data © the DES
Collaboration (public release). Code: MIT.

## Acknowledgments

The author would like to thank Anthropic, Google, and OpenAI for their
excellent tools which enabled the scripts and mathematical assistance as
well as collaborative/adversarial interactions to resolve the thousands
of details at the speed of electrons.
