# Pre-registration: static-frame Tolman reanalysis of Lubin & Sandage 2001

**Registered:** 2026-08-20, BEFORE any reduction of the L&S photometry.
**Producer for all numbers herein:** `src/rawframe/tolman_frame_shift.py`
(analytic frame-shift estimate; deterministic, no data touched yet).
**Data (to be fetched, step 1):** Lubin & Sandage 2001, Papers I–IV
(AJ 121, 2271 = Paper I local calibration; AJ 122, 1071 = Paper III HST
profiles; AJ 122, 1084 = Paper IV Tolman signal; arXiv astro-ph/0102213,
0106563, 0106566). 34 early-type galaxies, clusters Cl 1324+3011 (z = 0.76),
Cl 1604+4304 (z = 0.90), Cl 1604+4321 (z = 0.92).

---

## 1. Why the published exponents are frame-dependent — measured from L&S's own grid

L&S place high-z galaxies on the local ⟨SB⟩–size relation using linear radii
R = θ·d_A computed in FLRW. The published exponents therefore depend on the
assumed distance scale — and L&S *measured* that dependence by publishing n
for three deceleration parameters:

| q₀ | n_R | n_I | mean log₁₀ d_A (c/H₀) |
|---|---|---|---|
| 0 | 2.28 | 3.06 | −0.450 |
| 1/2 | **2.59 ± 0.17** | **3.37 ± 0.13** | −0.543 |
| 1 | 2.81 | 3.55 | −0.605 |

Regressing n on log₁₀ d_A: **S_R = −3.41/dex, S_I = −3.17/dex**, with
linearity residuals ≤ 0.011 across the grid — the response is measured, not
assumed, and it is linear where measured.

The static frame assigns d_A = D = (c/K)ln(1+z), which at these clusters sits
**+0.335 dex above the q₀ = 1/2 scale** (ratio ≈ 2.2×: FLRW divides by (1+z),
the static frame does not). Extrapolating the measured response:

| band | q₀=1/2 frame | static frame (extrapolated) | prediction n_eff(z̄=0.86) | tension |
|---|---|---|---|---|
| rest-R | 2.59 ± 0.17 (**+2.4σ**) | **1.45 ± 0.17** | 2.18 | **−4.3σ** |
| rest-I | 3.37 ± 0.13 (**+9.3σ**) | **2.30 ± 0.13** | 2.16 | **+1.1σ** |

**Findings declared in advance:**
1. The face-value 9.2σ I-band exclusion is an artifact of the EdS distance
   frame. In the model's own frame the I-band lands ~1σ from the prediction.
2. The constraint *migrates* to R-band, which overshoots ~4σ BELOW the
   prediction (galaxies too dim… too *bright*? — sign: n smaller than
   predicted means less dimming than the model requires in R). We register
   this expected R-band problem now, so a favorable I-band outcome cannot be
   cherry-picked later.
3. **The frame-invariant discriminant is the band spread**: distance
   reassignment shifts both bands nearly equally (S_R ≈ S_I within 8%), so
   n_I − n_R = 0.78 ± 0.21 survives *any* choice of d_A(z). The model
   predicts −0.02 (chromatic opacity is slightly *stronger* in R than I).
   **3.7σ in every frame.** This — not the 9.2 — is the irreducible Tolman
   discrepancy. Under ΛCDM it is absorbed as band-dependent luminosity
   evolution; the static model forfeits that parameter and must either
   attribute it to a measurement systematic (34 galaxies, 3 clusters,
   1990s HST photometry, K-corrections) or fail.
4. Caveat on 1–2: a 3.5× linear extrapolation of a 0.1-dex calibration.
   It licenses "the face-value σ's are frame-fragile", NOT "resolved".

## 2. The full reduction pipeline (the decisive test)

1. **Fetch** L&S Papers I–IV tables (ADS/VizieR): per-galaxy Petrosian
   η radii, ⟨SB⟩ within η apertures, cluster redshifts, local calibration
   sample (Paper I).
2. **Metric aperture recalibration**: linear radii R = θ·(c/K)ln(1+z);
   K = H₀ (same H₀ as the local calibration; H₀ cancels in the offsets).
3. **K-corrections under the two-channel transfer**: achromatic coordinate
   mapping ν → ν/(1+z) of the rest SED, plus chromatic attenuation
   Δm_λ = (2.5/ln10)·τ_∞(λ)[1−(1+z)^{−1/2}], τ_∞,B = 0.594, τ ∝ λ^{−1/2}.
   (Second-order relative to step 2; bounded by Δτ across each band.)
4. **Zero-evolution constraint enforced**: ΔM_evol ≡ 0. No band-dependent
   evolution term is available to the static model.
5. **Refit** ⟨SB⟩ offsets from the (re-placed) local relation vs (1+z);
   report n per band with the full error budget (photometric, slope,
   aperture-η choice, K-correction).

## 3. Kill conditions (pre-committed)

- **K1 (joint exponent test):** if the full static-frame reduction yields
  (n_R, n_I) jointly inconsistent with the prediction
  (n_eff ≈ 2.16–2.18 at z̄ = 0.86, spread −0.02) at > 3σ with the full
  systematic budget, the two-channel model **fails the Tolman test**. No
  evolution rescue is permitted (§2 step 4).
- **K2 (spread test, frame-invariant):** if the reduced band spread
  n_I − n_R remains > 3σ from −0.02 AND an independent modern SB dataset
  (e.g., deep-survey early-type SB profiles, or Sandage 2010 follow-up)
  reproduces a spread of the same sign and magnitude, the model fails
  regardless of K1 — the spread cannot be blamed on one dataset twice.
- **Anti-cherry-pick clause:** the I-band improvement (finding 1) may not
  be reported without the R-band migration (finding 2) and the invariant
  spread (finding 3) in the same table.

## 4. Expected outcomes (registered)

- If the full reduction tracks the linear extrapolation: I-band consistent,
  R-band ~4σ low, spread 3.7σ — the model survives the *distance* part of
  Tolman and inherits a sharp two-band anomaly whose sign (more apparent
  dimming in I than R) is opposite to any opacity explanation available to
  it. That outcome would put the burden on the L&S K-corrections/photometry
  and mandate an independent dataset (K2).
- If the reduction departs strongly from linearity (the extrapolation is
  3.5× the calibrated range): report the measured curve n(log d_A) and
  apply K1 as written.
