# The wake as an explicit wave equation: independent-photon dilation with b = 1 as an identity

**Session:** 2026-08-20. Answers the referee's Issue 1 at the level requested
("write down the explicit Hamiltonian/wave equation showing how the medium
retains memory without transverse dispersion"). Supersedes the kinematic
presentation in WAKE_DERIVATION.md / WAKE_COEFFICIENT.md by grounding it in a
field equation; consistent with both. The n(t) global-drift toy remains
rejected (author ruling): everything here is **globally stationary, locally
transient**.

---

## 1. The objection, and why it proves too much

The referee's theorem: in a stationary (time-translation-invariant),
dispersionless medium, two photons emitted Δt_em apart on a fixed baseline
arrive Δt_obs = Δt_em apart. **The theorem is correct.** But its premise
already forbids the *redshift*, not just the dilation: by Noether's theorem,
elastic propagation through a time-translation-invariant system conserves ω.
A medium that redshifts light is therefore *necessarily* one of two things —

- (a) explicitly time-dependent (a global n(t) drift — the relocated scale
  factor; **rejected**), or
- (b) **inelastic**: the photon excites the medium, leaving energy behind.

QFD's forward channel is (b) by construction (dE/E = −K dl/c deposited into
the medium). And inelasticity is exactly what voids the theorem's premise for
the *second* photon: the corridor it traverses is not the corridor the first
photon found, because the first photon's passage — and the passage of the
entire leading light front — left excitation in it. The medium's *Hamiltonian*
is time-independent (globally stationary); the medium's *state* along a lit
corridor is not. The objection assumes the state is stationary; the observed
redshift already proves it is not.

## 2. The field equations

Let χ(x, t) be the corridor conditioning field (the wake amplitude: local
excitation density of the vacuum medium, normalized so the effective
refractive index is n = 1 + χ/2, n² = 1 + χ). Effective action for the
electromagnetic envelope A and the conditioning field:

  ℒ = (1/2)[ n²(χ) (∂_t A)²/c² − (∇A)² ] + ℒ_χ[χ; I]

with the beam intensity I sourcing χ. The wave equation:

  **(1 + χ(x,t))/c² · ∂²_t A − ∇²A = 0.**

Eikonal limit (A = a e^{iφ}, ω = −∂_t φ, k = ∇φ), dispersion ω n(x,t) = c|k|,
ray Hamiltonian **H(x, k, t) = c|k| / n(x, t)**. Hamilton's equations give,
along a ray,

  d ln ω / dt = −∂ ln n/∂t ≡ −W(x, t).   (1)

W(x,t) is the local conditioning *rate*. Everything observable follows from
this one function.

## 3. Redshift and dilation are the same integral — b = 1 is an identity

**Redshift** (leading-edge photon, path parameter l, dl/dt = c/n ≈ c):

  ln(1+z) = (1/c) ∫ W(l, t_front(l)) dl.   (2)

**Inter-photon delay** (second photon, emitted Δt later, fully incoherent
with the first — no phase relation used, only the classical field χ):
its local slowness is n(l, t_front + Δt)/c, so

  d(Δt)/dl = [n(l, t_front+Δt) − n(l, t_front)]/c ≈ (Δt/c) · W(l, t_front)
  ⟹ d ln Δt / dl = W/c.   (3)

Equations (2) and (3) have the **same kernel**. Therefore

  **Δt_obs = Δt_em · exp[(1/c)∫W dl] = (1+z) · Δt_em,  b ≡ d lnΔt_obs/d ln(1+z) = 1**

identically — not fitted, not tuned, independent of the magnitude, spatial
profile, or microphysical origin of W. Both observables are two readings of
the single function ∂ln n/∂t; the coefficient cannot differ from 1 within
the wave equation. (This is precisely how FLRW gets b = 1: the comoving wave
equation carries a(t) as an effective index, and redshift and dilation are
two derivatives of the same a(t). The wake reproduces the structure locally
and transiently instead of globally and secularly.)

What *can* break b = 1 is only photon-number change at scattering vertices
(crest creation/destruction) — and White et al.'s b = 1.003 ± 0.005 already
bounds that fraction at f < 0.025 (WAKE_COEFFICIENT.md). The theory-side
requirement is crest conservation in the forward vertex; the measurement
says nature enforces it to 2.5%.

Note what the derivation does **not** use: mutual coherence of the two
photons. The corridor field χ is the bookkeeper between them. The referee's
independent-photon framing is fully respected.

## 4. The response function is over-determined by data (the microphysical target)

Naively one would write ∂χ/∂t ∝ I(t) (excitation proportional to drive).
**Observations exclude that**, and in doing so they pin the required response
sharply:

- **C1 — K is universal** (the Hubble law does not correlate with source
  luminosity): W cannot scale with beam intensity. The response is
  *rate-saturated*: illumination switches the conditioning on; the medium
  then relaxes at its own intrinsic rate W = K ≈ H₀, set by vacuum
  properties (the number QFD owes from β), not by the drive.
- **C2 — line redshift is epoch-independent through the light curve**: W is
  constant over the burst duration at each corridor point (eq. 1 would
  otherwise make z vary with light-curve phase).
- **C3 — dilation is shape-preserving** (White's template fits; b = 1.003 ±
  0.005 with no fluence-weighted time warping): confirms W ≠ W[I(t)] —
  an energy-proportional wake would remap time by cumulative fluence and
  distort light-curve shape, which is not seen.
- **C4 — achromatic**: W is frequency-independent (the achromaticity test,
  run and passed on line redshifts).
- **C5 — no blur**: see §6.
- **C6 — finite memory**: the conditioning must persist between photons
  (relaxation slower than the burst: T_relax ≫ months) and must saturate
  (χ cannot grow without bound in an eternal universe): W → 0 after a
  saturation time T_sat under continuous illumination.

C1–C4 say the coupling is **reactive/parametric** — a phase-type response
whose *rate* is a medium constant — not absorptive/energy-proportional. C6
yields the wake's unique falsifiable prediction: **steady sources sit at
saturation and under-dilate** (quasar variability: Hawkins' non-dilation vs
SNe's b = 1 becomes a prediction rather than an anomaly, subject to the
Lewis & Brewer dispute). A transient SN burst rides the linear-growth window
(months ≪ T_sat); a quasar that has conditioned its corridor for millennia
does not.

**The owed microphysics is now a narrow target**: derive from the QFD vacuum
action a response with W = K universal, reactive, achromatic, with
T_relax ≫ 10⁷ s and finite T_sat. That is a specification, not a blank
check — most couplings one could write down fail C1 or C3 immediately.

## 5. Magnitudes

K ≈ H₀ = 2.2×10⁻¹⁸ s⁻¹. Over a rest-frame burst window of ~60 d
(5×10⁶ s), the accumulated index change at any corridor point is
Δn ~ K·Δt ~ 10⁻¹¹ — eleven orders below unity. Energy bookkeeping: the beam
deposits (K/c)·u_beam per unit length into χ; the wake energy density is
correspondingly minute and rejoins the bath ledger (DA_TOLMAN_DERIVATION.md
§6) on relaxation.

## 6. No transverse dispersion, no blur — by symmetry, then by sign

- The conditioning is sourced by the source's own expanding light front, so
  χ is (statistically) spherically symmetric about the source. For a radial
  ray, ∇⊥n = 0 **by symmetry**: zero deflection to first order. Each source
  pixel's light rides its own corridor; image geometry is untouched.
- At second order, any residual transverse profile has n *maximal* on the
  lit corridor — a graded-index structure that weakly **self-guides**
  (focuses) rather than scatters. The failure mode the referee fears
  (defocusing blur) has the wrong sign.
- Chromatic blur requires dispersion; W is frequency-independent (C4), so
  the delay is achromatic and pulse shapes are preserved (consistent with
  the ξ = 0 dispersionless protection and the EGG-33 sharpness budget,
  θ_rms < 10⁻¹² rad, which constrains the *non-forward* channel).
- Note the contrast with the reviewer-sketched route v_g = v_g(ν(x)): a
  frequency-dependent group velocity **is** dispersion and is excluded by
  C4/sharpness. The correct object is time-dependence behind the front,
  n(l, t − t_front), not frequency-dependence.

## 7. Status

| item | status |
|---|---|
| independent-photon Δt_obs = (1+z)Δt_em | **derived** from the wave equation; b = 1 is an identity in W |
| coefficient freedom | none within the wave equation; only vertex crest change, bounded f < 0.025 |
| memory mechanism | corridor excitation deposited by the inelastic forward loss (the same event as the redshift) |
| transverse dispersion / blur | zero by symmetry; residual is self-guiding (wrong sign for blur) |
| microphysical derivation of W = K, T_relax, T_sat from β | **owed** — but now a six-constraint specification (C1–C6) |
| unique prediction | steady-source under-dilation (quasars at saturation) |

This discharges the referee's demand at the effective-field level: the wave
equation is written, the memory is identified with the inelastic deposit
that *is* the redshift, b = 1 follows as an identity, and image sharpness
survives by symmetry and sign. What remains owed is one level deeper — the
vacuum-Lagrangian derivation of the response constants — and it is now
constrained by six data-derived conditions rather than being free.
