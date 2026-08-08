# Task specification — populate the cross-paper conventions registry in `0-programme`

**Repository: `zetacheng/0-programme`.** This task runs there, under
that repository's `AGENTS.md`, not Paper 2's.

Specification evidence base (`0-programme`):
`b399e115786422f5985ae61293be15c26d647171`

External evidence base (`zetacheng/2-emergent-gravity`), read-only:
`51d4bbe1a2e965b0793b18f4ead5a11dab54c364`

Classification: **MATERIAL**. Branch only; integration is a separate
authorization after result review.

**This is the programme's first import.** Seven rows of
`CROSS_PAPER_CONVENTIONS.md` change — six gain values from established
Paper-2 material, one changes status. **Everything else stays
`NOT YET IMPORTED`.**

---

## 0. The architecture this task establishes

**PI ruling, 2026-08-08 — conventions registry authority.**

> `0-programme/CROSS_PAPER_CONVENTIONS.md` is **authoritative for the
> CURRENT cross-paper convention value used by downstream work.**
>
> **Paper repositories retain their historical and frozen statements as
> evidence of what was used at that revision**, and hold the derivation
> or ruling that establishes the value. **New downstream work cites the
> programme registry.**
>
> **Any disagreement between a paper artifact and the registry is
> recorded and explicitly resolved. Historical artifacts are never
> silently rewritten**, and establishing this registry does not
> retroactively make an existing frozen statement an improper copy.
>
> **This is consistent with `AGENTS.md` programme rules 2 and 3** —
> which forbid the authoritative copy of a *derivation* in
> `0-programme` and require linking to the owning paper. **The
> authority being centralised is the VALUE, not the derivation.**
>
> **A convention conflict between the registry and a paper remains a
> recorded, explicitly resolved event**, never a silent override. Shared
> rule 2 stands: conventions are never silently changed.
>
> **Consequence for the file's closing sentence.** It currently reads
> *"This file does not override a paper's convention registry
> automatically."* Under this ruling the registry is authoritative for
> values, so that sentence is replaced — see A3. **The non-silence
> requirement it protected is preserved and strengthened.**

**Why this matters, concretely.** `γ₅` was recently found carrying two
different definitions inside Paper 2 — one in the Phase-A freeze, one in
a companion JSON — and the discrepancy survived because nothing held a
single authoritative value. **A registry that each paper cites removes
the mechanism by which that happened.** Duplicated copies drift;
citations do not.

## 1. What to populate, and from what

**Six populated rows, plus one status change (below).** For each
populated row: the value, and a citation to the Paper-2 artifact that
establishes it. **Do not reproduce any derivation** —
programme rule 2. A row is a value plus a pointer.

**Cite by repository, path, and commit**, e.g.
`zetacheng/2-emergent-gravity @ 51d4bbe1 : DECISION_LOG.md, entry
2026-08-08`. **A citation without a commit is not a citation** — Paper 2
moves, and a bare path will drift.

**Verify every value against the external evidence base before writing
it.** Quote what you find. **If a value differs from what this
specification states, the repository is right and this specification is
wrong: report the difference and STOP.**

    Metric signature
      (1, 1, 1, 1) Euclidean
      source: Paper-2 Phase-A freeze, conventions block

    Euclidean exponent mapping                     [NEW ROW]
      The canonical interaction expression X is written as it appears
      in the Boltzmann exponent: exp(-S_E) contains exp(+X), i.e.
      S_E = S_E,0 - X. For a channel coefficient c in X, the
      Hubbard-Stratonovich coefficient is g = +2c.
      source: Paper-2 DECISION_LOG.md, PI ruling 2026-08-08
      status: PI-supplied convention, not derived from frozen material

    **This is a NEW row, inserted immediately after `Wick rotation`.**

    **The existing `Wick rotation` row stays `NOT YET IMPORTED`, and
    that is deliberate.** The ruling fixes the Euclidean exponent /
    action-sign mapping. **It does not define a Minkowski-to-Euclidean
    rotation rule**, and Paper 2 established that no such rule is frozen
    anywhere — `CANONICAL_INTERACTION.md` carries a Minkowski-looking
    kinetic expression alongside Euclidean algebra with no stated
    rotation between them. **Filling `Wick rotation` with this value
    would record an unestablished convention as established**, which is
    the failure this registry exists to prevent.

    Gamma matrices and gamma5
      gamma5 = gamma(0)*gamma(1)*gamma(2)*gamma(3); Hermitian;
      gamma5^2 = Id4. Euclidean Hermitian basis
      S=Id4, P=gamma5, V=gamma(mu), A=I*gamma(mu)*gamma5,
      T=I*(gamma(mu)gamma(nu)-gamma(nu)gamma(mu))/2;
      trace(Id4) = 4.
      source: Paper-2 Phase-A freeze; PI ruling 2026-08-07 on the
      conflicting companion entry

    Flavor generator normalization
      trace(lam(A) lam(B)) = 2*delta(A,B); lam(0) = sqrt(2/N)*Id(N);
      A = 0 .. N^2-1, a U(N) index set including the singlet.
      source: Paper-2 Phase-A freeze, conventions block
      (un_generator_normalization). CANONICAL_INTERACTION.md section 2
      is recorded as provenance only: it still carries a DRAFT v0.5
      banner, and the establishing citation must be the strongest
      frozen artifact, not the draft that fed it.

    Interaction normalization
      X = (G/(2N)) * Sum( bilinear(lam(A),Id4)^2
                        + bilinear(lam(A),I*gamma5)^2, (A,0,N^2-1) )
      Only S and P are supported in the interaction; V, A and T are
      Fierz/HS representation families, not independent couplings.
      source: Paper-2 Phase-A freeze, canonical_interaction_expression

    Definitions of G, G_V, G_omega
      Paper 3 writes L_V = (G_omega/2) * J_mu J^mu with
      J_mu = psibar gamma_mu psi. The Fierz-induced vector singlet
      coefficient of (psibar gamma_mu psi)^2 is c_J = -G/(2N), hence
      G_omega = 2*c_J = -G/N. The apparent factor of two between
      -G/N and -G/(2N) is a normalization mapping, not a discrepancy:
      one names a coupling in the (G/2)J^2 convention, the other is
      the coefficient of J^2 itself.
      source: Paper-2 normalisation audit, derivations/
      P2-NORMALISATION-AUDIT_g_omega.md; Paper-3 note
      zetacheng/3-vector-sector @ 8c363ef0 :
      derivations/u3-fierz/u3_fierz.md

**And one row changes status rather than gaining a value:**

    Sign convention for attraction and repulsion
      NOT DEFINED
      No rule anywhere in the programme maps a channel coefficient's
      sign to a physical attraction or repulsion label. The Paper-2
      channel-character derivation searched for one and returned
      ATTRACTIVE/REPULSIVE NOT DEFINED BY THE FROZEN MATERIAL.
      source: Paper-2 derivations/P2-PHASE-01_channel_character.md
      note: this is NOT the same as NOT YET IMPORTED

**`NOT DEFINED` and `NOT YET IMPORTED` are different findings and the
registry must not blur them.** The first says nobody has decided; the
second says somebody may have decided and nobody has transferred it.
**Add a legend to the file stating that distinction.**

**Every remaining row keeps `NOT YET IMPORTED`.** Do not fill a row on
the strength of your own reading of a paper repository: a row is
populated only where this specification supplies it and the external
evidence base confirms it.

## 2. Acceptance criteria

**A0 — Commit order and paths, frozen.** `0-programme` has no `specs/`
or `reports/` convention. **This task therefore creates `specs/` and
`reports/`, at exactly these paths:**

    specs/2026-08-08T{HHMM}Z_cross-paper-conventions-import.md
    reports/2026-08-08T{HHMM}Z_cross-paper-conventions-import.md

`{HHMM}Z` is a UTC token fixed once by commit 1 and reused.

    commit 1  this specification
    commit 2  CROSS_PAPER_CONVENTIONS.md, GLOBAL_DECISION_LOG.md,
              SYNC_STATUS.md
    commit 3  this task's report

**A1 — External material verified.** For each of the seven changed rows,
quote the source text from the external evidence base at `51d4bbe1…`
(and, for the `G_ω` row, from `zetacheng/3-vector-sector @ 8c363ef0…`).
Read-only.

**A2 — Exactly SEVEN row-level changes**, and no others: six rows gain
populated values (`Metric signature`, `Euclidean exponent mapping` (new),
`Gamma matrices and gamma5`, `Flavor generator normalization`,
`Interaction normalization`, `Definitions of G, G_V, G_omega`); one row
changes status (`Sign convention for attraction and repulsion`, from
`NOT YET IMPORTED.` to `NOT DEFINED`). `Wick rotation`,
`Lattice/cutoff units`, `Field dimensions`, `Fourier transform`,
`Error convention`, and the naming row all keep `NOT YET IMPORTED.`.

**A3 — The closing sentence replaced.** Remove *"This file does not
override a paper's convention registry automatically"* and state the §0
ruling in its place.

**A4 — Legend added** distinguishing `NOT YET IMPORTED`, `NOT DEFINED`,
and a populated value.

**A5 — `GLOBAL_DECISION_LOG.md` entry**, append-only, zero deleted lines.

**A6 — `SYNC_STATUS.md`: Paper 2's `Conventions audited` cell only.**

**A7 — `MASTER_PROGRESS.md` untouched.**

**A8 — Nothing else touched.**

**A9 — Scope:** add the two timestamped `specs/` and `reports/` files;
modify `CROSS_PAPER_CONVENTIONS.md`, `GLOBAL_DECISION_LOG.md`,
`SYNC_STATUS.md`. Forbidden operations: delete, rename, copy,
type_change, unmerged, unknown.

**A10 — `make check` passes.**

**A11 — Branch only.** No merge, no PR, no force-push.

## 3. What this task does NOT do

- It does not import Paper 2.
- It does not define the attraction/repulsion sign convention; it records
  that nobody has.
- It does not resolve `0-programme`'s own role-model text (fixed-agent
  model). Report as a finding; do not fix here.
- It does not ratify `CANONICAL_INTERACTION.md` (DRAFT v0.5).

## 4. Invariants and prohibitions

- Executor-writable: the five paths of A9 only.
- No derivation or production scientific code in `0-programme`
  (programme rules 1, 2).
- No modification of any paper repository; no paper file copied into
  `0-programme`.
- Do not populate a row this specification does not supply.
- Do not change `MASTER_PROGRESS.md`; alter no `SYNC_STATUS.md` cell
  other than Paper 2's `Conventions audited`.
- Commit-message hygiene: no `Co-Authored-By`, no session identifier or
  URL, no tool attribution.
- No merge into `main`, no PR, no force-push, no history rewrite.
- Branch naming: follow `0-programme`'s convention; else use
  `governance/cross-paper-conventions-import` and say so.
- `0-programme`'s `AGENTS.md` governs this task.

## 5. Report contract

Raw output for A1–A11; source evidence for all seven changed rows; the
conventions table before and after; the replaced closing sentence
(old/new); the decision-log entry with zero-deletion diff; the
`SYNC_STATUS.md` one-cell diff; the role-model finding; whether writing
to a second repository raised difficulty; a Stops-and-clarifications
section with the five primary categories; anything ambiguous.
