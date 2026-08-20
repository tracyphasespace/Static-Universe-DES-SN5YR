# Wake consistency: the explicit solution, the Gordon-metric question, and the front/trailing bookkeeping

**Session:** 2026-08-20, post-Draft-6 review adjudication. Input for the
Draft 6.1 §3.2 revision. Two referees have now asserted that the wake
requires the refractive index to grow to n = 1+z along the photon path,
breaking the distance law and reducing the model to a conformal
(Gordon-metric) relabeling of expansion. **The first half of that claim is
a mathematical error; the second half is a legitimate question with a
falsifiable answer.** Both belong in the paper.

---

## 1. The explicit solution (refutes n → 1+z)

The claim: "the redshift is ∫∂ₜ ln n dt ≈ ln(1+z) along the trajectory,
and ∂ₜ ln n is evaluated at the photon's position, so the index at the
front must rise from 1 to (1+z)." This conflates the **Lagrangian
integral of a partial time derivative along a moving trajectory** with
the **Eulerian change of the field at a point**. Counterexample — the
wake's actual form, a traveling transient profile:

  n(x, t) = 1 + K·(t − x/c)  for 0 < t − x/c < t_burst,  relaxing after.

Check every assertion against this solution:

- **At the front** (t = x/c): n = 1 identically, for the entire journey.
  Hence dl = c·dt holds exactly and **D = (c/K)·ln(1+z) is untouched**.
  The alternative D = (c/K)·z/(1+z) never arises.
- **Along the ray**: the photon samples ∂ₜ ln n = K at every point of
  passage and accumulates ∫K dt = K·t_journey = ln(1+z) — order unity
  over 10¹⁷ s. Redshift: correct.
- **At any fixed point**: n rises only while the burst passes,
  Δn ≈ K·t_burst ~ 10⁻¹¹, then relaxes. **Light arrives at the observer
  through n = 1 + O(10⁻¹¹), not n = 2.** No line-of-sight or
  epoch-dependent c variation at any observable level.

The photon integrates W for 10¹⁷ seconds; each medium point holds W for
~10⁷ seconds. An order-unity accumulated redshift and a 10⁻¹¹ index
excursion are simultaneously true. This box goes in Draft 6.1 verbatim —
the error is seductive and will recur in review.

## 2. The Gordon-metric question (legitimate — answered by an observable)

The serious version of the objection: a **spatially uniform, secularly
growing** index n(t) ∝ e^{Kt} is, via Gordon's optical metric, exactly an
FLRW scale factor a(t) = 1/n(t) — expansion in refractive language. If
the wake were that, the model would be a relabeling.

It is not that, and the difference is observable:

- The wake is **corridor-local and transient**: χ grows only during an
  illumination *transient* and relaxes after; under steady illumination
  it saturates (∂ₜχ → 0). The spatial/temporal mean of n is 1 + O(10⁻¹¹)
  with **zero secular growth** — there is no global a(t).
- **The discriminating observable**: a conformal a(t) time-dilates
  *everything*, including the variability of steady sources. A transient
  wake dilates only transients riding their own conditioning window;
  steady sources sit at saturation and **under-dilate**. Quasar
  variability (the Hawkins non-dilation claim vs Lewis & Brewer) is
  therefore not an anomaly to survive but the *distinguishing
  prediction*: b_SN = 1 with b_quasar < 1 is impossible in FLRW and in
  any Gordon-equivalent n(t), and generic for the wake.
- Because ⟨n⟩ = 1, the geometry stays Euclidean: d_A = D, the duality
  ratio (1+z), and the Tolman exponent derivations stand as derived —
  they need no conformal re-derivation.

## 3. Front/trailing bookkeeping (the paper's real §3.2 gap)

Draft 6.0 presents one kernel W doing everything, which invites the
causality objection ("what conditions the corridor before the front?").
The consistent two-level structure, to be stated explicitly in 6.1:

1. **Redshift is vertex-level.** Every photon — front or trailing —
   loses energy at the medium-set rate K through the inelastic forward
   vertex (the same event that deposits the wake). This requires no
   pre-conditioning and no self-action: K is a medium constant
   (requirement C1), not a response to the beam.
2. **Timing is corridor-level.** The deposited excitation is, for
   *later* photons, an effective index n(x,t); the inter-photon delay
   integrates Δn = K·Δt. The index description and the vertex description
   are the same energy deposition viewed from the two sides — used for
   timing and for redshift respectively, never summed (no 2K
   double-count).
3. **b = 1 status, stated precisely**: within the effective wave
   equation, redshift and delay share the kernel and b = 1 is an
   identity. The physical condition that the index growth rate equals
   the vertex drag rate (the reactive-coefficient-unity /
   crest-conservation condition) is the microphysical input, and it is
   *measured*: White's b = 1.003 ± 0.005 bounds any violation at
   f < 0.025. Draft 6.1 abstract wording: "consistent with b = 1 by
   construction, with the coefficient's microphysical derivation open"
   — per the reviewer's suggestion, adopted.

## 4. Adopted refinements (third review, 2026-08-20)

**4a. The cleaner statement of §1** (replaces the prose argument in
Draft 6.1): at the front, r = ct, so along the actual trajectory

  dn/dt = ∂ₜn + ṙ·∂ᵣn = K + c·(−K/c) = **0**.

The front rides a surface of constant n = 1 while experiencing
∂ₜ ln n = K — the partial derivative (which redshifts) and the total
derivative (which is what the erroneous objection integrated) are
different derivatives. Experimental precedent that spatiotemporal
index fronts convert photon frequency without any global index change:
photon acceleration / moving-index-front experiments (e.g. optical
push-broom in Bragg waveguides). Existence of the *mechanism class* is
laboratory physics; what QFD owes is the specific vacuum realization.

**4b. Minimal kinetic closure** (the "minimal form satisfying C1–C6"
both reviews asked for — an effective kinetic equation, explicitly NOT
yet a Lagrangian): with n = 1 + χ/2,

  ∂ₜχ = 2K · H[I(x,t)] · H[χ_sat − χ] − χ/T_relax,  χ(x, t < r/c) = 0,

with H a step (drive-saturated switch), T_relax ≫ t_burst, and
χ_sat/2K = T_sat. Behind a front this integrates to exactly Eq. A,
χ = 2K(t − r/c), during the unsaturated window; steady illumination →
saturation (under-dilation of steady sources); relaxation feeds the bath
(FORWARD_ENERGY_LEDGER.md). All six data-derived constraints are
satisfied by construction. **The open microphysics is unchanged in
content but now precisely located: derive this kinetic equation — the
intensity-independent rate 2K tied to the drag vertex, T_relax, and
χ_sat — from the QFD vacuum action (the W = K from β debt).** Until
then the wake is kinematically consistent and kinetically modeled, not
derived; Draft 6.1 should say exactly that.

## 5. Lookback time and the stationarity fork (new — and all three reviews missed half of it)

The galaxy-age objection ("static = no lookback time") is wrong as
stated: light travel time gives **t_lb(z) = D/c = K⁻¹·ln(1+z)** from the
model's own distance law. But finite lookback produces a *systematic*
age–z trend only if the universe evolves globally on ~1/K timescales.
A strictly stationary eternal ensemble shows the SAME population at
every lookback — galaxies age individually, the ensemble does not (this
is what killed classical steady state, and it cannot be waved at). The
model must therefore choose a fork, explicitly:

- **Fork A — strict stationarity:** the observed Balmer/fundamental-
  plane aging at z ~ 0.5–0.9 stays an adverse observation, full stop.
- **Fork B — static geometry, secularly evolving contents:** aging over
  t_lb is natural. The rest of the structure survives: with
  t_therm < 25 Myr the bath tracks sources adiabatically, so FIRAS
  Planckness needs fast kinetics, not eternity; wake saturation is
  corridor-local and indifferent. Cost: the model gives up "no cosmic
  clock" and inherits a synchronization/age question comparable to
  ΛCDM's t₀. Gain: a new discriminator — does measured stellar aging
  follow K⁻¹ln(1+z) or the FLRW lookback? (≈20% different at z ~ 0.9,
  strongly divergent at high z), and the unbounded static lookback
  (34 Gyr at z = 10) dissolves rather than worsens the JWST
  early-massive-galaxy tension — flagged for development, not claimed.

Draft 6.1 should adopt Fork B openly or defend Fork A; silence invites
the steady-state objection with its historical force.

## 6. Disposition of the two reviews' Issue-1 bullets

| assertion | verdict |
|---|---|
| n at front reaches 1+z; D(z) becomes (c/K)z/(1+z) | **wrong** — §1 explicit solution |
| observer receives light through n = 2; c varies observably | **wrong** — §1; n − 1 ≤ 10⁻¹¹ everywhere |
| time-growing uniform n(t) = Gordon/FLRW relabeling | **right as a trap, avoided**: no secular ⟨n⟩ growth; discriminator = steady-source under-dilation (§2) |
| "front acts on itself or corridor pre-conditioned" | **resolved** by the vertex/corridor split (§3): front redshift is vertex-level, needs no conditioning |
| what is n measured against | local vacuum standards; n − 1 ≤ 10⁻¹¹ makes all laboratory standards trivially unaffected |
