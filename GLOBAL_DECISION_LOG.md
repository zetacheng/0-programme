# Global Decision Log

This log is append-only. Corrections must be recorded as new decisions that identify what they supersede.

## 2026-07-15 — Programme decision

### Decision

Separate the five papers into independent repositories and establish 0-programme as the master coordination repository.

### Reason

Establish explicit ownership, synchronization, and cross-paper governance boundaries.

### Evidence

Programme infrastructure directive approved by the Principal Investigator.

### Affected papers

Papers 1–5.

### Required synchronization

Register each paper repository and initialize programme-level synchronization tracking.

### Supersedes

None.

### Related gates and repositories

`zetacheng/0-programme` and the five paper repositories. No scientific gate is assigned during initialization.

## 2026-08-08 — Cross-paper conventions registry: authority ruling and first import

### Decision

`0-programme/CROSS_PAPER_CONVENTIONS.md` is authoritative for the CURRENT cross-paper convention value used by downstream work (PI ruling, 2026-08-08). Paper repositories retain their historical and frozen statements as evidence of what was used at each revision and hold the derivation or ruling that establishes each value; new downstream work cites the programme registry. The authority centralised is the VALUE, not the derivation, consistent with `AGENTS.md` programme rules 2 and 3. Any disagreement between a paper artifact and the registry is recorded and explicitly resolved, never silently overridden; historical artifacts are never silently rewritten.

Under this ruling, the first import populates six registry rows from established Paper-2 material and records one row as `NOT DEFINED`: Metric signature; Euclidean exponent mapping (new row, inserted after Wick rotation); Gamma matrices and gamma5; Flavor generator normalization; Interaction normalization; Definitions of \(G\), \(G_V\), \(G_\omega\); and Sign convention for attraction and repulsion (`NOT DEFINED`). The file's former closing sentence ("This file does not override a paper's convention registry automatically.") is replaced by the ruling above, and a legend distinguishing a populated value, `NOT DEFINED`, and `NOT YET IMPORTED.` is added. Every other row stays `NOT YET IMPORTED.`.

### Reason

`γ₅` was found carrying two different definitions inside Paper 2 — one in the Phase-A freeze, one in the `CANONICAL_INTERACTION.json` companion — and the discrepancy survived because nothing held a single authoritative value. A registry each paper cites removes the mechanism by which duplicated copies drift.

### Evidence

External evidence base `zetacheng/2-emergent-gravity @ 51d4bbe1a2e965b0793b18f4ead5a11dab54c364` (read-only): `derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` (metric signature; gamma/gamma5 basis; flavor-generator normalization; interaction normalization); `DECISION_LOG.md` entry 2026-08-08 (Euclidean exponent mapping ruling); `specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md` §8 (gamma5 companion-conflict ruling); `derivations/P2-NORMALISATION-AUDIT_g_omega.md`; `derivations/P2-PHASE-01_channel_character.md` (Sign convention `NOT DEFINED`). Paper-3 note `zetacheng/3-vector-sector @ 8c363ef08368f5c022278ea5f36e01496be3d5ca : derivations/u3-fierz/u3_fierz.md` (`G_omega = -G/N`). No paper repository was modified; no paper file was copied into `0-programme`.

### Affected papers

Paper 2 (source of the six imported values and the `NOT DEFINED` finding); Paper 3 (co-source for the `G_omega` row). No paper status is imported: this is a conventions audit only.

### Required synchronization

Record the audit in `SYNC_STATUS.md` (Paper 2 `Conventions audited` cell only). `MASTER_PROGRESS.md`, gates, claims, and paper status remain `NOT IMPORTED`.

### Supersedes

None. The former closing sentence of `CROSS_PAPER_CONVENTIONS.md` is replaced within this decision; no prior decision-log entry is superseded.

### Related gates and repositories

`zetacheng/0-programme` (this registry); `zetacheng/2-emergent-gravity @ 51d4bbe1`; `zetacheng/3-vector-sector @ 8c363ef0`. No scientific gate is registered or closed.

## Entry template

```markdown
## YYYY-MM-DD — Programme decision

### Decision

### Reason

### Evidence

### Affected papers

### Required synchronization

### Supersedes

### Related gates and repositories
```
