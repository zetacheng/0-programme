# Programme-Level Gates

This registry contains programme-level gates only. Detailed paper gates remain in their owning paper repositories and must not be duplicated here.

Allowed status values are `PROPOSED`, `SPECIFIED`, `OPEN`, `RUNNING`, `PASS`, `FAIL`, `INCONCLUSIVE`, `SUSPENDED`, and `RETIRED`.

## PROG-SYNC-01 — P5-OMEGA-01 cross-repository synchronization review

Status: OPEN

### Cross-paper question

Do Papers 1, 3 and 5 describe as open or live the continuum topological-stability gate that PF-006 records as failed?

### Upstream repositories and gates

- `zetacheng/kappa-c2a`, branch `topo-mass-radius` at `6a20b05e0899a878fde214c44cf77a8610d7516f`, especially `results/topo_verdict.txt`;
- `paper-owned:5-topological-sector#P5-OMEGA-01`;
- accepted omega inputs from `paper-owned:3-vector-sector#P3-VEC-O3` and `paper-owned:3-vector-sector#P3-OMEGA-01`;
- PF-006 in `programme/FAILURE_REGISTER.md`.

### Downstream consequences

- Paper 1: the unmerged v16.3 governance branch describes the failed negative-quartic-plus-endogenous-omega continuum route as live with open gates; conflict confirmed.
- Paper 3: v3.11 still describes the omega kernel as input to a separate topological-stability gate with a future kill criterion; tense/status synchronization conflict confirmed only. Its omega derivation and verified claims remain intact.
- Paper 5: v0.23 explicitly says “continuum-radius gate open”; conflict confirmed.
- All paper edits are deferred to separate PI decisions.

### Locked assumptions

This review distinguishes the failed continuum \(B=1\) EFT route from the conceptually separate interface/wrinkle route and from any unresolved cutoff-scale lattice object. It does not test whether the full microscopic lattice theory contains a baryonic object and does not generalize PF-006 to every stabilization mechanism.

### Required evidence

Proof by direct, verbatim quotation from each authoritative paper source, recording repository, exact ref and full SHA, file, version, section, contextual interpretation, conflict disposition, minimal deferred edit, and affected claims. The legacy interface/wrinkle distinction must also be checked directly.

The evidence record is `reviews/PROG-SYNC-01.md`.

### Kill criterion

This gate is not designed to force a conflict. For any paper, the conflict is refuted in that paper's favour if direct quotation and context show that it does not describe the failed gate as open. Each paper must be classified `CONFLICT CONFIRMED`, `CONFLICT REFUTED`, or `UNVERIFIED`.

### Reviewer verdict

Quotation audit completed:

- Paper 1: `CONFLICT CONFIRMED` on the unmerged governance branch.
- Paper 3: `CONFLICT CONFIRMED` for tense/status synchronization only.
- Paper 5: `CONFLICT CONFIRMED` on `main`.

This is a synchronization finding, not a new scientific calculation or a paper-edit authorization.

### PI decision

PENDING.

### Synchronization actions

- Defer all paper edits.
- Do not merge the Paper 1 governance branch until the failed route is distinguished from the interface/wrinkle route and no longer called live.
- Later narrow P5-CL-008 to the tested one-loop EFT claim before marking that narrowed claim `FAILED`.
- Later change one Paper 3 sentence from future/open framing to a closed negative downstream gate without changing Paper 3's verified omega results.
- Import or reference the authoritative `topo-mass-radius` evidence in Paper 5.

### Date opened

2026-07-17

### Date closed

Open pending PI decision.

## Gate template

```markdown
## PG-XXX — Programme gate title

Status: PROPOSED

### Cross-paper question

### Upstream repositories and gates

### Downstream consequences

### Locked assumptions

### Required evidence

### Kill criterion

### Reviewer verdict

### PI decision

### Synchronization actions

### Date opened

### Date closed
```
