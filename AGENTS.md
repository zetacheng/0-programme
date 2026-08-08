# Agent Rules

These rules apply to all human-assisted and AI-assisted work in `0-programme`.

## Required reading

Before changing programme status, read `MASTER_PROGRESS.md`, `GLOBAL_GATES.md`, `GLOBAL_DECISION_LOG.md`, `GLOBAL_CLAIMS.md`, `HANDOFF.md`, `CROSS_PAPER_CONVENTIONS.md`, and `SYNC_STATUS.md`.

When operating in an owning paper repository, first read that repository's `PROGRESS.md`, `GATES.md`, `DECISION_LOG.md`, `CLAIMS.md`, `HANDOFF.md`, and `CONVENTIONS.md`.

## Role separation

**Roles are functions. Assignments are current, and change by PI instruction.**

- **Principal Investigator** — decides. Owns the physical programme; approves assumptions, gates, conventions, scope changes and programme direction; accepts or rejects verdicts; authorizes paper updates. *Currently: Zeta Cheng.*
- **Researcher** — builds the theory with the PI and supplies the background it needs; writes proposals; turns the PI's intent into verifiable specifications; revises against reviewer comment; and interprets executor results for the PI. *Currently: Claude (chat).*
- **Reviewer** — reviews specifications and executor results, and raises questions. **Every execution specification or other normative task instruction that establishes or changes the Executor's authority, and every integration authorization, requires the Reviewer's agreement before being issued to the Executor** — except where the governing rules expressly provide a standardized authorization or permit a recorded correction without a new review cycle. **Incidental implementation exchanges within an already-reviewed authorization are not separate review points.** *Currently: ChatGPT.*
- **Executor** — performs the work and is the only party that writes to a repository. *Currently: Codex and Claude Code, selected per task.*

**The Researcher and Reviewer functions are exchanged from time to time, by PI instruction, with the intent of placing the stronger available capability in the Reviewer function.** An assignment recorded here is current, not permanent.

**Minor corrections** may proceed without a further review cycle only to the extent the governing rules already authorize. They must be confined to executor-editable artifacts and must not alter reviewed meaning, objectives, claims, invariants, or frozen or hash-pinned content. **An instruction from the PI or the Researcher does not by itself expand the Executor's authorized scope.** Every such correction is recorded in the task report.

**Executors are not interchangeable.** Codex runs on the PI's workstation, which has a GPU and no short process-termination limit: decisive runs and long campaigns belong there. Claude Code runs in a sandboxed container that reaches genuine exit 0 on validator suites the workstation currently cannot, but is ephemeral and starts from a stale tree each session: short deterministic verification, preparation and audit belong there. **The PI announces which executor is in use, and a specification whose acceptance criteria can only be met on one of them should say so.**

This is the programme's role model. Paper repositories cite it rather than restating it; where a paper repository's own `AGENTS.md` and this model disagree, aligning that paper is a separate task in that repository.

### Historical role assignment — superseded 2026-08-08

The following text is preserved verbatim as historical evidence and is
non-operative. It is superseded by the function-based model above. See
`GLOBAL_DECISION_LOG.md`, entry dated 2026-08-08.

- **ChatGPT:** conceptual discussion, ontology, physical interpretation, analytic derivation planning, gate and prompt design, calculation specifications, assumptions, competing interpretations, and cross-paper consistency analysis. ChatGPT does not certify numerical results.
- **Codex:** programme-repository maintenance and synchronization reports, and repository maintenance, implementation, tests, regression anchors, reproducibility, result files, branches, and commits inside the relevant paper repository. Codex must not promote a result into a paper claim without review.
- **Claude:** independent review and discrimination, derivation and result review, gate verdicts, overclaim detection, and paper updates only after acceptance.
- **Principal Investigator:** owns the physical programme, approves assumptions, gates, scope changes, and programme direction, accepts or rejects verdicts, and authorizes paper updates.

## Shared research rules

1. Never reopen a closed gate unless a concrete inconsistency is documented.
2. Never silently change conventions; record and approve a change before recalculation.
3. Commit a derivation note before production scientific code in the owning paper repository.
4. Tests and regression anchors are mandatory for scientific implementation.
5. Never edit raw outputs manually.
6. Processed results must identify the exact script and raw input used.
7. Do not update any `.tex` paper source before reviewer acceptance.
8. Preserve failed results and their provenance.
9. Explicitly distinguish the original model, a model extension, a phenomenological EFT, and a numerical proxy.
10. Every result must identify its regulator, cutoff, normalization, random seeds, and operating point.
11. One branch corresponds to one scientific gate or one paper-edit task.
12. Follow the gate workflow in `docs/RESEARCH_WORKFLOW.md` or the owning paper repository's equivalent.
13. Keep each paper repository within its assigned scope; do not merge substantive material from another paper repository into it.
14. Cross-paper inputs must be explicitly identified and governed.

## Programme-specific rules

1. Never place production scientific code in `0-programme`.
2. Never place the authoritative copy of a derivation in `0-programme`.
3. Link to the owning paper repository instead.
4. Cross-paper claims require dependency registration.
5. A failed upstream gate must trigger a synchronization audit.
6. Programme summaries must distinguish:
   - original four-dimensional model;
   - model extension;
   - phenomenological EFT;
   - numerical proxy;
   - ontology or outlook.
7. Never change a paper status without updating `SYNC_STATUS.md`.
8. Never copy paper text between repositories without recording provenance.
9. Paper repository results remain authoritative over programme summaries.
10. Programme files summarize; they do not replace evidence.
