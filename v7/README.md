# V7 — canonical claim-to-source map

**Paper:** *A Static-Universe Two-Channel Photon Propagation Model
Confronted with DES-SN5YR* (T. McSheery, **Version 7.0 — standalone
post-review synthesis**, 20 August 2026), DOI
[10.5281/zenodo.22031627](https://doi.org/10.5281/zenodo.22031627).
PDF: [`../paper/Static_Universe_DES_SN5YR_V7_Zenodo.pdf`](../paper/Static_Universe_DES_SN5YR_V7_Zenodo.pdf)
(SHA-256 `a1e6bd74c4faf13b9a2482f14bc1518287bd5994325ed66f5b3df00ee246624f`,
verified against the Zenodo deposit). Prior records preserved as
provenance: Draft 6 (10.5281/zenodo.22031121), Draft 5
(10.5281/zenodo.22025329), both PDFs kept in `../paper/`.

V7 is standalone: a reviewer needs none of the prior drafts. Its key
structural change: the forward vertex is explicitly **two-faced** — an
always-on coherent inelastic frequency-shift face and a transient
reactive group-delay face — and the temporal law is written
Δt_obs = Δt_em·(1+z)^{κ_r} with **κ_r ≃ 1 measured** (DES/White);
the equality of the timing and redshift rates is the thing the
microscopic theory must derive, not an assumption hidden in an
"identity."

## Physics provenance (canonical for V7)

| V7 content | provenance source |
|---|---|
| Two-faced vertex; sourcing trilemma resolution; traveling-wake solution n = 1 + K(t − r/c); Gordon-metric disposition; stationarity fork; static lookback t_lb = K⁻¹ln(1+z) | [`../draft6/docs/WAKE_CONSISTENCY.md`](../draft6/docs/WAKE_CONSISTENCY.md) |
| Forward-channel 50% energy loss at z = 1; 5% of u_CMB per Hubble time throughput; FIRAS t_therm ≲ 25 Myr gate | [`../draft6/docs/FORWARD_ENERGY_LEDGER.md`](../draft6/docs/FORWARD_ENERGY_LEDGER.md) |
| d_A = D; duality (1+z); Tolman n_eff; τ∞,B = 0.594; radiance excess; raw c(z) = −0.096 ± 0.014 (selection-gated) | [`../draft6/docs/DA_TOLMAN_DERIVATION.md`](../draft6/docs/DA_TOLMAN_DERIVATION.md), producer `../draft6/src/rawframe/da_tolman.py` |
| Passband-artifact self-falsification (≤ 0.05% stretch, ≤ 0.05 d peak shift); phase-flat Q(z) = 0.979/0.964/0.944; Tolman frame-shift (n_I → 2.30 ± 0.13, n_R → 1.45 ± 0.17; 3.7σ frame-invariant band spread) | `../draft6/src/rawframe/transfer_integral.py`, `../draft6/src/rawframe/tolman_frame_shift.py`, [`../draft6/docs/SPECTRAL_CLOCKS.md`](../draft6/docs/SPECTRAL_CLOCKS.md) |
| T4 executed result: b₂ = 0.52 ± 0.78, N = 120, inconclusive | [`../draft6/docs/T4_RUN_REPORT.md`](../draft6/docs/T4_RUN_REPORT.md), registration [`../draft6/prereg/secondary_maximum_phase.md`](../draft6/prereg/secondary_maximum_phase.md), **frozen output: [`results/t4_secondary_max.json`](results/t4_secondary_max.json)** (SHA-256 `1670c4c9071d25cf88ae8ead3c01a5369c851175d297d051a31aeb016ca9a90c`) |
| Tolman reduction plan, Branch Z (zero-evolution, as registered) + Branch E (static-lookback evolution, pre-reduction amendment) | [`../draft6/prereg/tolman_static_reanalysis.md`](../draft6/prereg/tolman_static_reanalysis.md) |
| Hubble diagram Δχ² = +1.1; BBC leverage (methods layer) | [companion methods repo](https://github.com/tracyphasespace/Model-Discrimination-DES-SN5YR), CI-verified |

## Supersession and status notes

- [`../draft6/docs/WAKE_FIELD_FORMULATION.md`](../draft6/docs/WAKE_FIELD_FORMULATION.md)
  is **historical/superseded**: its single-kernel presentation ("b = 1 is
  an identity") is replaced by the two-faced vertex with κ_r = 1 as the
  measured coefficient whose microscopic derivation is open. Preserved
  unmodified as part of the Draft-6 record.
- `../draft6/` is a **chronological record** of the Draft-6 cycle
  (2026-08-20). Execution language inside those files ("run T4 next",
  etc.) reflects the state at writing; current status lives here and in
  the V7 paper's own ledger.
- Open debts as stated in V7: the single vertex response function from
  the QFD vacuum action (four constraints, one function: universal
  absorptive K; reactive ramp with κ_r = 1; t_therm ≲ 25 Myr; bath
  anisotropy structure incl. acoustic peaks/BAO correlation), the
  static-frame Tolman reduction, static-BBC selection modeling, and the
  global-evolution / stationarity fork consequences.
