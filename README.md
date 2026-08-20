# Static Universe DES-SN5YR — Two-Component Scattering

Companion code repository for *"A Static-Universe Two-Component Scattering
Interpretation of DES-SN5YR Supernovae"* (T. McSheery, Draft 5, 20 August
2026), published at DOI
[10.5281/zenodo.22025329](https://doi.org/10.5281/zenodo.22025329).
The PDF is in [`paper/`](paper/).

> **Erratum (pending v2):** the published Draft 5 PDF's front matter cites
> "reserved archive DOI 10.5281/zenodo.22022089" — that is the *methods*
> paper's DOI. This paper's correct DOI is **10.5281/zenodo.22025329**.

## The two papers, and what lives where

| paper | claim | code |
|---|---|---|
| [Methods paper](https://doi.org/10.5281/zenodo.22022089) ([repo](https://github.com/tracyphasespace/Model-Discrimination-DES-SN5YR)) | BBC-layer leverage measurement — no cosmological claim | Hubble-diagram fits, bracket, projection, probes, Camilleri amplitude comparison, manifest CI |
| **This paper** ([Zenodo](https://doi.org/10.5281/zenodo.22025329)) | the static two-channel propagation interpretation | this repository |

The papers are logically independent: the leverage measurement stands
whatever one thinks of this interpretation.

## Claim-to-script map (paper section → code)

| paper section | claim | script / source |
|---|---|---|
| §5–6.2, Eq. (12)–(13) | static probe law; Δχ² = +1.1 released, +12.8 pre-BBC, L_BBC = −11.7; Camilleri amplitude comparison | **companion repo** — `bracket.py`, `envelope.py`, `probes.py` (CI-verified there) |
| §4 | chromatic rise/decay fingerprints: 0.5–3.4 mmag, g:r:i:z ≈ 1.00:0.78:0.45:0.10 at z = 0.5 | `src/sne_wien_lightcurve_shift.py` (toy blackbody), `src/sne_wien_realSED.py` (Hsiao real-SED pass), `src/sne_open_items_b1.py`; registered outputs + the 2026-08-03 pre-registration in [`registered/`](registered/) |
| §6.3 | SALT-free raw-photometry transfer fit | `src/transfer_pipeline.py` — the **b = 1 canon-updated pipeline** (see status note below) |

## Status note on §6.3 — read this before comparing numbers

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
