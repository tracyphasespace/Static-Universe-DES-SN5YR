# V7 freeze checklist — four edits, then stop and circulate to humans

**Session:** 2026-08-20 (late). Adjudicates the final skeptic review of V7
(DOI 10.5281/zenodo.22031627) and the stopping-rule recommendation, with
two data corrections that change Edit 1. After these four edits the paper
contains an explicit incompleteness, not a self-contradiction — the
correct state for human circulation. **No further synthetic-referee
cycles after this.**

Data anchors verified this session (producer commands in-line):
- **T_CMB(z) drift check:** CO excitation at z = 2.418 measures
  T = 9.15 ± 0.7 K (Noterdaeme et al. 2011); Face-1 drift predicts
  T₀(1+z) = 9.31 K — **0.2σ, zero parameters**. A stationary bath
  predicts 2.725 K at all lookbacks — excluded at ~9σ. SZ cluster
  measurements agree at other redshifts.
- **21cm cutoff kill:** a thermal IR cutoff K(ν) = K₀[1 − e^(−hν/kT)]
  gives K/K₀ = 0.025 at 1.42 GHz; 21cm absorber redshifts match optical
  to ~10⁻⁵ → any cutoff protecting the CMB band is already falsified.

---

## Edit 1 — CMB bath: drifting self-similar solution, not a static fixed point

**Location:** §3.1 ("Face 1 acts on every photon"), the energy section
(Eq. 37–38 region), Table 1 CMB row.

**Change:** adopt the reviewer's collision-operator *form* but not their
fixed-point condition. The bath is not C[f_eq] = 0 stationary — the
T_CMB(z) data above exclude that. Face 1 drives the isotropic bath along
the **self-similar drifting Planck solution**: d ln ν/dt = −K for every
photon — which *predicts the measured T_CMB(z) = T₀(1+z) relation with
zero parameters* — accompanied by a required photon-number relaxation
d ln n_γ/dt = −3K that preserves Planck shape (the role volume dilution
plays in FLRW). The number process is **not identified in this paper**;
its required properties are stated: broadband, low-frequency-weighted,
rate 3K, shape-preserving, and it must not attenuate directed beams
observably. The 20×-starlight "drain crisis" dissolves under this
framing: the bath is not maintained, it drifts — and the T(z) data
confirm exactly that drift rate. FIRAS's absolute normalization today is
then the constraint on the number process, not on the drift.

**Explicitly disown the IR-cutoff escape** (21cm kill above) — one
sentence, so no referee proposes it.

**Table 1:** CMB row goes **red**: "active theoretical barrier — number
relaxation at rate 3K owed; T(z) relation predicted and confirmed
(9.31 K vs 9.15 ± 0.7 K at z = 2.418); FIRAS normalization conditional
on the owed process; acoustic/BAO structure unaddressed."

**Acceptance test:** manuscript states the T(z) prediction with
citation; contains no stationary-bath claim; cutoff disowned; row red;
"equilibrium bath" wording removed in favor of "drifting bath +
number relaxation."

## Edit 2 — the wake is a direction-resolved susceptibility, not a scalar index

**Location:** Eq. 7 (n_g(ξ)), Eq. 13 (switch S), §3.2 terminology
throughout.

**Change:** χ = χ(x, k̂, t) — a **direction-resolved reactive
susceptibility** (phase-space transport memory), with
n_g(x, k̂, t) = 1 + χ(x, k̂, t) defined only as the one-ray
characteristic. All derived phenomenology (D = (c/K)ln(1+z),
Δt_obs = Δt_em(1+z)^κ_r) is unchanged — it was always a one-ray
calculation. What changes is what the microscopic theory owes (an
angular-memory transport response, not a local scalar field) and what
the model no longer suffers: cross-talk between overlapping transients
*and* deflection by foreign corridors both vanish, because a foreign
source's χ lives in a foreign k̂ cell. QFD-native remark (author's
geometric-product point, correctly scoped): the field-overlap geometric
product (direction ⊗ polarization) selects the activated cell; **the
rate within an activated cell remains the universal K** — overlap
density must not modulate the Face-1 rate, or the luminosity-independent
distance law dies (a z = 1 beam at mid-path is ~13 orders less dense
than the CMB).

Replace the Heaviside switch with the generic form
∂ₜχ_k̂ = R[δf_k̂] − χ_k̂/T_relax and label the Heaviside version an
existence sketch. Note the sketch's own testable corollary before
retiring it: a strict δI > 0 switch would under-dilate nebular-phase
light; nebular aging data can constrain R.

**Acceptance test:** the words "refractive index" no longer describe the
wake as a bulk medium property; the phase-space object is named; the
switch is labeled a sketch; the cell-selection vs rate distinction is
stated.

## Edit 3 — κ_r accounting

**Location:** §3.2, Table 1 timing row, §14 parsimony text.

**Change:** Table 1 row — FLRW: "b = 1, predicted"; static: "b = κ_r,
empirically constrained ≈ 1; microscopic equality to unity open."
Remove any sentence crediting the timing sector as parameter-free.

**Acceptance test:** the row reads as above; §14 contains no timing
parsimony credit.

## Edit 4 — quasars: withdraw under-dilation, adopt the bandwidth constraint

**Location:** the quasar paragraph and its Table 1 row.

**Change:** lead with Brewer et al. 2025 (n = 1.14 ± 0.34, robust to
modeling choices) rather than Hawkins 2010. **Withdraw the generic
steady-source under-dilation prediction** — a quasar's variability is
fluctuations δI(t) about a saturated DC mean, and a directional response
to δI can track the AC component while the DC stays saturated; this is
also what preserves the sourcing-trilemma answer (ambient DC saturated).
Quasar dilation therefore *constrains the response's bandwidth,
saturation, and relaxation* (memory over rest-frame decades:
T_relax ≳ 30 yr) rather than killing it. **Knock-on to log honestly:**
retiring under-dilation removes the wake-vs-conformal-n(t) timing
discriminator; the surviving discriminator between this model and a
Gordon-metric relabeling is the geometric sector — d_A = D and the
(1+z) duality ratio vs conformal (1+z)². Tolman and duality now carry
that burden alone.

**Acceptance test:** withdrawal sentence present; 2025 citation leads;
bandwidth-constraint sentence present; the discriminator hand-off to the
geometric sector stated.

---

## Then freeze

Do **not** wait for: the QFD collision operator, the CMB acoustic
spectrum, the Tolman re-reduction, static-BBC, a quasar
transfer-function fit, the APD experiment, or a galaxy-evolution model.
After the four edits every remaining open item has the same form — "can
a microscopic QFD transport theory realize the effective response the
phenomenology requires?" — which is a question for human physicists,
not another synthetic pass.

**Human circulation questions (targeted, not 'find another flaw'):**
1. *Kinetic/nonlinear-optics theorist:* can a passive or driven medium
   support a phase-space response with the drifting-Planck bath solution,
   directional memory, and narrow-beam relaxation rate K, without
   excessive dispersion or noise?
2. *CMB/cosmology expert:* assuming this effective transport operator,
   which existing CMB/BAO/lensing observation kills it first, and can
   that test be expressed independently of ΛCDM parameter fitting?
3. *Supernova observer:* are the DES Hubble, b, color, T4 and Tolman
   tests represented correctly, and what existing dataset gives the
   cleanest model-vs-FLRW discriminator?

One research task proceeds in parallel without blocking circulation:
the preregistered Tolman reduction (Branches Z and E, plus the direct
comparison against L&S's own published tired-light computation — added
to the registration).
