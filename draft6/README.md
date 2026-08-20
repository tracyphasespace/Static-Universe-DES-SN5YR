> **Chronological record of the Draft-6 cycle (2026-08-20).**
> Superseded as the canonical map by [`../v7/`](../v7/) — V7 (DOI
> 10.5281/zenodo.22031627) replaces the single-kernel "b = 1 identity"
> framing with the two-faced vertex and measured κ_r ≃ 1. Files here are
> preserved unmodified as provenance.

# Draft 6 working analysis — the proof ledger

Public support material for **Draft 6.0** of the static-universe paper —
**published 20 August 2026 at DOI
[10.5281/zenodo.22031121](https://doi.org/10.5281/zenodo.22031121)**
(supersedes Draft 5, 10.5281/zenodo.22025329); the PDF is in
[`../paper/`](../paper/Static_Universe_DES_SN5YR_Draft6_Zenodo.pdf).
Everything here is a verbatim provenance copy from the campaign repository
at commit `226f83d` (2026-08-20). Every number in the documents regenerates
from the scripts in `src/rawframe/`.

## What this adds beyond Draft 5

Responding to referee review of Draft 5, the model's remaining claims were
converted into explicit derivations and pre-registered tests:

| item | file | status |
|---|---|---|
| d_A = D derived; duality d_L/d_A = (1+z) | `docs/DA_TOLMAN_DERIVATION.md` | derived; clean geometric discriminator vs FLRW's (1+z)² |
| Wake wave equation; **b = 1 as an identity** | `docs/WAKE_FIELD_FORMULATION.md` | derived at effective-field level; microphysics owed against a six-constraint spec |
| "Filter/Wien erosion fakes dilation" artifact hypothesis | `docs/SPECTRAL_CLOCKS.md` §5, `src/rawframe/transfer_integral.py` | **self-falsified**: full Hsiao × real DECam transfer moves apparent stretch ≤ 0.05% and peak epochs ≤ 0.05 d with the remap off — dilation cannot be a passband artifact |
| Tolman: L&S face-value 9.2σ is frame-dependent | `prereg/tolman_static_reanalysis.md`, `src/rawframe/tolman_frame_shift.py` | calibrated from L&S's own q₀ grid: static-frame n_I → 2.30±0.13 (+1.1σ), n_R → 1.45 (−4.3σ); **band spread 0.78±0.21 vs −0.02 predicted = 3.7σ frame-invariant — the serious unresolved threat**; full reduction pre-registered with kill conditions |
| T4: iron-group secondary-maximum clock on raw DES i/z | `prereg/secondary_maximum_phase.md`, `docs/T4_RUN_REPORT.md`, `src/rawframe/secondary_max_test.py` | **executed: b₂ = 0.52 ± 0.78 (N = 120) — inconclusive.** Does not falsify the universal (1+z) remap; underpowered to distinguish it from no dilation (realized σ(t₂) = 5.3 d vs 2 d forecast; z ≤ 0.3 visibility window). No evidence *for* the model is claimed from this test. |
| §9 instrument concept: dichroic/APD photon-counting telescope for Q(z) + per-object T4 | `docs/INSTRUMENT_NOTE_PHOTON_COUNTING.md` | design note — sub-percent band ratios, sub-day secondary-max timing, alert-stream ingestion |
| Chromatic λ^(−1/2) erosion predictions | `docs/SPECTRAL_CLOCKS.md` §2–3, `src/rawframe/da_tolman.py` | Q = 0.979/0.964/0.944 at z = 0.25/0.5/1.0, **phase-flat**, amplitude fixed in advance by the Hubble-diagram fit — an independent discriminator, no longer used to explain dilation |

## Status statement (the level of claim the record supports)

The model is no longer dismissible as a classical static model: it
*predicts* the (1+z) light-curve broadening (b = 1 falls out of the wake
wave equation as an identity), it does **not** rely on chromatic scattering
to produce redshift or dilation (that route is self-falsified above at
≤ 0.05%), and a pre-registered species-clock test with explicit kill
conditions was executed and did not contradict it. T4 supplies **no
positive evidence** — a wide interval containing both hypotheses prefers
neither. The strongest standing threat is the Tolman surface-brightness
test: the face-value exclusion is frame-fragile, but the band-spread
discrepancy (3.7σ) survives any distance law and awaits the pre-registered
static-frame reduction of the Lubin & Sandage photometry.

## Running the code

Analytic producers (`da_tolman.py`, `tolman_frame_shift.py`,
`transfer_integral.py`) need only numpy/scipy/sncosmo (the Hsiao template
and DES bandpasses download via sncosmo on first use):

```
cd draft6/src && python3 -m rawframe.da_tolman
                 python3 -m rawframe.tolman_frame_shift
                 python3 -m rawframe.transfer_integral
```

`secondary_max_test.py` and the raw-DES c(z) slope additionally need the
DES-SN5YR raw photometry and HD+metadata tables (fetch instructions in the
[methods repo](https://github.com/tracyphasespace/Model-Discrimination-DES-SN5YR));
they expect a `rawframe.data` loader pointing at those files — the copy
here is for transparency of the exact executed code, with its full
amendment/defect trail in `docs/T4_RUN_REPORT.md`.
