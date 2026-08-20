# Lubin & Sandage 2001 source tables — provenance

Fetched 2026-08-20 from arXiv e-print sources (LaTeX, containing the
published deluxetables):
- `Sandage.tex`  = astro-ph/0102213 = Paper I  (AJ 121, 2271): local
  calibration — ⟨SB⟩–log R relations at five Petrosian η, R band,
  z = 0 zero points, nonlinearity corrections.
- `tolman3.tex`  = astro-ph/0106563 = Paper III (AJ 122, 1071): HST
  photometry of the three clusters (reference).
- `tolman4.tex`  = astro-ph/0106566 = Paper IV (AJ 122, 1084): per-galaxy
  M/⟨SB⟩/log R tables at q₀ = 1/2 (K-corrected), per-cluster summary
  tables (validation targets), and Table 8 conversion recipes INCLUDING
  the "Tired Light" column (ΔM, Δlog R) whose distance is identical in
  form to the static model's d_A = (c/H₀)ln(1+z) — verified: their
  Δlog R = 0.305 at z = 0.7565 vs our computed 0.3046.

Used by `src/rawframe/tolman_reduction.py` under
`preregistration/tolman_static_reanalysis.md` (Branches Z and E).
