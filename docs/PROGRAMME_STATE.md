# Programme State

**Canonical programme state for the H(4) lattice-fermion condensate research programme.**
This is the single document every AI session, executor, and reviewer reads first,
before reading the repositories. If this document and a paper repository disagree,
**the paper repository wins**, and this document must be corrected through the
amendment process in §1.4.

| Field | Value |
|---|---|
| Version | 1.0 |
| Date | 2026-07-21 |
| Status | CANONICAL — approved for landing |
| Canonical main SHAs | `0-programme` `b399e11` · P1 `4307e1c` · P2 `20f96f1` · P3 `8c363ef` · P4 `60939f8` · P5 `234c458` |
| Generator (this version) | Claude |
| Discriminator (this version) | ChatGPT — review completed 2026-07-21 (structure, governance, and word-named evidence classes approved) |
| Approved by | PI (Zeta), 2026-07-21 |

Amendment rule: every change to this file follows Generator → Discriminator
review → PI approval → executor merge, with a version bump and a one-line
changelog entry (§8). Never rewrite silently.

---

## 0. Programme overview

Derive spacetime, gravity, dark matter, and dark energy from a Planck-scale
H(4) lattice fermion condensate. The original unified manuscript (rejected by
IJMPD for scope/presentation) was decomposed into a five-paper series, one
repository per paper, plus a programme-level repository (`0-programme`) holding
cross-paper registries and the Sea–Ice physical narrative.

Method: honesty-first, pre-registered numerical experiments. Gates are
registered before computation; negative results are recorded with the same
prominence as positive ones; retractions carry version numbers; silent
rewrites are forbidden.

## 1. Governance

### 1.1 Roles are hats, not identities

- **PI (Principal Investigator — Zeta)** — proposes research directions and physical intuitions
  (S³ proposal, S²/Hopf layer, Sea–Ice framing, U(1)_A condition, …),
  authorizes experiments and merges, makes final programme decisions.
  **The only party holding authorization power.** Not permanently labelled
  "generator".
- **Generator** — the AI currently drafting, integrating, or revising a
  prompt or document together with the PI.
- **Discriminator** — the AI currently performing adversarial review of a
  finished artifact (prompt, branch, document): stress-testing, hunting
  loopholes, verifying independently on clean clones.
- ChatGPT and Claude alternate between Generator and Discriminator. The
  assignment follows model capability, context state, and quota — **the
  strongest model with sufficient context/quota preferentially takes the
  Discriminator hat.** The recent betaV arc happened to have ChatGPT as the
  final Discriminator; that is a factual record, not an institutional
  binding.
- **Executor ("Codex")** — the generic name for the execution layer (Codex
  or Claude Code, on the PI's machine). Writes code, runs validated
  computations, commits, and pushes, strictly per approved prompts. **Holds
  no physics adjudication power.** Reviewing AIs never perform git writes;
  they verify on clean clones fetched from GitHub.

### 1.2 Merge protocol

A merge requires all three: (1) independent Discriminator review;
(2) PI authorization; (3) executor execution. There is no rule that a
specific named model must approve.

Mechanics: canonical reports are written by the executor into `reports/`;
reviewers read from GitHub. Merges are `--no-ff`, never squash/force/
delete-branch; merge the pinned SHA, not the branch ref; verify remote refs
upfront; docs-only diffs use allowlists where applicable.

### 1.3 Artifact discipline

Artifacts land byte-for-byte unmodified; metadata external; payload hashes
in sidecars. A commit can never contain its own SHA; final SHAs appear only
in the executor's final response. A raw output JSON never contains its own
file hash (external sidecar only).

### 1.4 Amendment of this document

This file is maintained **by the programme, not by any single model**:
Generator drafts the amendment → Discriminator reviews → PI approves →
executor merges with a version bump. A session's private understanding never
becomes programme state without passing this chain.

**Two-tier maintenance rule:** `PROGRAMME_STATE.md` (this file) always
requires the full chain above. `CURRENT_STATUS.md` is the fast-changing
companion and is exempt from a separate chain: the executor updates it as
the **final substantive step of any approved task, immediately before the
report-only commit**, so each update inherits that task's review and
authorization. No update to either file may occur outside
an approved task.

### 1.5 Known reliability facts

Every AI's independent verification is fallible. Recorded cross-review
catches in the betaV arc included a wrong momentum basis, a wrong q→0
interpretation, and a mutation-sign omission — each caught by an
independent reviewer. (Attribution of individual errors lives in canonical
reports and reliability logs, not in this constitution.) Multi-AI
cross-review is the epistemic machine itself; it is never skipped, and each
AI flags its own errors to the PI as reliability data.

## 2. Repository map

| Repo | Scope | Canonical main | State (one line) |
|---|---|---|---|
| `0-programme` | Cross-paper registries, Sea–Ice narrative, global gates | `b399e11` | Sea–Ice framework + research map + prereg policy merged; sync branch `8b0d370` unmerged (deferred) |
| `1-dark-matter-structure` | Galaxy phenomenology, SPARC, RAR, BTFR | `4307e1c` | v13 fix list registered, not yet executed; MNRAS targeted |
| `2-emergent-gravity` | Induced metric, spin-2, EH term, induced source | `20f96f1` | betaV recovery arc complete on main; decisive-campaign prereg in flight (§4) |
| `3-vector-sector` | Four-fermion vector channels, RPA, ω sector | `8c363ef` | No natural-coupling below-threshold bound state; survives as conditional sign mechanism; `bs_induced_gv.py` recovery pending |
| `4-dark-energy-cosmology` | Equilibrium vacuum, dark energy, Sea–Ice interface | `60939f8` | Re-scoped after Q≡0 machine proof; surviving χ_top candidates: gravitational R R̃, Berry–Hopf |
| `5-topological-sector` | U(2)/U(3) topology, Hopf, Skyrme, WZW, baryons | `234c458` | Internal-dimension working note v0.19; overlap-frame campaign superseded Wilson-frame table |

Cross-paper rule: cross-paper inputs remain links/references; the same
derivation is never duplicated and allowed to diverge.

## 3. Physics consensus

### 3.1 Established negative results (equal epistemic weight to positives)

- **Tensor-channel graviton is dead**: σ_μν is antisymmetric, so its
  coupling to the symmetric Σ vanishes identically; the NJL tensor channel
  yields a Kalb–Ramond field, not h_μν. The programme pivoted to the
  Sakharov induced-gravity route.
- **The minimal condensate fails its own survival condition** in the clean
  regime: ξ_ind ≈ −L/6 < 0 — the minimal model cannot self-generate a
  positive M_Pl² from first principles. (Honest prior for SI-2 is therefore
  biased FAIL, compounded by the repulsive G_ω = −G/N headwind.)
- **Exclusivity theorem**: the same angular mode cannot be both dark energy
  (m_θ ~ H₀, cannot clump) and a galactic superfluid medium — Papers 1 and
  4 cannot share that degree of freedom.
- **Fermion-kernel index gives Q≡0** for all chiral backgrounds (machine
  proof) — Paper 4 re-scoped accordingly.
- **The Yukawa kernel is the wrong functional form** for recovering MOND;
  non-universal per-galaxy masses were the symptom. Correct target: a
  k-mouflage/AQUAL nonlinear kernel with one universal a₀ ~ Λ_DE²/M_Pl.
- **The old three-phase confinement mechanism is retired** (diagonal
  currents commute; SU(3) was never derived); the question is repositioned
  as the U(3) seed's baryonic-topology programme.

### 3.2 Standing structural results

- Paper 2's recovered gravity engine reproduces: speed_check exactly
  (ξ_χ=−0.0777, ξ_f=−0.250); β_B ≈ +2.6e-4; the sign β_V < 0. The ratio
  magnitude is grid-limited at small n and **not reproduced**; `−3.2(5)`
  remains quarantined (§4).
- The Solodukhin quotient `Γ_Proca = Γ_minvec − Γ_scalar` is a **β-level**
  statement: the flat determinants differ by an ultralocal m² longitudinal
  factor with no propagating log. Pointwise Z equality must never be
  demanded.
- The audit of that identity is not an output-algebra tautology
  (`M_minvec = M_Proca + M_gf` with an independently constructed
  gauge-fixing block; β_gfvec from an independent loop). Narrow scope: a
  PASS shows the implementation and extraction consistently obey the
  identity; it does not clear the historical −3 of target-aware
  circularity (Phase-1 record stands) and does not independently prove
  nature's vector contribution is −3.
- Phase-1 and the historical session converged independently on the
  gauge-fixed/Stueckelberg construction: **convergent evidence, never
  "mutual verification".**
- R10 and R12 use different mass windows (0.11–0.20 vs 0.125–0.55) and are
  never collapsed.
- `ward_analysis_summary.txt` (claims Z_cov < 0; positive axis slope an
  artifact of the non-covariant c4 term) is **recorded, NOT adopted**;
  generating code is MISSING #1. If ever verified it bears on the M_Pl²
  sign and SI-2 priors.

### 3.3 Sea–Ice framework (interpretation layer)

Sea–Ice is a physical narrative **lens**: it owns no claim, gate, or
evidence; every testable proposition is owned by a paper-level gate; when
the framework and a paper disagree, the paper wins. Hierarchy: Sea
(lattice-fermion collective phase) → Ice (stable condensed phase =
observable spacetime) → Sea–Ice interface (dark energy = interface
stress-energy) → interface wrinkles → bound excitations (dark matter).

Gate aliases: SI-0=`P2-BETAV-CIRC-01`; SI-1 prerequisite=
`P2-CHANNEL-FREEZE-01`; SI-1=`P2-PHASE-01`; **SI-2=`P2-MULTIPHASE-GRAV-01`**;
SI-3…SI-6 in Papers 4/1, all conditional on SI-2 CLEAN PASS.

**Scope of "programme-death"**: SI-2 is the death gate **of the Sea–Ice
emergent-gravity unification route**. A CLEAN FAIL severs SI-3→SI-6 and the
minimal-model positive-gravity mainline; it does **not** invalidate Paper
1's empirical results, Paper 3's conditional mechanisms, or the topological
programme.

## 4. Current active campaigns

### 4.1 betaV decisive-campaign pre-registration (Paper 2) — IN FLIGHT

Rebuilds the historical, never-executed `precision_campaign.py` under
modern blind discipline. Serves two strictly distinct gates:
`P2-BETAV-CIRC-01` (operator/determinant-identity audit, SPECIFIED) and
`P2-BETAV-NUMREPRO-01` (historical `−3.2(5)` reproduction, PROPOSED).
`P2-C9` PROPOSED; `−3.2(5)` quarantined — the quarantine enforces the
programme's **own historical promotion criterion** (the campaign that was
supposed to establish it never ran), not a retroactive standard.

**Three distinct outputs, never conflated**: (1) CIRC audit verdict;
(2) Arm-H NUMREPRO verdict; (3) Arm-P historical-promotion-criterion
outcome. CIRC PASS + NUMREPRO PASS is necessary but **not sufficient** for
quarantine release; the Arm-P 5% targets can independently FAIL. Canonical
rule: quarantine release or `P2-C9` promotion requires the registered
dual-gate conditions AND explicit consideration of the separately recorded
Arm-P outcome, followed by PI+reviewer authorization. **No script
automatically promotes.**

Prompt version history: v3 (initial + two review rounds) → v4 (ChatGPT's
two core statistical fixes: dimensionless resolving-power ceiling
`δ_audit=0.05` forbidding "noisier ⇒ easier PASS"; strict verdict vs
diagnostic-only variant separation; plus τ_Z scale, pilot-amendment
invalidation, registered source-hash set) → **v5** (n=6 probe downgraded to
a non-adopted motivating note; three-output canonical wording; Arm-H
confound treatment).

**Open decisions blocking execution (Discriminator to rule, then PI to
authorize):**
1. Arm-H **window-shift** classified as a VERDICT variant (it is the R10
   subwindow systematic, the dominant term of σ_H; excluding it would
   artificially shrink the NUMREPRO uncertainty).
2. Arm-H confound resolution, **option A vs B**. A (Generator-proposed):
   uniform `with_m4=False` primary basis for all Arm-H mass-set variants —
   removes both the drop-one and window-shift mass/basis confounds;
   baseline gains dof=1. B (fallback, original Discriminator suggestion):
   keep `with_m4=True` baseline and honestly label all mass-set variants
   as mixed `mass-drop-one + forced reduced-basis`, with an attribution
   caveat on σ_H. Exactly one must be frozen before the executor runs.

Pre-registered honest expectations (frozen): Arm H is likely INCONCLUSIVE
even under perfect reproduction of −3.2(5) (window sensitivity — a
statement about the configuration's discriminating power, not the
identity); Arm P's historical gfvec/B (−2.4…−2.9) lies outside the
promotion band [−2.10, −1.90], so a promotion-criterion FAIL is a live
possibility.

Task scope when executed: prereg doc → blind harness → NON-DECISIVE pilot →
gate bookkeeping → report → STOP. Decisive Arm H (n=32) then Arm P (n=48,
may run on the PI's machine with the frozen harness) require separate
step-by-step authorization.

### 4.2 Other pending work (priority order)

1. Recovery routing of files held by the PI: `fiducial_rerun.py` +
   `cluster_test.py` → Paper 1; `bs_induced_gv.py` → Paper 3 (the
   BS/induced-G_V open gate's historical object — high value);
   `wzw_flow.py` + `skyrme_sign2.py` → Paper 5. Same discipline: verbatim,
   sha256, dedup, no gate outcomes.
2. MISSING hunt (`2-emergent-gravity/scripts/recovered_2026/MISSING.md`):
   #1 ward-complete vierbein-link kernel (would verify Z_cov<0); #6 the
   finite-q position-space full-determinant validation script; residue:
   standalone n=32 driver, fermion-mlog driver (β_Dirac/β_B=2), fig_mlog
   generator. Sources come from the PI only — never synthesized.
3. SI-1 critical path: `P2-CHANNEL-FREEZE-01` (Fierz foundations validated
   on main; groundwork ready) → `P2-PHASE-01` → SI-2.
4. Deferred: 0-programme PROG-SYNC-01 (`8b0d370`); docs cleanup (P1 v16.4
   typo; P5-CL-015 stale pointer); Paper 1 v13 fix list.

## 5. Evidence hierarchy

**Programme-level evidence classes (named labels, deliberately not
lettered — see note below):**

| Class | Meaning | Examples |
|---|---|---|
| **CANONICAL** | Merged to main, Discriminator-reviewed, PI-approved; citable as programme state | Paper 2 recovery-arc reports; gate registry entries |
| **RECOVERED-SOURCE** | Historical source code recovered byte-for-byte, hash-sealed, not independently re-run at the claimed configuration | `precision_campaign.py`; `gfvec_loop.py` before campaign execution |
| **RECOVERED-RECORD** | Historical logs/notebooks/transcribed values; design-rationale evidence, never numerical verification | `session_log_full.md`; the 15-row run-record index; R10/R12 numbers |
| **EXPLORATORY** | Ad-hoc probes without branch/commit/hash/environment record, not independently reviewed, **not adopted** | the n=6 gf-seagull slope probe |
| **HYPOTHESIS** | Registered expectations and physical narratives awaiting their gates | Sea–Ice interpretation; pre-registered expectations before runs |

Rules: evidence classes classify **how an artifact or number is being
used to support a claim**, not merely whether the file exists on a
canonical branch — the same file may be CANONICAL as a recovered artifact
while numerical claims derived from an unexecuted historical configuration
remain RECOVERED-SOURCE (e.g. `gfvec_loop.py`). An EXPLORATORY observation
may motivate a pre-registered expectation but is never cited as evidence;
promotion between classes only through the governance chain; a report must
state the class of every number it quotes.

**Relation to the existing historical-provenance classes (do not confuse):**
within RECOVERED-* material, Paper 2's PROVENANCE files classify individual
historical numbers as A (source code) / B (saved outputs) / C
(printed-transcribed) / D (memory). That A–D ladder is a
**sub-classification inside the RECOVERED layers** and keeps its letters;
the programme-level classes above deliberately use words, not letters, to
avoid collision. *(Word-named programme classes approved by the Discriminator, 2026-07-21.)*

## 6. Open questions

- Can the campaign's Arm P pull gfvec/B from the coarse −2.4…−2.9 to the
  −2.0 target at the historical fine configuration?
- Ward/vierbein Z_cov sign: recorded-not-adopted claim awaiting MISSING #1.
- SI-2: can any multi-channel structure overcome ξ_ind < 0 and the
  repulsive ω channel? (Honest prior: FAIL.)
- K(X) EOS shape derivation for Paper 1 (a₀ to be fitted, not fixed, given
  the factor-of-two discrepancy).
- χ_top: gravitational R R̃ vs Berry–Hopf vs η-Hopf (third candidate,
  registered).
- Whether the strong historical non-circularity question (Phase-1) can ever
  be closed by any implementation-level audit (current answer: no — all
  steps linear).

## 7. Next governed actions

1. Discriminator rules on the two open v5 decisions (§4.1) and gives the
   prompt a final verdict.
2. PI authorizes; executor runs the prereg task (Part 0 → prereg → harness
   → non-decisive pilot → gate bookkeeping → report → STOP).
3. Discriminator + PI review the branch on clean clones; merge per §1.2.
4. Separate authorizations: decisive Arm H, then decisive Arm P.
5. In parallel, as PI provides files: the three recovery-routing prompts
   (§4.2.1).

## 8. Changelog

- **1.0 (2026-07-21)** — approved canonical version. Discriminator review
  completed (word-named evidence classes approved); PI approval recorded.
  Changes from 1.0-draft: §1.5 depersonalized (error attribution moved to
  reports/logs); §5 claim-use classification rule added; §7 retitled "Next
  governed actions"; §1.4 two-tier wording fixed to "final substantive
  step before the report-only commit"; PI expanded to Principal
  Investigator on first use; header approvals recorded.
- **1.0-draft (2026-07-21)** — first canonical draft, produced from the
  bilingual consensus document v2 after two Discriminator review rounds;
  restructured per Discriminator proposal (canonical location, English,
  evidence hierarchy, collaboration protocol, version header, governed
  maintenance).
