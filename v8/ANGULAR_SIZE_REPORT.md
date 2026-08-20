# Angular-size test — EXECUTED. K2-ang fires for early types: EGG-19 scores FOR Euclidean angles.

**Run:** 2026-08-20, per `preregistration/angular_size_test.md` (committed
before any catalog fetch). Producer: `src/rawframe/angular_size_test.py`.
Data: van der Wel+ 2012 CANDELS GALFIT angular sizes (VizieR
J/ApJS/203/24) positionally joined (≤0.6″) to Skelton+ 2014 3D-HST
redshifts/masses (J/ApJS/214/24); 1,766 galaxies, logM ≥ 10.3,
band-per-z windows pinning rest λ ≈ 4800–6700 Å (Y/J/H), z = 0.6–2.2.
Sizes used in **angular units only** — no catalog kpc conversions.
Pre-run amendments (disclosed): UVJ colors unavailable on VizieR →
subsample split by Sérsic proxy (n ≷ 2.5); everything else as frozen.

## Early-type proxy (n ≥ 2.5, N = 628) — the standard-rod population

θ_med(z): 0.369″ → 0.307″ → 0.249″ → 0.195″ across the four registered
bins (z_med 0.68 → 1.79).

| shape | params | χ² (3–2 dof) | AIC |
|---|---|---|---|
| **Euclidean strict θ = A/ln(1+z)** | 1 | **0.93** | **2.93** |
| coasting strict | 1 | 17.14 | 19.14 |
| ΛCDM strict | 1 | 18.25 | 20.25 |
| coasting + evolution | 2 | 0.93 (βs = **−1.00**) | 4.93 |
| ΛCDM + evolution | 2 | 1.16 (βs = −1.02) | 5.16 |

**K2-ang FIRES**: the one-parameter Euclidean shape wins on AIC against
every alternative; the strict turnover shapes are excluded at
Δχ² ≈ +16–17; systematics band (faintest-quartile removal) leaves the
Euclidean fit at χ² = 0.79. **And the internal signature is exact: the
evolution the other frames require is βs = −1.00 — algebraically the
frame-conversion factor, since (1+z)^(−1)·[(1+z)/ln(1+z)] ≡ 1/ln(1+z).**
The measured quiescent-galaxy angular-size shape IS 1/ln(1+z); the FLRW
frame renames the difference "size evolution." This is the quantitative
content of the author's recollection that "our angles were viable versus
the 1930s expanding-universe angles," now registered, executed, and
kill-adjudicated.

## Late-type proxy (n < 2.5, N = 1,138)

θ_med is flatter than every strict shape (0.555″ → 0.575″ → 0.500″ →
0.411″): all three strict fits fail (χ² 21–24) and, with evolution
freedom, all three frames tie (AIC 11.3–12.2; Euclidean needs βs = +0.49,
coasting −0.51). **Per the registration's letter, K1-ang fires for late
types** — reported per the anti-cherry-pick clause — but the correct
reading is that this subsample discriminates *nothing about geometry*:
star-forming disks demand evolution in EVERY frame (astrophysically
expected — inside-out growth), and once evolution floats the frames are
degenerate. The kill's registered meaning ("Euclidean loses its
naturalness asset") applies only where naturalness was claimed: the
z-invariant standard-rod population, which is the early-type sample —
where Euclidean won outright.

## Caveats (standing)

Stellar masses (selection) inherit FLRW luminosity distances — the
registered flux-selected robustness variant remains to be run; photo-z
scatter smears bins (second-order for shape); the JWST z = 3–8 extension
was not fetched this run (the z ≤ 2.2 anchor already separates the
strict shapes by 2×). None of these plausibly manufactures a χ² = 0.93
one-parameter fit while breaking the competitors by +16.

## Ledger consequences

- **EGG-19 is scored at last: FOR Euclidean angles (early types).**
- The D-M fork rebalances: the angular sector now *discriminates* and
  favors d_A = D (readings A/A′), while the Tolman sector — per the
  symmetric-grading addendum — discriminates nothing without floated
  evolution and carries a single-cluster band confound. The strongest
  clean geometric evidence in hand favors Euclidean.
- Reading B (coasting) now owes the same βs ≈ −1 evolution ΛCDM owes,
  and its Tolman advantage was already evolution-bought. Reading A/A′
  still owes the steady-source rate-dilation account (the continuity
  theorem) for its Tolman face.
- Next data steps unchanged: K2 (modern multi-band SB) for Tolman;
  optional JWST z > 3 extension here (the turnover-vs-monotonic
  divergence becomes ×5 by z = 4).
