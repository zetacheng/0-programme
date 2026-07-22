# Report — Canonical PROGRAMME_STATE v1.0 landing

Date: 2026-07-21
Repo: `zetacheng/0-programme`
Branch: `docs/programme-state-v1` (off `main` `b399e11`)
Task: land the canonical Programme State ("constitution") + CURRENT_STATUS,
docs-only, **no merge**. Push and STOP for review.

## Preconditions (recorded, per prompt)

Discriminator (ChatGPT) review completed 2026-07-21 — document structure,
governance, and word-named evidence classes approved; required amendments
issued. Generator (Claude) applied the amendments; PI (Zeta) approved the
final 1.0 artifacts on 2026-07-21. The Task-1 hashes identify the approved
**final** files, independently re-verified below (no DRAFT/pending marker in
the landed header).

## Part 0 — remote verification (mandatory)

- `git fetch origin` performed.
- `origin/main` = `b399e115786422f5985ae61293be15c26d647171` (`b399e11`) —
  **matches** the required precondition. Proceeded to branch.
- Sync branch `8b0d370` (`sync/programme-state-2026-07-16`) left untouched
  (known-unmerged, out of scope).

## Task 1 — files landed verbatim

sha256 of the PI-supplied inputs (verified **before** committing):

```
44bf8cfaef066df9a97e41cd22e1118b495660815eb1efd029e9c2e83faf6a08  (supplied) PROGRAMME_STATE.md
5fb3fe4646cc9f89e199b63c8ccaf5b3d8685c4fad766916e4d31c81119ae13b  (supplied) CURRENT_STATUS.md
```

sha256 at destination after landing (byte-for-byte identical to the table):

```
44bf8cfaef066df9a97e41cd22e1118b495660815eb1efd029e9c2e83faf6a08  docs/PROGRAMME_STATE.md
5fb3fe4646cc9f89e199b63c8ccaf5b3d8685c4fad766916e4d31c81119ae13b  CURRENT_STATUS.md
```

Both match the pinned table exactly. No reformatting / re-wrapping / whitespace
normalization applied.

Header guard (re-verified even though the precondition is recorded satisfied):

- `Version` = `1.0` — does **not** end in `-draft`.
- `Status` = `CANONICAL — approved for landing` — no `pending`/`draft`.
- `Discriminator (this version)` = `ChatGPT — review completed 2026-07-21 …` —
  no `pending`/`draft`.
- `Approved by` = `PI (Zeta), 2026-07-21` — no `pending`/`draft`.

Guard PASS (case-insensitive). Commit `210b7fd`.

## Task 2 — README reading-order pointer

Added a `## Start here` section immediately after the intro paragraph, before
`## Paper repositories`. Wording per prompt (links adapted to the README's
existing relative-link style). Nothing else in `README.md` changed; the
structure-test invariants hold (`README.md` still begins with `# 0-programme`
and still contains "contains no complete paper manuscript"). Commit `c842fcb`.

README diff summary (one hunk, insertion only):

```
+## Start here
+
+Read [CURRENT_STATUS.md](CURRENT_STATUS.md) for the live handoff (2 min), then
+[docs/PROGRAMME_STATE.md](docs/PROGRAMME_STATE.md) for the canonical programme
+state and governance (10 min), then the paper repositories. PROGRAMME_STATE.md
+changes only through its §1.4 amendment chain; CURRENT_STATUS.md is updated by
+the executor as the final substantive step of each approved task, immediately
+before the report-only commit.
```

## Task 3 — governance guard test

Added `tests/test_programme_state_guard.py` (three tests), parsing the Markdown
**header tables** (not arbitrary body/README lines):

1. `test_programme_state_header_is_canonical_not_draft` — `Version` not
   `-draft`; `Status` / `Approved by` / `Discriminator` present and free of
   `pending`/`draft` (case-insensitive).
2. `test_programme_state_changelog_integrity` — `## 8. Changelog` section
   present; the exact header `Version` label appears as a changelog entry;
   changelog version labels unique. A module- and inline-comment states this
   does **not** prove no historical version was silently skipped (review
   responsibility).
3. `test_canonical_main_shas_match_between_documents` — parses the
   `Canonical main SHAs` value from **each** file's header table, trims only
   surrounding whitespace, and requires the two byte-identical.

Commit `b95aa79`.

## Task 4 — CURRENT_STATUS self-update (two-tier rule demonstration)

Exactly two edits in `CURRENT_STATUS.md`, per the rule that the executor
updates it as the final substantive state step of an approved task:

- "Active branches (repo-qualified)" programme-level entry →
  ``0-programme` · `docs/programme-state-v1` — pushed by the landing task;
  awaiting post-push review.`
- "Pending reviews" placeholder line →
  ``0-programme` · `docs/programme-state-v1` — awaiting Discriminator + PI
  review on clean clones.`

Nothing else changed; the header table (incl. `Canonical main SHAs`) is
untouched, so the Task-3 SHA-consistency guard still passes. Commit `9612507`.

Resulting `CURRENT_STATUS.md` sha256 (post-edit):

```
f5f4a9c033d3a35ea01448318b8d5c198e78e75381e40a489db9bc3aceb78186  CURRENT_STATUS.md
```

This **differs** from the Task-1 landing hash `5fb3fe46…` — **expected and
correct, not tampering**: the Task-1 hash pinned the approved *input* artifact;
Task 4 is the rule-governed task-final update applied on top of it.

## Tests / lint

- `python -m pytest` → **6 passed** (3 pre-existing structure tests + 3 new
  guard tests).
- `python -m ruff check .` → **All checks passed**.

## Allowlist compliance

Branch diff vs `origin/main` (`git diff --name-status`) — every path within the
allowlist, nothing outside it:

```
A  CURRENT_STATUS.md
M  README.md
A  docs/PROGRAMME_STATE.md
A  tests/test_programme_state_guard.py
A  reports/2026-07-21_programme-state-landing_report.md   (this file)
```

## Commit chronology (through pre-report HEAD)

```
210b7fd  docs: land canonical PROGRAMME_STATE v1.0 + CURRENT_STATUS (approved)
c842fcb  docs: README reading-order pointer to canonical programme state
b95aa79  test: governance guard for canonical programme-state documents
9612507  status: CURRENT_STATUS updated per two-tier maintenance rule (task-final step)
```

Pre-report HEAD = `9612507`. The report-only commit is the true last commit;
per the self-reference rule its own SHA is **not** recorded inside this file —
it appears only in the executor's final response, together with the post-push
`git ls-remote`.

## Remote state (origin `0-programme`, at report authoring, pre-push)

```
572b24b  refs/heads/claude/sea-ice-framework-stubs-kfqjd9
b399e11  refs/heads/main
8b0d370  refs/heads/sync/programme-state-2026-07-16
```

`docs/programme-state-v1` is pushed after this commit; its head SHA and the
updated `ls-remote` are recorded in the executor's final response.

## Observation for reviewers (no action taken)

The landed canonical `Canonical main SHAs` field records Paper 2 as `20f96f1`.
This value is part of the approved, hash-pinned artifact and was **not** edited.
It differs from the Paper 2 `main` HEAD `e21f81e` produced by the immediately
preceding Sea–Ice merge task in this environment; reconciling the canonical P2
SHA against the live Paper 2 `main` is a review/amendment matter (§1.4), outside
this docs-only landing.

## Status

Tasks 1–5 complete on `docs/programme-state-v1`. **Not merged, no PR** — pushed
and stopped for Discriminator + PI review on clean clones, per the prompt.
