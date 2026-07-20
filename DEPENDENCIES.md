# Cross-Paper Dependency Registry

| Dependency ID | Upstream paper | Upstream result | Downstream paper | Use | Status | Evidence |
|---|---|---|---|---|---|---|
| SEAICE-CHAIN-01 | Papers 2, 4 | Sea–Ice critical path (paper-owned gates) | Papers 4, 1 | Sea–Ice programme critical chain (see below) | PROPOSED | `sea-ice/SEA_ICE_RESEARCH_MAP.md` |

No other scientific dependencies were entered during infrastructure initialization.

## SEAICE-CHAIN-01 — Sea–Ice critical chain

Status: `PROPOSED`. All evidence is paper-owned; this repo only routes.
The single source is `sea-ice/SEA_ICE_RESEARCH_MAP.md`.

    P2-BETAV-CIRC-01
        → P2-CHANNEL-FREEZE-01
        → P2-PHASE-01
        → P2-MULTIPHASE-GRAV-01
        → P4-SEA-ICE-01
        → { P4-INTERFACE-DE-01,
            P4-WRINKLE-BRIDGE-01 → P4-BOUND-DM-01 }
        → P1-SEAICE-RAR-01

## Status vocabulary

- `PROPOSED`
- `UNVERIFIED`
- `ACCEPTED`
- `SUSPENDED`
- `FAILED`
- `SUPERSEDED`

A downstream paper may not treat an upstream result as accepted unless the corresponding upstream gate is closed and accepted.
