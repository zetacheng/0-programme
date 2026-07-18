# Cross-Paper Dependency Registry

| Dependency ID | Upstream paper | Upstream claim | Upstream result | Upstream gate | Downstream paper | Downstream use | Downstream gate | Status | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| PD-001 | Paper 5 | P5-CL-003 | `kappa_U = -17/(1152 pi^2)` | `paper-owned:5-topological-sector#P5-C2A-03`; `paper-owned:5-topological-sector#P5-C2A-04` | Paper 4 | `S_mono = 640 kappa_U`. The arithmetic is Paper 4's; the input coefficient belongs to Paper 5. | `paper-owned:4-dark-energy-cosmology#P4-MONOPOLE-01` | ACCEPTED | Paper 5 P5-CL-003 is `VERIFIED`; Paper 4's unmerged v6.3 migration record gives `S_mono = -85/(9 pi^2) = -0.95` and closes the route negatively. |
| PD-002 | Paper 3 | P3-C-001 | `G_omega = -G/N` from the U(3) Fierz gate | `paper-owned:3-vector-sector#P3-FIERZ-01` | Papers 2 and 5 | Paper 2 Finding 2 retraction and Paper 5 P5-CL-014: cross-channel ratios are Fierz-inherited. | — | ACCEPTED | Paper 3 P3-C-001 is `VERIFIED`; Paper 2 v2.15 and Paper 5 v0.23 quote the convention correction; P5-CL-014 is `FAILED`. |
| PD-003A | Paper 3 | P3-C-005 | Omega exists, has healthy kinetic and mass terms, and supplies a repulsive static kernel. | `paper-owned:3-vector-sector#P3-VEC-O3`; `paper-owned:3-vector-sector#P3-OMEGA-01` | Paper 5 | Input to the continuum-stabilization gate. Upstream result is accepted; the tested downstream stabilization use failed. | `paper-owned:5-topological-sector#P5-OMEGA-01` | FAILED | Paper 3 P3-C-005 is `VERIFIED`; PF-006 and the legacy `topo-mass-radius` verdict record the failed downstream use. |
| PD-003B | Paper 3 | P3-C-005 | Omega exists, has healthy kinetic and mass terms, and supplies a repulsive static kernel. | `paper-owned:3-vector-sector#P3-VEC-O3`; `paper-owned:3-vector-sector#P3-OMEGA-01` | Paper 2 | Possible positive species contribution to the induced-gravity budget. | — | PROPOSED | Paper 3 P3-C-007 remains `PROPOSED`; Paper 2 v2.15 identifies the omega budget insertion as open and uncomputed. |
| PD-004 | Paper 2 | P2-C9 | `beta_V/beta_B = -3.2(5)` from lattice Finding 5 | `paper-owned:2-emergent-gravity#P2-BETAV-CIRC-01` | Paper 3 | Paper 3 v3.11 abstract quotes the number as decisive confirmation of the analytic sign reversal. | — | SUSPENDED | Paper 2's unmerged verification record leaves the full lattice reproduction open. The analytic target is structure-dependent, but the numerical pipeline has not been shown to discriminate. |
| PD-005 | Paper 4 | P4-CL-007 | `Lambda_DE` and the terminated monopole chain | `paper-owned:4-dark-energy-cosmology#P4-MONOPOLE-01` | Paper 1 | Proposed causal relation `a0 ~ Lambda_DE^2/M_Pl`. | — | FAILED | Paper 1 v16.3 restates the relation as a numerical coincidence owing nothing to the framework; P1-CL-010 is `RETIRED`. |

## `beta_V/beta_B` synchronization note

The Paper 2 independent-verification branch opened `paper-owned:2-emergent-gravity#P2-BETAV-CIRC-01`. The gate asks whether the lattice extraction genuinely distinguishes `-3.2(5)` from a value generated automatically by species counting.

A flat-space loop integral may be species-independent and could therefore return

\[
\beta_V/\beta_B=-3
\]

by construction. The current Paper 2 record finds that the analytic target is structure-dependent, `-(k+2)`, but the full curved-background lattice Proca pipeline has not been run. If the pipeline returns `-3` regardless of the supplied structure, Paper 2 Finding 5 is not an independent confirmation and Paper 3's abstract quotation must be revised.

Accordingly:

- the Paper 2 lattice confirmation is `SUSPENDED` at programme level;
- Paper 3 claim P3-C-004 remains `VERIFIED`;
- P3-C-004 rests on the analytic C6 sign structure, not on the lattice number `-3.2(5)`;
- the claim promotion is therefore not currently at risk.

## Status vocabulary

- `PROPOSED`
- `UNVERIFIED`
- `ACCEPTED`
- `SUSPENDED`
- `FAILED`
- `SUPERSEDED`

A downstream paper may not treat an upstream result as accepted unless the corresponding upstream gate is closed and accepted.
