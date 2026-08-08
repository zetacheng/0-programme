# Task specification — adopt the function-based role model programme-wide in `0-programme`

**Repository: `zetacheng/0-programme`.** Runs under that repository's
`AGENTS.md`.

Specification evidence base: `ada3087a44e335fd9a1676f2459789b0a36551a9`

External evidence base (`zetacheng/2-emergent-gravity`, read-only):
`51d4bbe1a2e965b0793b18f4ead5a11dab54c364`

Classification: **MATERIAL**. Branch only; integration is a separate
authorization. **This records decisions the PI has already made. It
decides nothing new.** No scientific content, gate, claim or convention
is touched.

## The divergence

`0-programme/AGENTS.md` assigns roles to named agents (ChatGPT
conceptual, Codex maintenance, Claude review, PI ownership). Paper 2
replaced that on 2026-08-06 with a function-based model (roles are
functions; assignments current, not permanent; Researcher and Reviewer
exchanged by PI instruction). Both statements are live and disagree;
now that `0-programme` holds authoritative cross-paper values, the
divergence must be resolved centrally: `0-programme` states the model,
papers cite it.

## The model to record

`AGENTS.md`'s `## Role separation` section is replaced by the
function-based model: Principal Investigator (decides), Researcher
(builds theory, writes specifications, interprets executor results),
Reviewer (reviews specifications and executor results; agreement
required before an execution specification or integration authorization
reaches the Executor, except standardized authorizations / recorded
corrections; incidental implementation exchanges are not separate review
points), Executor (performs work, only party that writes to a
repository). Researcher and Reviewer are exchanged by PI instruction to
place the stronger capability in the Reviewer function. Minor corrections
are bounded by the governing rules; a PI or Researcher instruction does
not by itself expand the Executor's authorized scope. Executors are not
interchangeable (Codex on the PI's GPU workstation for decisive/long
runs; Claude Code in a sandboxed container for short deterministic
verification/preparation/audit); the PI announces which executor is in
use.

Provenance: `zetacheng/2-emergent-gravity @ 51d4bbe1 : AGENTS.md`,
verified clause-by-clause in substance before recording. If any clause
is absent, STOP.

## What else changes

- Every review or record created or substantively amended under
  `reviews/` after adoption states in its header the function under
  which it was produced. Existing records remain valid historical
  evidence and are not retrospectively non-conforming (`reviews/README.md`).
- `AGENTS.md` states that this is the programme's role model and that
  paper repositories cite it. No paper repository is edited.

## Explicitly NOT changed

- Shared research rules 1–14 and programme-specific rules 1–10 —
  byte-identical, not renumbered/reworded/reordered.
- `CROSS_PAPER_CONVENTIONS.md`, `GLOBAL_GATES.md`, `GLOBAL_CLAIMS.md`,
  `SYNC_STATUS.md`, `MASTER_PROGRESS.md`.
- `docs/RESEARCH_WORKFLOW.md` — checked and reported, not fixed here (a
  second file is a second authorization).

## Acceptance criteria (summary; full text governs)

- **A0** commit order: (1) this spec; (2) `AGENTS.md`,
  `GLOBAL_DECISION_LOG.md`, `reviews/README.md`; (3) report. UTC token
  `2020` fixed by commit 1.
- **A1** external material verified clause by clause (eight clauses);
  absence of any is a STOP.
- **A2 / A2a** `## Role separation` states the model; former text
  preserved verbatim under `### Historical role assignment — superseded
  2026-08-08`; no region holds both an operative and historical copy of
  the same assignment.
- **A3** fixed-string checks in the operative and historical regions of
  `## Role separation` only.
- **A4** `reviews/README.md` header requirement; `reviews/programme/`
  layout unchanged.
- **A5** `GLOBAL_DECISION_LOG.md` entry, append-only, zero deletions.
- **A6** rules sections byte-identical to base.
- **A7** nothing else touched.
- **A8** scope: add the two `2020Z` files; modify `AGENTS.md`,
  `GLOBAL_DECISION_LOG.md`, `reviews/README.md`. Final: 2 additions, 3
  modifications.
- **A9** `make check` passes.
- **A10** branch only from `ada3087`; `main` unmoved; push task branch
  only.

## Invariants

- Executor-writable: the five A8 paths only.
- Decide nothing; if §1 is ambiguous, stop and report.
- No paper repository modified; no paper file copied in.
- Shared/programme rules untouched; no renumbering.
- `docs/RESEARCH_WORKFLOW.md` (or any agent-naming file) not fixed here.
- No existing `reviews/` record retroactively relabelled.
- Commit-message hygiene: no `Co-Authored-By`, no session id/URL, no
  tool attribution; report suppression per commit.
- No merge, PR, force-push, or history rewrite. Branch
  `governance/programme-role-model`.
- `0-programme`'s `AGENTS.md` governs this task.
