# Repository Synchronization Status

Authoritative remote state inspected on 2026-07-17. A branch listed as unmerged is not current `main`, even when its scientific record is more complete than `main`.

| Paper | Repository | Main head | Inspected scientific ref | Paper version | Paper source | Progress, gates and claims | Claims audited | Conventions audited | Repository state | Last sync |
|---|---|---|---|---|---|---|---|---|---|---|
| Paper 1 | `zetacheng/1-dark-matter-structure` | `1a610213e388c885d52a15369a150fd8e4812d47` | `claude/paper1-gated-repo-governance-z478hp` at `8f5c63c1206b81a09df810c62ba92122d074ca38` (unmerged) | v16.3 | Present only on the unmerged governance branch as `paper/yukawa_sparc_paper_v163.tex` | Populated on the unmerged branch; `main` remains scaffolding | Unmerged ledger: P1-CL-001–008 `SUPPORTED`, P1-CL-009 `FAILED`, P1-CL-010 `RETIRED` | Repository conventions inspected on the unmerged branch; programme synchronization pending | Scientific record imported from `zetacheng/yukawa-sparc-fits` on the unmerged branch, but not yet authoritative on owning-repository `main` | 2026-07-17 |
| Paper 2 | `zetacheng/2-emergent-gravity` | `b92b6c1bf8a4a610cfa42f3f89de8740ae7bc386` | `claude/paper-2-independent-verification-dysdp0` at `de754ea6d7aff94c253b29bb80aea9ebb70cd54f` (unmerged) | v2.15 | Present only on the unmerged verification branch as `paper/emergent_gr_paper_v2_15.tex` | Populated by independent recomputation on the unmerged branch; no legacy computation repository exists | No `VERIFIED` claims; supported analytic and reconstructed numerical results; P2-C9 and P2-C12 `PROPOSED` | Repository conventions inspected on the unmerged branch; programme synchronization pending | `main` remains scaffolding; the unmerged branch reconstructs the numerical record and leaves `paper-owned:2-emergent-gravity#P2-BETAV-CIRC-01` open | 2026-07-17 |
| Paper 3 | `zetacheng/3-vector-sector` | `0cb95fe7052a675708999d44f66084e446a3d0bf` | `main` at `0cb95fe7052a675708999d44f66084e446a3d0bf` | v3.11 | Merged as `paper/paper3_vector_channel_v3_11.tex` | Merged and independently accepted; 12/12 tests | P3-C-001, P3-C-002, P3-C-004 and P3-C-005 `VERIFIED`; P3-C-003 `FAILED`; P3-C-006 `SUPPORTED`; P3-C-007 `PROPOSED` | Audited on `main` | Authoritative record merged | 2026-07-17 |
| Paper 4 | `zetacheng/4-dark-energy-cosmology` | `3cc5d67bbf745c342b7b7babd78cd2019385af0b` | `sync/legacy-de-migration` at `ea3c7ffc56a9ad3f087945cea817d08398ecbe24` (also `claude/paper4-dark-energy-migration-4ftubo`; unmerged) | v6.3 | Source `paper4_dark_energy_v6_3.tex` is not present | Four legacy interface/wrinkle gates and the terminated monopole chain are populated on the unmerged branch; `main` remains scaffolding | No `VERIFIED` claims; migrated ledger is awaiting independent review | Repository conventions inspected on the unmerged branch; programme synchronization pending | Prompt expectation that migration had only been specified is stale: migration has run on the unmerged branch, not on `main` | 2026-07-17 |
| Paper 5 | `zetacheng/5-topological-sector` | `6de940c4dcbdf419cda4ef7578de2066f6d9a9c5` | `main` at `6de940c4dcbdf419cda4ef7578de2066f6d9a9c5` | v0.23 | Merged as `paper/paper5_internal_dimension_v0_23.tex` | Merged and independently accepted for C2a/GW; 15/15 tests | P5-CL-001, P5-CL-002, P5-CL-003 and P5-CL-007 `VERIFIED`; P5-CL-014 `FAILED`; P5-CL-009–013 `PROPOSED` | Audited on `main` | Authoritative C2a/GW record merged; `topo-mass-radius` remains outside this repository | 2026-07-17 |

## Open ownership and naming items

### Paper 1 scientific-record ownership

`PAPER_MAP.md` assigns Paper 1 to `zetacheng/1-dark-matter-structure`. Paper 1 v16.3 on the unmerged governance branch cites `https://github.com/zetacheng/yukawa-sparc-fits` in its public-repository/reproducibility statement, and the branch records that repository as the scientific-record source.

One of the following must eventually happen:

1. the scientific record is migrated into `1-dark-matter-structure`; or
2. the programme ownership map and paper citations are revised.

The Principal Investigator decides. This sweep records but does not resolve the discrepancy.

### Legacy `kappa-c2a` ownership

The legacy repository `zetacheng/kappa-c2a` at `main` commit `0f153e84574781230ca9a42aa9993bf7092f9262` still contains unmigrated material:

- `topo-mass-radius` at `6a20b05e0899a878fde214c44cf77a8610d7516f`, owned by Paper 5;
- `de-interface-wrinkle` at `5ee543c9c7c37082c1053f438aa10a4a65ee7234`, owned by Paper 4;
- `driven-interface-wrinkle` at `2a80c9db07654c51978891f6bac4a9518ea8a6dd`, owned by Paper 4;
- `sea-interface-phase-conversion` at `1cd94b5dde72745006b3fec67b40b227fd8eaacb`, owned by Paper 4;
- `wrinkle-bound-excitation` at `17c187df09966e2a89bb73489d5cdd121ade3f21`, owned by Paper 4.

The Paper 4 artifacts have been copied onto an unmerged Paper 4 migration branch; their acceptance and merge remain pending. The Paper 5 `topo-mass-radius` evidence remains unmigrated.

## Synchronization checklist

1. paper source imported;
2. progress imported;
3. gate history imported;
4. decision history imported;
5. claim ledger compared with paper prose;
6. conventions checked;
7. cross-paper dependencies registered;
8. latest accepted commit recorded.
