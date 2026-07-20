# Sea–Ice Cosmology — Research Map

Status: PROPOSED
Version: draft 2026-07-19
Owner: `0-programme` (routing only; all evidence lives in paper repos)

Every Sea–Ice programme gate below is an **alias** for a concrete
paper-level gate. The paper-level gate is the real object: it lives in that
paper's `GATES.md`, is bound to that paper's `CLAIMS.md` by the CLAIMS↔GATES
guard, and its failure changes a paper claim's status. The `SI-x` label is
a routing convenience, not an independent gate.

New gate IDs introduced here were checked against the current `GATES.md`
of each repo (2026-07-19) and do not collide. Existing Paper 2 gates:
`P2-HK-01`, `P2-GAP-01`, `P2-BETA-01`, `P2-BETAV-01`, `P2-NORM-01`,
`P2-BETAV-CIRC-01`. New IDs (`P2-CHANNEL-FREEZE-01`, `P2-PHASE-01`,
`P2-MULTIPHASE-GRAV-01`, `P4-SEA-ICE-01`, `P4-INTERFACE-DE-01`,
`P4-WRINKLE-BRIDGE-01`, `P4-BOUND-DM-01`, `P1-SEAICE-RAR-01`) are clear.
**Before any of these is created in a paper repo, re-fetch that repo and
re-confirm no collision** — this map is a proposal, not the authority on
current IDs.

## Dependency chain (critical path)

    P2-BETAV-CIRC-01            (SI-0  validate the extraction pipeline)
        → P2-CHANNEL-FREEZE-01  (freeze the HS/Fierz basis + PASS metrics)
        → P2-PHASE-01           (SI-1  ∃ admissible stable phase?)
        → P2-MULTIPHASE-GRAV-01 (SI-2  ∃ robust healthy phase?  FAIL iff ∀ pathological  PROGRAMME-DEATH)
        → P4-SEA-ICE-01         (SI-3  derived finite-tension interface?)
        → { P4-INTERFACE-DE-01           (SI-4  interface → dark energy)
            P4-EQ-WRINKLE-01 → P4-BOUND-DM-01 }  (SI-5  wrinkle-bound DM)
              (P4-WRINKLE-BRIDGE-01 ⤏ evidence-transfer only, not a life gate)
        → P1-SEAICE-RAR-01      (SI-6  derive RAR + a_0)

**Resource warning — read before planning effort.** This is a near-linear
chain of eight hard gates, most of them `∀`-type or derive-from-scratch.
Chain survival is a product of per-gate survival: the programme's life is
decided, with high probability, at `P2-MULTIPHASE-GRAV-01` (the fourth
gate). Everything downstream of SI-2 is conditional to the point of being
hypothetical until SI-2 returns CLEAN PASS. Effort should be front-loaded
onto SI-0 → SI-2, not spread evenly across the eight. The downstream gate
designs are recorded now for completeness and to fix the kill criteria in
advance (AE-3), not because they are near-term work.

## Gate table

| SI | Owner | Paper gate | Question | Inputs | Kill consequence |
|----|-------|-----------|----------|--------|------------------|
| SI-0 | Paper 2 | `P2-BETAV-CIRC-01` | Does the `β_V` lattice extraction track a changed background, or return `-3` regardless? | `k≠1` curved-background lattice Proca; analytic target `R(k)=-(k+2)` | Extraction is circular → dependent numerical claims (Finding 5) downgraded before SI-1 proceeds |
| SI-1 | Paper 2 | `P2-CHANNEL-FREEZE-01` | (pre-req) Freeze the complete HS/Fierz channel basis and the CLEAN-PASS metric before any multiphase scan | four-fermion interaction; complete bilinear basis; Fierz identities | — (a freeze, not a test; but SI-2 may not run until this is committed with a hash) |
| SI-1 | Paper 2 | `P2-PHASE-01` | Does the fixed theory possess ≥1 physically admissible stable condensed phase (the Ice)? | frozen channels; `Γ[Φ_i]`; finite density/μ | No admissible phase anywhere in the frozen space → simplest framework terminates |
| SI-2 | Paper 2 (primary), Paper 3 (dependency) | `P2-MULTIPHASE-GRAV-01` | **Programme-death.** Does *at least one* admissible stable phase produce healthy gravity (∃)? FAIL iff *every* admissible phase is pathological (∀). | every phase from SI-1; full `K_ij(p)` incl. all frozen-channel mixing; Paper 3 vector input | `∀ Φ: ¬HealthyGravity(Φ)` → **simplest lattice-fermion Sea–Ice programme terminated** |
| SI-3 | Paper 4 | `P4-SEA-ICE-01` | Do two admissible phases support a stable finite-tension microscopic interface? | Paper 2 phase pair; `V_eff(Φ)`; kinetic terms | No interface between any registered admissible phase pair → Sea–Ice realization fails even with healthy homogeneous gravity |
| SI-4 | Paper 4 | `P4-INTERFACE-DE-01` | Does the interface's 4D stress-energy account for the observed DE scale? **(high-risk magnitude gate)** | derived interface; upstream parameters | Wrong sign / outside pre-registered `ρ_DE` window / no accelerating solution / needs inserted Λ → interface-DE mechanism rejected (→ Outcome B possible) |
| SI-5-exist | Paper 4 | `P4-EQ-WRINKLE-01` | (existence) Does the microscopically derived interface *independently* support a stable or dynamically generated equilibrium wrinkle background — from its own fluctuation spectrum / nonlinear EFT, regardless of the old driven result? | SI-3 interface; interface fluctuation spectrum; nonlinear interface EFT | Derived interface supports no trap-capable wrinkle → wrinkle-bound DM has no background → SI-5 fails |
| SI-5-id | Paper 4 | `P4-WRINKLE-BRIDGE-01` | (identity / evidence-transfer, **not a life gate**) Is the SUPPORTED driven wrinkle (`P4-CL-002`) continuously/dynamically connected to the derived equilibrium wrinkle? | driven pattern; `P4-EQ-WRINKLE-01` background | FAIL blocks *inheritance* of `P4-CL-002` as precedent only; it does **not** kill `P4-EQ-WRINKLE-01` or `P4-BOUND-DM-01` |
| SI-5-spec | Paper 4 (primary), Paper 5 (boundary) | `P4-BOUND-DM-01` | (spectrum) Does the equilibrium wrinkle trap normalizable, long-lived, pressureless, clustering bound modes? | `P4-EQ-WRINKLE-01` background; fluctuation operator `O_fluct` | No such mode → wrinkle-bound DM rejected; may not revert to the Paper 5 continuum soliton |
| SI-6 | Paper 1 | `P1-SEAICE-RAR-01` | Does the effective theory *derive* the RAR and a universal `a_0`, without inserting the empirical interpolation? | interface elastic response; bound-mode response; modified Poisson kernel | RAR must be inserted / `a_0` freely fitted / wrong shape / lensing-dynamics mismatch → galactic explanation fails |

## SI-2 PASS classification (the programme-death gate)

`P2-MULTIPHASE-GRAV-01` returns one of three verdicts. The thresholds
distinguishing them are themselves pre-registered (see AE-3 and the
preregistration policy) — this is required, because otherwise "CLEAN vs
CONDITIONAL" becomes a retrospective judgement, reopening the escape AE-3
closes.

- **CLEAN PASS** — a healthy phase exists on a parameter region of
  **positive volume** under the *pre-registered measure*, at least the
  *pre-registered minimum healthy volume*, and stable under small parameter
  perturbation. Only CLEAN PASS supports continuing into Sea–Ice cosmology.
- **CONDITIONAL PASS (fine-tuned)** — a healthy phase exists only at an
  isolated point, on a zero-measure surface, in a tuning band narrower than
  the registered minimum, or requires fine cancellation. Permits technical
  follow-up; **must not** be written as a theoretical success.
- **FAIL** — every admissible phase is gravitationally pathological
  (negative Newtonian coupling, negative-residue physical pole,
  unavoidable ghost or tachyon, or no viable long-range mode). Hard
  consequence per AE-1.

## Cross-repo dependencies must be pinned

Every dependency on another paper's result must cite a **pinned commit
SHA** (or tag), not just the paper name — otherwise a later update to that
paper silently changes what this gate depends on. Specifically:

- `P2-MULTIPHASE-GRAV-01`'s Paper 3 vector input must record: which Paper 3
  claim/gate (`P3-C-001` / `P3-FIERZ-01`), the `3-vector-sector` commit
  SHA, the `G_ω = -G/N` and screening-formula conventions, and exactly
  which `K_ij` entries Paper 3 supplies.
- `P4-BOUND-DM-01`'s Paper 5 boundary must record the `5-topological-sector`
  commit SHA at which `P5-OMEGA-01` FAILED, so the scope statement
  (`P5-OMEGA-01 ⇏ P4-BOUND-DM-01 FAIL`) is tied to a fixed result.

## Paper 3's role — constrained input, not a rescue branch

Paper 3 enters SI-2 only as an interaction input to `K_ij(p)`, and enters
SI-5b as bound-mode self-interaction / screening / decay. Its known
negative result stands and is load-bearing: increasing the nominal vector
coupling does **not** automatically strengthen anything, because the
response saturates/screens (`D_00 = g_0/(1+g_0 Π_V) → 1/Π_V`). Paper 3 is a
`Supporting interaction sector, not an independent rescue branch`. In
particular its vector channel is repulsive (`G_ω = -G/N`), which is a
headwind for SI-2, not a help (see the framework doc's honest prior).

## How existing results map in (scope unchanged)

- **Paper 4 monopole** (`P4-CL-007`/`P4-MONOPOLE-01`, `S_mono=-0.95`):
  the monopole DE hierarchy is rejected. Does **not** test the interface
  stress-energy mechanism (`P4-INTERFACE-DE-01`).
- **Paper 4 driven wrinkle** (`P4-CL-002` SUPPORTED): wrinkles form and
  saturate in a driven EFT. Whether the *equilibrium* interface has its own
  wrinkle is the **existence** gate `P4-EQ-WRINKLE-01` (independent of the
  old result); whether that equilibrium wrinkle is the *same object* as the
  driven one is the **identity** gate `P4-WRINKLE-BRIDGE-01` (evidence
  transfer only). A bridge FAIL blocks inheriting `P4-CL-002` as precedent
  but does not kill the independently derived wrinkle or the bound-DM
  spectrum gate.
- **Paper 5 continuum object** (`P5-OMEGA-01` FAILED): the continuum
  topological DM object is excluded. This does **not** exclude
  interface-bound modes, whose localization comes from an independently
  derived interface, not from self-support of a continuum radius.
  Formally: `P5-OMEGA-01 ⇏ P4-BOUND-DM-01 FAIL`, and equally it lends the
  bound modes no support.
- **Paper 1 RAR** (`P1-CL-007` SUPPORTED): empirical RAR success is
  evidence for the *phenomenon*, not that the microscopic theory derives
  it. `P1-SEAICE-RAR-01` stays open until RAR and `a_0` come from the
  theory.
- **Paper 2 gravity** (`ξ_ind<0`, single channel): motivates
  `P2-PHASE-01` and `P2-MULTIPHASE-GRAV-01`; not erased. The simplest
  programme survives only if the exhaustive multiphase scan finds an
  admissible phase with healthy gravity.

## Paper–programme dependency (summary)

    Paper 2  microscopic phases + gravity   (SI-0, SI-1, SI-2)
        ↓
    Paper 4  interface, DE, wrinkles, bound modes  (SI-3, SI-4, SI-5)
        ↓
    Paper 1  galaxies, RAR, a_0             (SI-6)

    Paper 3 = interaction-sector input to Papers 2 and 4 (constrained)
    Paper 5 = exclusion boundary for invalid DM realizations

## Integration record

Integration date: **2026-07-20** (Sea–Ice review fixes applied and landed on
the paper stub branches before this map merged).

Source SHAs of the paper stub branches this map points at (branch
`sea-ice/gate-stubs` in each repo, pinned at integration time):

- `zetacheng/2-emergent-gravity` — `b02c70279b382e05d415b23b9b5f562e3c5e2156`
  (`P2-CHANNEL-FREEZE-01`, `P2-PHASE-01`, `P2-MULTIPHASE-GRAV-01`; Paper 3
  input pinned at `8c363ef`).
- `zetacheng/4-dark-energy-cosmology` —
  `90f210f5d8787037677778817d2bc5ab16c7aa6f` (`P4-SEA-ICE-01`,
  `P4-INTERFACE-DE-01`, `P4-EQ-WRINKLE-01`, `P4-WRINKLE-BRIDGE-01`,
  `P4-BOUND-DM-01`; Paper 5 boundary pinned at `b35acc0`).
- `zetacheng/1-dark-matter-structure` —
  `0673610640b8f60df429d4c5cfb45fc06bb4eb1c` (`P1-SEAICE-RAR-01`; unchanged by
  this review).

Cross-repo result inputs are pinned per "Cross-repo dependencies must be
pinned" above: Paper 3 vector input at `8c363ef`
(`zetacheng/3-vector-sector` `main`), Paper 5 `P5-OMEGA-01` FAILED verdict at
`b35acc0` (`zetacheng/5-topological-sector`, PR #4 merge; still on `main`).
