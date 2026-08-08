# Report — integrate the cross-paper conventions import (`0-programme`)

Task: integrate `governance/cross-paper-conventions-import` into `main`
via one `--no-ff` merge. Classification: MATERIAL. First content
integration into `0-programme`'s `main`.
Authority: `specs/2026-08-08T1954Z_integrate-cross-paper-conventions.md`.

This report carries the pre-push evidence (A1, A2, A4–A7, A8-pre, A9 for
commits 1–2), the intended final manifest, and the pre-report head.
Post-report evidence (A3 final `--name-status` at the pushed head,
A8-final, the push, the final ref comparison, the report commit's stored
message, and ancestry) is returned to the Reviewer and is **not** written
back into this file, per §4.

## A1 — refs (read from the remote)

- `refs/remotes/origin/main` → `b399e115786422f5985ae61293be15c26d647171`
- remote `refs/heads/main` → `b399e115786422f5985ae61293be15c26d647171`
- remote `refs/heads/governance/cross-paper-conventions-import` → `810fe767119cf19c22045c0821e0d915eb247068`

All as required; no mismatch; no STOP.
Commands: `git fetch origin`; `git ls-remote origin refs/heads/main`;
`git ls-remote origin refs/heads/governance/cross-paper-conventions-import`;
`git rev-parse refs/remotes/origin/main`.

## A2 — merge parentage

- merge commit: `b06613cc5bc34dfa9828b93627ec58f5b862fe96`
- parent 1: `ec95d5c936a19d434cc1c70402569833dfd8425f` (the integration specification, commit 1)
- parent 2: `810fe767119cf19c22045c0821e0d915eb247068` (the reviewed source branch)
- merge-base(parent 1, parent 2): `b399e115786422f5985ae61293be15c26d647171` (the ORIGINAL base)

Commands: `git merge-base HEAD 810fe767…`; `git log -1 --format='%P'`;
`git rev-parse HEAD^1 HEAD^2`. The merge was `--no-ff` on the pinned
remote-ref SHA; a `--no-commit --no-ff` dry run reported *"Automatic merge
went well"* with zero unmerged paths before it was committed.

## A3 — scope (intended final manifest)

`0-programme` has **no scope checker** (its only test target is
`tests/test_repository_structure.py`); the base-to-head `--name-status`
diff is supplied as the evidence. Intended final manifest at the pushed
head (base `b399e11` → head):

```
M	CROSS_PAPER_CONVENTIONS.md
M	GLOBAL_DECISION_LOG.md
M	SYNC_STATUS.md
A	reports/2026-08-08T1904Z_cross-paper-conventions-import.md
A	reports/2026-08-08T1954Z_integrate-cross-paper-conventions.md
A	specs/2026-08-08T1904Z_cross-paper-conventions-import.md
A	specs/2026-08-08T1954Z_integrate-cross-paper-conventions.md
```

**4 additions, 3 modifications.** Two additions (`…1904Z…`) arrive from the
branch; two (`…1954Z…`) are authored here. No forbidden operation
(delete/rename/copy/type_change/unmerged/unknown). At the pre-report head
the diff is 3 modifications + 3 additions (the `…1954Z…` report is added by
commit 3). The final `--name-status` at the pushed head is post-report
evidence.

## A4 — the registry arrives intact

`CROSS_PAPER_CONVENTIONS.md` at the merged head is **blob-identical** to
its value on the source branch:

- head `HEAD:CROSS_PAPER_CONVENTIONS.md` = `b4dd002a1a2fea0e3f1ed07659e6bc06e343177a`
- source `810fe767:CROSS_PAPER_CONVENTIONS.md` = `b4dd002a1a2fea0e3f1ed07659e6bc06e343177a`

Read from the merged file:

- **13 data rows** (one more than the base's 12);
- `Wick rotation` still reads `NOT YET IMPORTED.`;
- `Euclidean exponent mapping` exists as its **own** row;
- `Sign convention for attraction and repulsion` reads `NOT DEFINED`;
- the six other rows (`Lattice/cutoff units`, `Field dimensions`,
  `Fourier transform`, `Error convention`, `Naming …`, `Wick rotation`)
  still read `NOT YET IMPORTED.`;
- the legend is present (`## Legend`);
- the former closing sentence *"This file does not override a paper's
  convention registry automatically"* occurs **zero** times.

Commands: `git rev-parse HEAD:… 810fe767:…`; `git show HEAD:CROSS_PAPER_CONVENTIONS.md | grep …`.

### The merged registry table, quoted in full

| Convention | Programme value |
|---|---|
| Metric signature | `(1, 1, 1, 1)` Euclidean.<br>source: Paper-2 Phase-A freeze, conventions block — `zetacheng/2-emergent-gravity @ 51d4bbe1 : derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` (§C, `metric_signature`). |
| Wick rotation | NOT YET IMPORTED. |
| Euclidean exponent mapping | The canonical interaction expression `X` is written as it appears in the Boltzmann exponent: `exp(-S_E)` contains `exp(+X)`, i.e. `S_E = S_E,0 - X`. For a channel coefficient `c` in `X`, the Hubbard-Stratonovich coefficient is `g = +2c`.<br>status: PI-supplied convention, not derived from frozen material.<br>source: `zetacheng/2-emergent-gravity @ 51d4bbe1 : DECISION_LOG.md, entry 2026-08-08` (PI ruling, Euclidean exponent mapping). |
| Gamma matrices and gamma5 | `gamma5 = gamma(0)*gamma(1)*gamma(2)*gamma(3)`; Hermitian; `gamma5^2 = Id4`. Euclidean Hermitian basis `S=Id4`, `P=gamma5`, `V=gamma(mu)`, `A=I*gamma(mu)*gamma5`, `T=I*(gamma(mu)gamma(nu)-gamma(nu)gamma(mu))/2`; `trace(Id4) = 4`.<br>source: Paper-2 Phase-A freeze — `zetacheng/2-emergent-gravity @ 51d4bbe1 : derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` (§C); PI ruling 2026-08-07 on the conflicting companion entry, reproduced in `specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md` §8 (the Phase-A freeze governs over the `CANONICAL_INTERACTION.json` companion). |
| Flavor generator normalization | `trace(lam(A) lam(B)) = 2*delta(A,B)`; `lam(0) = sqrt(2/N)*Id(N)`; `A = 0 .. N^2-1`, a U(N) index set including the singlet.<br>source: Paper-2 Phase-A freeze, conventions block (`un_generator_normalization`) — `zetacheng/2-emergent-gravity @ 51d4bbe1 : derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md`. `CANONICAL_INTERACTION.md` §2 is provenance only (it still carries a DRAFT v0.5 banner); the establishing citation is the frozen freeze artifact, not the draft that fed it. |
| Lattice/cutoff units | NOT YET IMPORTED. |
| Interaction normalization | `X = (G/(2N)) * Sum( bilinear(lam(A),Id4)^2 + bilinear(lam(A),I*gamma5)^2, (A,0,N^2-1) )`. Only S and P are supported in the interaction; V, A and T are Fierz/HS representation families, not independent couplings.<br>source: Paper-2 Phase-A freeze, `canonical_interaction_expression` — `zetacheng/2-emergent-gravity @ 51d4bbe1 : derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` (§D). |
| Definitions of \(G\), \(G_V\), \(G_\omega\) | Paper 3 writes `L_V = (G_omega/2) * J_mu J^mu` with `J_mu = psibar gamma_mu psi`. The Fierz-induced vector singlet coefficient of `(psibar gamma_mu psi)^2` is `c_J = -G/(2N)`, hence `G_omega = 2*c_J = -G/N`. The apparent factor of two between `-G/N` and `-G/(2N)` is a normalization mapping, not a discrepancy: one names a coupling in the `(G/2)J^2` convention, the other is the coefficient of `J^2` itself.<br>source: Paper-2 normalisation audit — `zetacheng/2-emergent-gravity @ 51d4bbe1 : derivations/P2-NORMALISATION-AUDIT_g_omega.md`; Paper-3 note `zetacheng/3-vector-sector @ 8c363ef0 : derivations/u3-fierz/u3_fierz.md` (convention at lines 10-11; assembly at lines 185-190). |
| Sign convention for attraction and repulsion | **NOT DEFINED.** No rule anywhere in the programme maps a channel coefficient's sign to a physical attraction or repulsion label. The Paper-2 channel-character derivation searched for one and returned `ATTRACTIVE/REPULSIVE NOT DEFINED BY THE FROZEN MATERIAL`.<br>note: this is **not** the same as `NOT YET IMPORTED` (see legend).<br>source: `zetacheng/2-emergent-gravity @ 51d4bbe1 : derivations/P2-PHASE-01_channel_character.md` (Layer 2 verdict). |
| Field dimensions | NOT YET IMPORTED. |
| Fourier transform | NOT YET IMPORTED. |
| Error convention | NOT YET IMPORTED. |
| Naming of Sea, interface, lattice phase, wrinkle and topological object | NOT YET IMPORTED. |

Legend and closing paragraph are present in the merged file as reviewed (a populated value / `NOT DEFINED` / `NOT YET IMPORTED.` distinction, and the registry-authority ruling).

## A5 — GLOBAL_DECISION_LOG.md append-only

Blob-identical to source (`HEAD:GLOBAL_DECISION_LOG.md` == `810fe767:GLOBAL_DECISION_LOG.md`). Base-to-head numstat: **`32  0`** (32 insertions, 0 deletions). Command: `git diff --numstat b399e11 HEAD -- GLOBAL_DECISION_LOG.md`.

## A6 — SYNC_STATUS.md, exactly one cell

Blob-identical to source. Base-to-head diff — Paper 2's `Conventions audited` cell only:

```
-| Paper 2 | `zetacheng/2-emergent-gravity` | NOT IMPORTED | NOT IMPORTED | NOT IMPORTED | NOT IMPORTED | NOT IMPORTED | NOT IMPORTED |
+| Paper 2 | `zetacheng/2-emergent-gravity` | NOT IMPORTED | NOT IMPORTED | NOT IMPORTED | NOT IMPORTED | 7 rows @ 51d4bbe1 (6 imported, 1 NOT DEFINED) | NOT IMPORTED |
```

Paper 2's other five cells (`Latest paper imported`, `Progress imported`, `Gates imported`, `Claims audited`, `Last sync`) and every other paper's row are unchanged (the base-to-head diff touches only the Paper 2 line, and only its `Conventions audited` cell).

## A7 — protected paths blob-identical (base ↔ merged head)

`git diff --name-only b399e11 HEAD -- MASTER_PROGRESS.md AGENTS.md GLOBAL_GATES.md GLOBAL_CLAIMS.md MASTER_ROADMAP.md PAPER_MAP.md DEPENDENCIES.md HANDOFF.md README.md Makefile pyproject.toml CITATION.cff docs .github tests programme handoffs papers reviews sea-ice archive` → **empty** (all identical). `MASTER_PROGRESS.md` explicitly unchanged (`b399e11:MASTER_PROGRESS.md` == `HEAD:MASTER_PROGRESS.md`): `INFRASTRUCTURE INITIALIZED` and all `NOT IMPORTED` rows stand.

## A8-pre — make check at the pre-report head (`b06613c`)

```
python -m ruff check .
All checks passed!
python -m pytest
… tests/test_repository_structure.py ...   3 passed
python -m pytest tests/test_repository_structure.py
… tests/test_repository_structure.py ...   3 passed
```

Green at the pre-report head. No installation beyond the dev deps `make check` requires. A8-final at the pushed head is post-report evidence and carries the verdict.

## A9 — commit-message hygiene (commits 1–2)

The executor's harness appends `Co-Authored-By:` and `Claude-Session:`
trailers by default; both were **suppressed** on every commit to satisfy
the hygiene rule. Messages inspected before writing and read back after:

- commit 1 `ec95d5c` — `docs: record the cross-paper conventions integration specification` (suppressed: `Co-Authored-By`, `Claude-Session`).
- commit 2 (merge) `b06613c` — `merge: integrate cross-paper conventions first import (governance/cross-paper-conventions-import @ 810fe767)` (suppressed: `Co-Authored-By`, `Claude-Session`).

Both stored messages carry no trailer. The report commit (commit 3) intended message is `docs: report the cross-paper conventions integration`, likewise trailer-free; it is read back from the object as post-report evidence.

## Pre-report head

`b06613cc5bc34dfa9828b93627ec58f5b862fe96` (the merge commit; the report commit will be its child).

## Worktree states (stated separately)

- **Merge worktree** (this task's working tree on `governance/integrate-cross-paper-conventions`): clean after each commit; the merge produced no conflict and left no unmerged paths.
- **`main` worktree**: untouched by this task until the push; `main` is not checked out and no `main` ref is moved locally. The remote `main` is advanced only by the post-report push, after all local checks pass.

## Integrating into `0-programme` vs a paper repository

Differences observed, this being the programme repo's first content merge:

- `0-programme` has **no merge guard and no scope checker** — Paper 2's governance tooling does not exist here. Equivalent checks were done directly with read-only Git (`git merge-base`, `git rev-parse <rev>:<path>` blob comparison, `git diff --name-status/--numstat`, `git show`), named above. Their absence is reported, not remedied; no tool was copied across repositories.
- `make check` here runs only `lint test structure` over infrastructure tests (no scientific regression suite), so the CI gate is lighter than a paper repo's; correspondingly more of the assurance rests on the blob-identity and scope checks.
- Otherwise the mechanics (pinned-SHA `--no-ff` merge, spec→merge→report layering, hygiene suppression) matched paper-repo integrations; nothing behaved unexpectedly.

## Stops and clarifications

No hard STOP occurred. One primary category per stop; none triggered.

- **SPECIFICATION_DEFECT** — none. (The spec pre-emptively corrected an earlier draft that forbade altering any `SYNC_STATUS.md` cell, which would have contradicted A3/A6; the corrected spec is internally consistent.)
- **ENVIRONMENT** — none. No installation beyond `make check`'s existing dev deps.
- **OBSERVATION_METHOD_ERROR** — none.
- **REPOSITORY_DEFECT** — none in `0-programme`. (The absent merge/scope guards are a known limitation, reported here, not a defect to fix in this task.)
- **UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY** — none blocking. (Carried-forward, not for this task: `0-programme`'s fixed-agent role model diverges from Paper 2's function-based model; a separate authorization.)

## Anything ambiguous / would have specified differently

- The merge was performed on the pinned SHA `810fe767…`, which is byte-for-byte the remote ref `refs/heads/governance/cross-paper-conventions-import`; "merge the pinned remote ref, not a local copy" is satisfied by merging that SHA.
- No other ambiguity; the specification was consistent with `0-programme`'s `AGENTS.md`.
