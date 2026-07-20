# Programme-Level Gates

This registry contains programme-level gates only. Detailed paper gates remain in their owning paper repositories and must not be duplicated here.

Allowed status values are `PROPOSED`, `SPECIFIED`, `RUNNING`, `PASS`, `FAIL`, `INCONCLUSIVE`, `SUSPENDED`, and `RETIRED`.

No programme-level gates were entered during infrastructure initialization.

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

## Sea–Ice programme gates (aliases)

Status: PROPOSED

These `SI-x` labels are **routing aliases only**. Each is an alias for a
concrete paper-level gate that is **owned in the paper repositories, not
here** — it lives in that paper's `GATES.md`, is bound to that paper's
`CLAIMS.md` by the CLAIMS↔GATES guard, and its failure changes a paper
claim's status. Sea–Ice owns no evidence. The gate bodies (questions,
inputs, kill consequences, PASS classification) are **not** duplicated
here; the single source is `sea-ice/SEA_ICE_RESEARCH_MAP.md`.

| Programme alias | Paper-level gate (owner repo) | Pointer |
|---|---|---|
| SI-0 | `P2-BETAV-CIRC-01` (Paper 2) | see `sea-ice/SEA_ICE_RESEARCH_MAP.md` |
| SI-1 (pre-req freeze) | `P2-CHANNEL-FREEZE-01` (Paper 2) | see `sea-ice/SEA_ICE_RESEARCH_MAP.md` |
| SI-1 | `P2-PHASE-01` (Paper 2) | see `sea-ice/SEA_ICE_RESEARCH_MAP.md` |
| SI-2 (programme-death) | `P2-MULTIPHASE-GRAV-01` (Paper 2) | see `sea-ice/SEA_ICE_RESEARCH_MAP.md` |
| SI-3 | `P4-SEA-ICE-01` (Paper 4) | see `sea-ice/SEA_ICE_RESEARCH_MAP.md` |
| SI-4 | `P4-INTERFACE-DE-01` (Paper 4) | see `sea-ice/SEA_ICE_RESEARCH_MAP.md` |
| SI-5a | `P4-WRINKLE-BRIDGE-01` (Paper 4) | see `sea-ice/SEA_ICE_RESEARCH_MAP.md` |
| SI-5b | `P4-BOUND-DM-01` (Paper 4) | see `sea-ice/SEA_ICE_RESEARCH_MAP.md` |
| SI-6 | `P1-SEAICE-RAR-01` (Paper 1) | see `sea-ice/SEA_ICE_RESEARCH_MAP.md` |

The framework these gates test is described in
`sea-ice/SEA_ICE_PHYSICAL_FRAMEWORK.md`; freeze requirements are in
`sea-ice/SEA_ICE_PREREGISTRATION_POLICY.md`.
