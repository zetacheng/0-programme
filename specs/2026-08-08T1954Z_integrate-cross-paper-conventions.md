# Task specification — integrate the cross-paper conventions import (`0-programme`)

**Repository: `zetacheng/0-programme`.** Runs under that repository's
`AGENTS.md`.

Specification evidence base: `b399e115786422f5985ae61293be15c26d647171`

    Branch  governance/cross-paper-conventions-import
            810fe767119cf19c22045c0821e0d915eb247068

Classification: **MATERIAL**. The branch completed result review. This is
the integration authorization: **one `--no-ff` merge into `main`**.

Dry run: **2 additions, 3 modifications**, no conflict, merge-base is the
original base `b399e11`. If a conflict occurs, STOP.

This is `0-programme`'s first content integration: its `main` has carried
only infrastructure since initialization.

## What is being integrated

The cross-paper conventions registry gains **seven row-level changes**:
six rows populated with values established in Paper 2 (and Paper 3, for
the `G_omega` row), each citing repository, path and commit; and one row —
`Sign convention for attraction and repulsion` — changed from
`NOT YET IMPORTED.` to `NOT DEFINED`. The former closing sentence is
replaced by the PI ruling that the registry is authoritative for the
current value used by downstream work, while paper repositories retain
their historical/frozen statements and hold the establishing derivations.
A legend distinguishes a populated value, `NOT DEFINED`, and
`NOT YET IMPORTED.`. `Wick rotation` remains `NOT YET IMPORTED.`; the
Euclidean exponent mapping is a new, separate row.

## What this integration does NOT establish

- Paper 2 is not imported. `MASTER_PROGRESS.md` keeps
  `INFRASTRUCTURE INITIALIZED`; progress, gates, claims and paper content
  remain `NOT IMPORTED`.
- The attraction/repulsion convention is not defined; the registry records
  that nobody has defined it.
- `CANONICAL_INTERACTION.md` is not ratified (DRAFT v0.5; cited as
  provenance only).
- `0-programme`'s role model is not reconciled (fixed-agent text stands; a
  separate authorization).

## Sequence

1. fetch; verify refs (A1); create a local integration branch from the base.
2. `--no-ff` merge the source branch (the pinned remote ref `810fe767`).
3. on the unpushed pre-report head: A4, A5, A6, A7, A8-pre.
4. commit the integration report, carrying the step-3 evidence.
5. remaining locally-verifiable checks at the final head.
6. push only if every check at steps 3 and 5 passed.
7. fetch; verify final ref agreement.

`0-programme` has no merge guard and no scope checker; the equivalent
checks are performed directly with read-only Git commands, named in the
report. An absent tool is a finding, not a reason to skip a check or to
copy a tool across repositories.

## Acceptance criteria (summary; full text governs)

- **A1** refs: remote `main` and `origin/main` = `b399e11`; source =
  `810fe767`. Mismatch → STOP.
- **A2** parentage: parent 1 = the integration spec commit (commit 1),
  parent 2 = `810fe767`, merge-base = `b399e11`.
- **A3** scope, exact: base `b399e11` → head; 4 additions
  (`reports/2026-08-08T1904Z_…`, `reports/2026-08-08T1954Z_…`,
  `specs/2026-08-08T1904Z_…`, `specs/2026-08-08T1954Z_…`) + 3
  modifications (`CROSS_PAPER_CONVENTIONS.md`, `GLOBAL_DECISION_LOG.md`,
  `SYNC_STATUS.md`); forbidden ops: delete/rename/copy/type_change/
  unmerged/unknown. An eighth path is a defect.
- **A4** `CROSS_PAPER_CONVENTIONS.md` blob-identical to source; 13 rows;
  `Wick rotation` = `NOT YET IMPORTED.`; `Euclidean exponent mapping` its
  own row; sign row = `NOT DEFINED`; six other rows `NOT YET IMPORTED.`;
  legend present; former closing sentence occurs zero times.
- **A5** `GLOBAL_DECISION_LOG.md` blob-identical to source; base-to-head
  zero deleted lines.
- **A6** `SYNC_STATUS.md`: exactly Paper 2's `Conventions audited` cell
  changed; all other cells/rows unchanged.
- **A7** protected paths blob-identical base↔head (incl.
  `MASTER_PROGRESS.md`, `AGENTS.md`, and every path under `docs/`,
  `.github/`, `tests/`, `programme/`, `handoffs/`, `papers/`, `reviews/`,
  `sea-ice/`, `archive/`).
- **A8** `make check` passes at the merged head (`lint test structure`);
  A8-pre in the report, A8-final post-report.
- **A9** commit-message hygiene on every commit incl. the merge: no
  `Co-Authored-By`, no session id/URL, no tool attribution; report
  suppression per commit.
- **A10** source branch still `810fe767` after the merge; no branch
  deleted.

## Commit order

1. this integration specification.
2. `--no-ff` merge of the source branch.
3. the integration report.

## Invariants

- Executor-writable: this spec and the integration report only.
  Everything arriving by merge is integrated exactly as reviewed.
- No further import from any paper repository; no paper repository
  modified.
- No additional registry row filled (incl. `Wick rotation`).
- `MASTER_PROGRESS.md` untouched.
- `SYNC_STATUS.md` at the merged head blob-identical to source
  `@ 810fe767`; the one carried cell change is the merge's, none added.
- Role model not reconciled; Paper 2 governance tools not imported.
- Merge commit only: no ff, squash, rebase, or force-push; merge the
  pinned remote ref.
- Any conflict is an immediate STOP.
- `0-programme`'s `AGENTS.md` governs this task.
