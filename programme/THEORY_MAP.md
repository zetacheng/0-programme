# Programme Theory Map

Scientific dependencies have not yet been reviewed. The diagram records repository coordination only.

## Current physical interpretation — Sea–Ice (PROPOSED)

The Sea–Ice framework is the current physical interpretation of the
lattice-fermion programme. It supplies ontology and vocabulary but **owns
no evidence**: every testable proposition it makes is owned, tested, and
killed by a paper-level gate in a paper repo, bound there by the
CLAIMS↔GATES guard. The framework lives in `sea-ice/`
(`SEA_ICE_PHYSICAL_FRAMEWORK.md`, `SEA_ICE_RESEARCH_MAP.md`,
`SEA_ICE_PREREGISTRATION_POLICY.md`); the programme-gate aliases are listed
in `GLOBAL_GATES.md` and the critical chain in `DEPENDENCIES.md`.

```mermaid
flowchart TB
    P0["0-programme"]
    P1["Paper 1 — Dark Matter Structure"]
    P2["Paper 2 — Emergent Gravity"]
    P3["Paper 3 — Vector Sector"]
    P4["Paper 4 — Dark Energy and Cosmology"]
    P5["Paper 5 — Topological Sector"]

    P0 --- P1
    P0 --- P2
    P0 --- P3
    P0 --- P4
    P0 --- P5
```
