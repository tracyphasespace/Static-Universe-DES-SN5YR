# The forward-channel energy ledger and the FIRAS thermalization bound

**Session:** 2026-08-20. Closes the gap both Draft-6 reviews correctly
identified: the energy ledger covered the non-forward channel's 16%
(by z = 1) but not the **forward channel's z/(1+z) — 50% of the entire
beam energy at z = 1 — deposited into the medium**. In FLRW that line
reads "expansion work" and needs no destination; here it does. This note
supplies the flow accounting and the one sharp number it produces.

## 1. No unbounded sink

The deposition does not accumulate in χ: the wake is transient
(saturation + relaxation, requirement C6), so the corridor is a
*conduit*, not a reservoir. Energy flows photon → vertex → wake →
(relaxation) → the diffuse microwave bath. The question is whether that
flow is consistent with the observed bath.

## 2. The magnitudes (verified computation)

- u_CMB = aT⁴(2.725 K) = 4.17×10⁻¹³ erg cm⁻³.
- Ambient starlight (EBL, optical+IR ≈ 50 nW m⁻² sr⁻¹):
  u_opt ≈ 2.1×10⁻¹⁴ erg cm⁻³.
- Forward-channel deposition rate: u_opt·K ≈ 4.8×10⁻³² erg cm⁻³ s⁻¹
  (K = H₀ = 2.27×10⁻¹⁸ s⁻¹) — i.e. **the forward channel feeds the bath
  ≈ 5.0% of u_CMB per Hubble time**. The non-forward channel adds a
  fraction of u_opt on top; same order.

Five percent per Hubble time is *not* hideable as a small perturbation.
In the eternal-equilibrium framing it need not hide: it is a steady
throughput, balanced within the bath's equilibrium. What FIRAS then
constrains is not the flow itself but **how un-Planckian the in-transit
energy is allowed to be**.

## 3. The FIRAS bound → a thermalization-time requirement

In steady state, the non-thermalized fraction of bath energy is
(injection rate × thermalization time)/u_CMB. FIRAS's chemical-potential
limit μ < 9×10⁻⁵ therefore requires

  **t_therm < μ · u_CMB / (u_opt·K) ≈ 7.9×10¹⁴ s ≈ 25 Myr ≈ 2×10⁻³ t_H.**

This is the quantitative content of D-K gate 2, now with a number: the
wake-relaxation products must thermalize to the Planck bath within
~25 Myr, i.e. the vacuum medium's photon-photon/mode-mixing
thermalization rate must exceed the injection rate by ≳ 500×. That is a
sharp, falsifiable demand on the same microphysics that owes W = K —
one derivation must deliver both, or the model fails FIRAS.

Corollaries already in the record, restated here as parts of one ledger:
- **No optical/IR reappearance**: the cascade must leave the optical
  band promptly (zero redshift-correlated PSF wings — EGG-33; no EBL
  excess), so the flow's only observable face is the microwave bath.
- **CMB scope statement (Draft 6.1)**: the transfer operator applies to
  localized sources seen through the bath; the CMB itself is claimed as
  the equilibrium bath, *not* as redshifted surface radiation — which is
  why the (1+z)² radiance excess of Eq. 26 does not apply to it. The
  cost of that claim is exactly the D-K gates, of which the 25 Myr
  thermalization bound above is now the most concrete.

## 4. Draft 6.1 actions from this note

1. §8: add the forward-channel line ΔE/E = z/(1+z), the 5%/t_H flow,
   and the 25 Myr thermalization bound as an explicit falsification
   gate.
2. Scope paragraph: transfer operator = localized sources; CMB =
   equilibrium bath (stated, with the D-K debt named).
3. Falsification table: new row — "FIRAS μ vs forward-channel
   throughput: passes only if t_therm < 25 Myr; derivation owed."
