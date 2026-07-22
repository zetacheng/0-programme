# Current Status

One-page live status. Read this first (2 min), then
`docs/PROGRAMME_STATE.md` (10 min), then the repositories. Maintenance:
this file is updated by the executor as the final substantive step of any
approved task, immediately before the report-only commit (inheriting that
task's review); `PROGRAMME_STATE.md` changes only through the full
amendment chain (its §1.4).

| Field | Value |
|---|---|
| Date | 2026-07-21 |
| Canonical main SHAs | `0-programme` `b399e11` · P1 `4307e1c` · P2 `20f96f1` · P3 `8c363ef` · P4 `60939f8` · P5 `234c458` |

## Current active campaign

**Paper 2 betaV decisive-campaign pre-registration** (prompt v5). Blind
harness + non-decisive pilot for the operator-identity audit
(`P2-BETAV-CIRC-01`) and historical reproduction (`P2-BETAV-NUMREPRO-01`).
`−3.2(5)` quarantined. Decisive Arm H / Arm P forbidden until separately
authorized.

## Active branches (repo-qualified)

**Programme-level (documentation):** `0-programme` · `docs/programme-state-v1` — pushed by the landing task; awaiting post-push review.

**Research-level (Paper 2):** none on origin yet;
`2-emergent-gravity` · `gate/p2-betav-campaign-prereg` will be created by
the executor once prompt v5 is approved. (Verified 2026-07-21: both
branches absent on origin.)

## Next task

1. Discriminator (current round: ChatGPT) rules on the two open v5
   decisions: (a) Arm-H window-shift = VERDICT variant; (b) Arm-H confound
   resolution, option A (uniform `with_m4=False` basis) vs option B (mixed
   variants, honest labels).
2. PI authorizes → executor runs the prereg task and STOPs at the report.

## Blocking issues

- The two v5 open decisions above (block the Paper 2 prereg executor
  start). The programme-state landing is not blocked: Discriminator review
  and PI approval were completed 2026-07-21.

## Pending reviews

- Prompt v5 (`CODEX_PROMPT_betav_campaign_prereg_v5.md`) — Discriminator
  ruling on the two open Arm-H decisions, then final verdict.
- `0-programme` · `docs/programme-state-v1` — awaiting Discriminator + PI review on clean clones.

## Deferred / background

- 0-programme sync branch `8b0d370` unmerged (PROG-SYNC-01).
- Recovery routing to Papers 1/3/5 (files with the PI).
- MISSING hunt (top: #1 ward vierbein kernel, #6 finite-q validator).
- Paper 1 v13 fix list; docs cleanup (P1 v16.4 typo, P5-CL-015 pointer).
