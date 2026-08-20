# Pre-registration: the sigma-M* frame-free dynamical test

**Registered:** 2026-08-20, before fetching or inspecting any velocity-
dispersion values. Motivation: theta = R/D_A is exactly degenerate
between "large D_A, no evolution" and "small D_A, evolution"
(ADJUDICATION_2026-08-20B §3). Velocity dispersion sigma is
frame-free; it breaks the degeneracy.

## Physics

For pressure-supported galaxies M_dyn = K_v sigma^2 R_e / G (K_v ~ 5,
Sersic-dependent, frozen per Cappellari 2006 prescription). R_e = theta
* D_A is frame-valued; M* scales with d_L^2 (frame ratio <~ 20% at
z <= 2 in the Hubble-degenerate sector, applied explicitly). At
z = 1.5-2 the static D_A is ~2.0-2.3x LCDM's, so on the SAME measured
(sigma, theta, flux):

  (M_dyn/M*)_static ~= (D_A ratio) x (d_L ratio)^-2 x (M_dyn/M*)_LCDM
                    ~= 2.0-2.8 x (M_dyn/M*)_LCDM.

## Data (fetch after registration; schema-only first)

Published compact-quiescent samples with sigma at z ~ 1.4-2.2:
van de Sande et al. 2013; Belli et al. 2014/2017 (tables via
VizieR/journal); low-z anchor: local ETG M_dyn/M* within R_e
(ATLAS3D-class values, quoted from literature with IMF convention
stated).

## Estimator (frozen)

1. Per galaxy: M_dyn under each frame from the SAME (sigma, theta);
   M* re-scaled to each frame via its d_L. Output: distribution of
   M_dyn/M* per frame, per z bin ([1.3,1.7), [1.7,2.2]).
2. Statistic: median ratio per frame per bin with bootstrap errors;
   compared against the local median ratio (its dispersion carried).
3. Declared reading implications (committed now):
   - LCDM frame: ratio ~ local (~1.0-1.7 incl. DM+IMF) = the
     mainstream consistency.
   - Static frame: ratio must EXCEED local by the D_A ratio
     (~2.0-2.8x by z ~ 2), i.e. inner-R_e dark fractions rising to
     >~ 55-65% at z ~ 2 — opposite in sign to LCDM-frame findings that
     high-z compact galaxies are MORE baryon-dominated.
4. Kill condition K-sigma (pre-committed): if the static-frame required
   ratio exceeds the local ratio by > 3 sigma AND exceeds the maximum
   dynamically-modeled inner dark fraction admitted by the cited
   modeling literature (bound recorded from the papers BEFORE computing
   our numbers), then **Euclidean sizes + standard dynamics are jointly
   excluded**: the Euclidean reading survives only by abandoning
   standard virial dynamics — recorded as a kill of reading A/A' 's
   geometric sector unless an in-model dynamical account exists. If the
   static-frame ratio is within the modeled range, the degeneracy
   stands unbroken and is reported as such.
5. No-freedom clause; amendments labeled pre/post-data; anti-cherry-
   pick: both z bins and both frames reported together.
