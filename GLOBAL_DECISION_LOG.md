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

## 2026-07-17 — PROG-SYNC-01 quotation audit

### Decision

Record the quotation-based synchronization findings for PF-006 while deferring every paper edit and the final programme disposition to the Principal Investigator.

### Reason

The authoritative `topo-mass-radius` verdict closes the tested continuum EFT route negatively, so any paper that still calls that same route open or live is out of synchronization.

### Evidence

`reviews/PROG-SYNC-01.md` records verbatim source quotations and exact commits. The audit found:

- Paper 1: conflict confirmed on unmerged branch `claude/paper1-gated-repo-governance-z478hp` at `8f5c63c1206b81a09df810c62ba92122d074ca38`; the future-directions text calls the negative-quartic-plus-endogenous-omega route live with open continuum-radius gates.
- Paper 3: conflict confirmed narrowly at `main` commit `0cb95fe7052a675708999d44f66084e446a3d0bf`; the paper correctly disclaims stabilization but still frames the downstream gate prospectively. This does not undermine P3-C-001, P3-C-002, P3-C-004 or P3-C-005.
- Paper 5: conflict confirmed at `main` commit `6de940c4dcbdf419cda4ef7578de2066f6d9a9c5`; the status block says “continuum-radius gate open.”
- The distinct interface/wrinkle route was checked directly at `zetacheng/kappa-c2a`, branch `de-interface-wrinkle` commit `5ee543c9c7c37082c1053f438aa10a4a65ee7234`, and explicitly states that it is not the B=1 skyrmion gate.

### Affected papers

Papers 1, 3 and 5.

### Required synchronization

Separate later PI-authorized edits must narrow Paper 5's P5-CL-008 before failure promotion, update the Paper 5 gate status and verdict scope, correct one Paper 3 tense/status sentence, and remove Paper 1's live-route wording while preserving the interface/wrinkle distinction.

### Supersedes

None. PF-006 and the owning paper records remain preserved.

### Related gates and repositories

PROG-SYNC-01; `paper-owned:5-topological-sector#P5-OMEGA-01`; `zetacheng/1-dark-matter-structure`; `zetacheng/3-vector-sector`; `zetacheng/5-topological-sector`; legacy evidence in `zetacheng/kappa-c2a`.

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
