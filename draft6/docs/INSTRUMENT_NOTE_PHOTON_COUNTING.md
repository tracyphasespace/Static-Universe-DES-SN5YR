# Instrument note: dedicated photon-counting telescope for the Q(z) and T4 measurements

**Date:** 2026-08-20 (author's concept note, recorded after Draft 6
publication). Expands Draft 6 §9 ("A purpose-built photon-counting
experiment", DOI 10.5281/zenodo.22031121). Motivated directly by the two
instrument-limited results of the campaign: T4's cadence-starved
b₂ = 0.52 ± 0.78, and the Q(z) amplitude test sitting at the 5–15%
spectrophotometric calibration floor of survey slit spectroscopy.

## Concept

A dedicated, rapid-response telescope using narrow-band **dichroic
filtering** and **avalanche photodiode (APD/SPAD) photon counters** in
targeted rest-frame passbands — replacing slit spectroscopy with
high-cadence photon counting in simultaneously registered bands.

## Key advantages over survey pipelines

- **Bypasses spectroscopic slit losses.** Slit spectrographs lose blue
  light to atmospheric dispersion and slit clipping — the 5–15% flux
  calibration uncertainty that blocks the Q(z) test today. APDs behind a
  dedicated narrow-field aperture integrate the full PSF, enabling
  sub-percent *relative* flux ratios.
- **Simultaneous multi-band registration.** A dichroic tree feeding
  simultaneous APD channels makes atmospheric transparency variations,
  thin cirrus, and seeing fluctuations cancel in the band *ratios* — the
  quantity the model actually predicts.
- **Solves the T4 cadence deficit.** The DES i/z secondary-maximum test
  was crippled by ~7-day cadence and noisy epoch extraction
  (b₂ = 0.52 ± 0.78, realized σ(t₂) = 5.3 d). Daily or sub-daily tracking
  of a newly discovered event measures the secondary-maximum turn-around
  to sub-day precision — a decisive species-clock measurement per object
  rather than a 25×-underpowered ensemble.
- **Direct Q(z) verification.** Tracks the unwarped rest-frame UV
  (320–340 nm Fe/Ni complex) against the red optical reference
  (620–680 nm) with no continuum spline fitting — confronting the
  predicted **phase-flat** suppression Q = 0.979 / 0.964 / 0.944 at
  z = 0.25 / 0.5 / 1.0 (τ∞,B = 0.594 fixed in advance by the
  Hubble-diagram fit; the instrument does not get to choose its opacity).

## Critical design and engineering constraints

- **Silicon vs. InGaAs detector split.** For z ≲ 0.3, red-enhanced
  silicon APDs cover both channels. For z ≈ 0.5–1.0 the rest-650 nm
  reference window shifts to 975–1300 nm, requiring TE-cooled InGaAs/InP
  APDs or SNSPDs alongside the silicon channels.
- **Host-galaxy background baseline.** A narrow field of view minimizes
  diffuse host light, but post-fade host template subtraction remains
  necessary for faint high-z targets.
- **Alert-ingestion latency.** To capture the rise phase and establish
  the phase-flatness baseline, the telescope must ingest broker alert
  streams (Rubin LSST, ZTF) and begin counting within hours of candidate
  confirmation.

## Why this matters for the program

A purpose-built instrument focused on relative count ratios and
high-cadence timing turns the two remaining instrument-limited tests —
the phase-flat chromatic erosion (the ΛCDM discriminator) and the
species-clock universality (T4) — from disputes over pipeline and
calibration artifacts into clean physical measurements. Both tests come
with kill conditions already registered
(`preregistration/secondary_maximum_phase.md`; SPECTRAL_CLOCKS.md §2
amendment 2 for the Q(z) estimator).
