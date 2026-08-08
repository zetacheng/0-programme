# Report — adopt the function-based role model programme-wide (`0-programme`)

Task: replace `0-programme/AGENTS.md`'s named-agent role model with the
function-based model, preserving the former text as labelled historical
evidence. Classification: MATERIAL. Records a decision already made.
Authority: `specs/2026-08-08T2020Z_programme-role-model.md`.

Committed-report layer (A1–A7, A9-pre, commit SHAs/messages, pre-report
head, intended manifest and report message). Post-report evidence (final
`--name-status`, `make check` at the pushed head, the push, the report
commit's stored message, ancestry) is returned to the Reviewer and not
written back.

## A10 — refs (read from the remote)

- `refs/remotes/origin/main` → `ada3087a44e335fd9a1676f2459789b0a36551a9`
- remote `refs/heads/main` → `ada3087a44e335fd9a1676f2459789b0a36551a9`

Branch `governance/programme-role-model` created from `ada3087`. No `main`
ref moved locally. Commands: `git ls-remote origin refs/heads/main`;
`git rev-parse refs/remotes/origin/main`.

## A1 — external material verified, clause by clause

Source: `zetacheng/2-emergent-gravity @ 51d4bbe1a2e965b0793b18f4ead5a11dab54c364 : AGENTS.md` (read-only). Each §1 clause is supported in substance; quoted:

1. **roles are functions; assignments current, not permanent** — *"Roles are functions. Assignments are current, and change by PI instruction."* + *"An assignment recorded here is current, not permanent."* — matches.
2. **Researcher and Reviewer functions exchanged by PI instruction** — *"The Researcher and Reviewer functions are exchanged from time to time, by PI instruction, with the intent of placing the stronger available capability in the Reviewer function."* — matches.
3. **Reviewer agreement required before an execution specification / integration authorization reaches the Executor** — *"Every execution specification or other normative task instruction that establishes or changes the Executor's authority, and every integration authorization, requires the Reviewer's agreement before being issued to the Executor — except where the governing rules expressly provide a standardized authorization or permit a recorded correction without a new review cycle."* — matches.
4. **incidental implementation exchanges are not separate review points** — *"Incidental implementation exchanges within an already-reviewed authorization are not separate review points"* (Paper 2 adds *"per rules 8 and 11"*; the substance is identical, the rule reference is Paper-2-specific). — matches in substance.
5. **minor corrections bounded by the governing rules** — Paper 2: *"Minor corrections may proceed without a further review cycle only to the extent already authorized by `CONVENTIONS.md` rule 10 and the current reviewed specification…"* vs recorded: *"…only to the extent the governing rules already authorize."* Both bound minor corrections to the governing rules and forbid altering reviewed meaning / frozen or hash-pinned content; they agree in substance (the recorded wording is genericised because `0-programme` has no `CONVENTIONS.md` rule 10).
6. **a PI or Researcher instruction does not by itself expand the Executor's authorized scope** — *"An instruction from the PI or the Researcher does not by itself expand the Executor's authorized scope."* — matches (verbatim).
7. **executors are not interchangeable; the capability difference is material** — *"They are not interchangeable, and the difference is material rather than administrative."* with the Codex-workstation / Claude-Code-container capability split. — matches.
8. **the PI announces which executor is in use** — *"The PI announces which executor is in use. A task specification whose acceptance criteria can only be met on one of them should say so."* — matches.

All eight present. No STOP.

## A2 / A2a — role section replaced; former text preserved verbatim

`## Role separation` now states the function-based model (operative), followed by `### Historical role assignment — superseded 2026-08-08`, under which the former named-agent bullets are preserved verbatim and non-operative. No region holds both an operative and a historical copy of the same assignment. The A2a block (heading, three-line intro, four bullets) was inserted and verified byte-for-byte.

### Superseded vs superseding, side by side

| Former (now historical, non-operative) | New (operative) |
|---|---|
| **ChatGPT:** conceptual discussion, ontology, physical interpretation, … does not certify numerical results. | **Principal Investigator** — decides. Owns the physical programme; approves assumptions, gates, conventions, scope changes and programme direction; … *Currently: Zeta Cheng.* |
| **Codex:** programme-repository maintenance and synchronization reports, … must not promote a result into a paper claim without review. | **Researcher** — builds the theory with the PI …; turns the PI's intent into verifiable specifications; … interprets executor results for the PI. *Currently: Claude (chat).* |
| **Claude:** independent review and discrimination, derivation and result review, gate verdicts, overclaim detection, … | **Reviewer** — reviews specifications and executor results …; Reviewer agreement required before an execution specification or integration authorization reaches the Executor …; incidental implementation exchanges are not separate review points. *Currently: ChatGPT.* |
| **Principal Investigator:** owns the physical programme, approves assumptions, gates, scope changes, and programme direction, … | **Executor** — performs the work and is the only party that writes to a repository. *Currently: Codex and Claude Code, selected per task.* |

Plus: Researcher/Reviewer exchanged by PI instruction; minor corrections bounded by the governing rules; a PI/Researcher instruction does not by itself expand the Executor's scope; executors not interchangeable; the PI announces which executor is in use; and a pointer that this is the programme's role model that paper repositories cite.

## A3 — fixed-string checks (region-scoped to `## Role separation`)

Operative region (after the `## Role separation` heading, before the `### Historical …` heading):

| string | count | required |
|---|---|---|
| `Roles are functions. Assignments are current` | 1 | exactly 1 ✓ |
| `The Researcher and Reviewer functions are exchanged` | 1 | exactly 1 ✓ |
| `does not by itself expand the Executor's authorized scope` | 1 | exactly 1 ✓ |
| `Executors are not interchangeable` | 1 | exactly 1 ✓ |
| `Researcher` | 3 | ≥1 ✓ |
| `Reviewer` | 4 | ≥1 ✓ |
| `Executor` | 5 | ≥1 ✓ |
| `**ChatGPT:** conceptual discussion` | 0 | 0 ✓ |
| `**Codex:** programme-repository maintenance` | 0 | 0 ✓ |
| `**Claude:** independent review and discrimination` | 0 | 0 ✓ |

Historical region (the `###` heading to the next `##`): each of the four preserved bullets present exactly once.

## A4 — reviews/README.md

Added the prospective record-header requirement: every review or record created or substantively amended under `reviews/` after 2026-08-08 states the function under which it was produced (Researcher, Reviewer, Executor, or PI authorization); existing records remain valid historical evidence and are not retrospectively non-conforming. `reviews/programme/` layout unchanged (`reviews/programme/.gitkeep` blob-identical to base).

## A5 — GLOBAL_DECISION_LOG.md (append-only)

`git diff --numstat GLOBAL_DECISION_LOG.md` → **`41  0`** (41 insertions, 0 deletions). Entry `## 2026-08-08 — Adopt the function-based role model programme-wide`, in the file's `Decision / Reason / Evidence / Affected papers / Required synchronization / Supersedes / Related gates and repositories` format, records the adoption, its Paper-2 provenance with commit, that it is prospective only, and that no existing record is relabelled.

## A6 — rules untouched (byte-identical to base)

`diff` of `## Shared research rules … EOF` between base `ada3087:AGENTS.md` and the branch head → **no difference**. `## Shared research rules` (1–14) and `## Programme-specific rules` (1–10) are byte-identical; nothing renumbered, reworded, or reordered.

## A7 — nothing else touched

`git diff --name-only ada3087 HEAD --` over `CROSS_PAPER_CONVENTIONS.md GLOBAL_GATES.md GLOBAL_CLAIMS.md SYNC_STATUS.md MASTER_PROGRESS.md MASTER_ROADMAP.md PAPER_MAP.md DEPENDENCIES.md HANDOFF.md README.md Makefile pyproject.toml CITATION.cff docs .github tests programme handoffs papers sea-ice archive reviews/programme` → **empty**. All protected paths (and every `reviews/` file other than `README.md`) blob-identical. `MASTER_PROGRESS.md` unchanged.

## A8 — scope

`0-programme` has **no scope checker**; the base-to-head `--name-status` diff is the evidence. Intended final manifest (base `ada3087` → head):

```
M	AGENTS.md
M	GLOBAL_DECISION_LOG.md
M	reviews/README.md
A	reports/2026-08-08T2020Z_programme-role-model.md
A	specs/2026-08-08T2020Z_programme-role-model.md
```

**2 additions, 3 modifications.** No forbidden operation. At the pre-report head the diff is 3 modifications + 1 addition (the report is added by commit 3).

## A9-pre — make check at the pre-report head

```
python -m ruff check .        → All checks passed!
python -m pytest              → 3 passed
python -m pytest tests/test_repository_structure.py → 3 passed
```

Green. No installation beyond the dev deps `make check` requires. A9-final at the pushed head is post-report evidence.

## Commit hygiene (A9; commits 1–2)

The harness appends `Co-Authored-By:` and `Claude-Session:` trailers by default; both **suppressed** on every commit. Messages inspected before and read back after:

- commit 1 `f8f6881` — `docs: record the programme role-model adoption specification` (suppressed: `Co-Authored-By`, `Claude-Session`).
- commit 2 `2616261` — `docs: adopt the function-based role model programme-wide; preserve prior text as historical` (suppressed: `Co-Authored-By`, `Claude-Session`).
- commit 3 (report) intended message `docs: report the programme role-model adoption` — trailer-free; read back as post-report evidence.

Pre-report head: `2616261...` (commit 2).

## Repository-wide named-agent audit

Search: `git grep -nE "ChatGPT|Codex|Claude"` over all tracked files, excluding the two files this task authors. Findings, classified:

### Live named-agent role assignments — NOT fixed here (each a separate authorization)

- **`README.md`**, `## Role separation` (lines 15–43): `### ChatGPT`, `### Codex`, `### Claude`, `### Principal Investigator` — a full named-agent role assignment, the same divergence just resolved in `AGENTS.md`. **Operative in README; left unfixed.**
- **`HANDOFF.md`** (lines 19–27): `## Codex responsibility`, `## ChatGPT responsibility`, `## Claude responsibility` — named-agent responsibility assignments. **Operative; left unfixed.**

### Resolved by this task

- **`AGENTS.md`** (lines 34–36): named-agent bullets, now under `### Historical role assignment — superseded 2026-08-08`, explicitly non-operative. No longer a live divergence.

### Incidental mentions (not role assignments)

- **`AGENTS.md`** operative region: *"Currently: Claude (chat)"*, *"Currently: ChatGPT"*, *"Codex and Claude Code"* — current function-holder annotations **within** the new function-based model, not fixed-role assignments.
- **`GLOBAL_DECISION_LOG.md`** (this task's entry): the descriptive phrase *"the former named-agent text (ChatGPT / Codex / Claude / PI)"* — a reference, not an assignment.
- **`reports/2026-08-08T1904Z_…`** and **`reports/2026-08-08T1954Z_…`**: prior task reports mentioning `Claude-Session`/`Co-Authored-By` hygiene and the earlier fixed-agent finding — historical records, not operative assignments.

### `docs/RESEARCH_WORKFLOW.md`

Exists in `0-programme`. It does **not** name any agent; its only role wording is generic — line 11, *"Record the reviewer verdict and PI decision separately"* (functions, not named agents). Reported per §2; nothing to fix. (Paper 2 found a named-agent divergence in its own `docs/`; `0-programme`'s does not carry one.)

**Fix count: 0.** This audit is left as the evidence base for the next governance task (README and HANDOFF alignment).

## Integrating vs a paper repository / observations

`0-programme` has no merge or scope guard; checks were done with read-only Git (`git grep`, `git rev-parse <rev>:<path>`, `git diff --name-status/--numstat`, region extraction). Nothing behaved unexpectedly.

## Stops and clarifications

No hard STOP. One primary category per stop; none triggered.

- **SPECIFICATION_DEFECT** — none. (The spec pre-corrected an earlier draft's operative-region definition and its `docs/`-only audit scope; the governing text is consistent.)
- **ENVIRONMENT** — none (no install).
- **OBSERVATION_METHOD_ERROR** — none.
- **REPOSITORY_DEFECT** — none. (The absent merge/scope guards are a reported limitation, not fixed here.)
- **UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY** — none blocking. Secondary, carried forward: `README.md` and `HANDOFF.md` still carry named-agent assignments (audited above; each a separate authorization).

## Anything ambiguous / would have specified differently

- **A1 clause 5** wording: `0-programme` has no `CONVENTIONS.md` rule 10, so the recorded "minor corrections" clause is genericised to "the governing rules already authorize." Substance matches Paper 2; a future revision could enumerate which `0-programme` rules stand in for Paper 2's rule 10.
- Otherwise the specification was internally consistent and consistent with `0-programme`'s `AGENTS.md`.
