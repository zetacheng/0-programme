# Global Claims Registry

| Global claim ID | Claim | Status | Owning repository | Owning claim ID | Owning gate | Affected downstream papers | Synchronization state | Evidence | Last reviewed |
|---|---|---|---|---|---|---|---|---|---|
| GC-001 | `kappa_U = -17/(1152 pi^2)` in the controlled limit | SUPPORTED | `zetacheng/5-topological-sector` | P5-CL-003 | `paper-owned:5-topological-sector#P5-C2A-03`; `paper-owned:5-topological-sector#P5-C2A-04` | Paper 4 | OWNER-VERIFIED / SYNC-PENDING: Paper 5 is accepted on `main`; Paper 4's dependent arithmetic is recorded only on an unmerged migration branch. | Paper 5 P5-CL-003 `VERIFIED`; independent C2a review; dependency PD-001; PF-001 and PF-003. | 2026-07-17 |
| GC-002 | `G_omega = -G/N` for the repulsive flavor-singlet vector channel | SUPPORTED | `zetacheng/3-vector-sector` | P3-C-001 | `paper-owned:3-vector-sector#P3-FIERZ-01` | Papers 2 and 5 | OWNER-VERIFIED / SYNC-PENDING: Paper 3 is accepted on `main`; Paper 2's retraction is unmerged and Paper 5 P5-CL-013 remains `PROPOSED`. | Paper 3 P3-C-001 `VERIFIED`; independent vector-sector review; dependency PD-002. | 2026-07-17 |
| GC-003 | `c_GW = 1` for the Goldstone-Wilczek normalization | VERIFIED | `zetacheng/5-topological-sector` | P5-CL-007 | `paper-owned:5-topological-sector#P5-GW-01` | Paper 3 | SYNCHRONIZED: Paper 5 owns and verifies the normalization; Paper 3's accepted C6 record uses it explicitly. | Paper 5 P5-CL-007 `VERIFIED`; Paper 3 P3-C-004 `VERIFIED`; independent reviews in both repositories. | 2026-07-17 |

The candidate `beta_V = -3 beta_B` is not entered as a global claim in this sweep because its owning Paper 2 claim P2-C3 is `SUPPORTED`, not `VERIFIED`, and exists only on an unmerged branch. Paper 3's separate analytic C6 claim P3-C-004 remains `VERIFIED`.

Allowed statuses are `PROPOSED`, `SUPPORTED`, `VERIFIED`, `CONDITIONAL`, `FAILED`, `RETIRED`, and `INCONCLUSIVE`.

Programme-level `VERIFIED` requires:

1. accepted upstream gate;
2. reproducible evidence;
3. independent review;
4. synchronization into every affected paper repository.
