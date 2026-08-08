# Report — cross-paper conventions registry, first import

Task: populate `0-programme/CROSS_PAPER_CONVENTIONS.md` (first import).
Classification: **MATERIAL**. Branch only; no merge, no PR.
Authority: `specs/2026-08-08T1904Z_cross-paper-conventions-import.md`.

- Specification evidence base (`0-programme`): `b399e115786422f5985ae61293be15c26d647171`.
- External evidence base (`zetacheng/2-emergent-gravity`, read-only): `51d4bbe1a2e965b0793b18f4ead5a11dab54c364`.
- Co-source (`zetacheng/3-vector-sector`, read-only): `8c363ef08368f5c022278ea5f36e01496be3d5ca`.
- Branch: `governance/cross-paper-conventions-import` (chosen per the spec's fallback; see A11).

## A0 — commit order and paths

UTC token fixed by commit 1: **1904** (`2026-08-08T1904Z`). Paths created:

- `specs/2026-08-08T1904Z_cross-paper-conventions-import.md` (commit 1)
- `reports/2026-08-08T1904Z_cross-paper-conventions-import.md` (commit 3, this file)

`0-programme` had no `specs/` or `reports/` directory at the base; both are created by this task. Commit order: (1) specification; (2) `CROSS_PAPER_CONVENTIONS.md` + `GLOBAL_DECISION_LOG.md` + `SYNC_STATUS.md`; (3) this report.

## A1 — external material verified (source evidence for all SEVEN changed rows)

All quotations are from the pinned read-only bases. No paper repository was modified; no paper file was copied into `0-programme`. `zetacheng/2-emergent-gravity @ 51d4bbe1` was fetched and checked out detached; `zetacheng/3-vector-sector @ 8c363ef0` cloned read-only to a workspace path outside this repository.

1. **Metric signature** — `zetacheng/2-emergent-gravity @ 51d4bbe1 : derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` (§C conventions JSON). Quote: `"conventions":{"metric_signature":["1","1","1","1"], …}`. → `(1,1,1,1)` Euclidean. **Matches spec.**

2. **Euclidean exponent mapping** (NEW) — `zetacheng/2-emergent-gravity @ 51d4bbe1 : DECISION_LOG.md`, entry `2026-08-08 — Euclidean exponent mapping`. Quote (PI ruling, verbatim): *"exp(-S_E) contains exp(+X)  <=>  S_E = S_E,0 - X … for a channel whose coefficient in `X` is written `c * J**2`, the Hubbard–Stratonovich coefficient is `g = +2c` … This is **NOT derived from the frozen material**."* **Matches spec** (incl. the "not derived from frozen material" status).

3. **Gamma matrices and gamma5** — `zetacheng/2-emergent-gravity @ 51d4bbe1 : derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` (§C). Quote: `"gamma5_definition":"gamma(0)*gamma(1)*gamma(2)*gamma(3)"`, `"dirac_trace_normalization":"trace(Id4)=4"`, basis `S=Id4, P=gamma5, V=gamma(mu), A=I*gamma(mu)*gamma5, T=I*(gamma(mu)*gamma(nu)-gamma(nu)*gamma(mu))/2`. Corroborated by `CONVENTIONS.md:27` (*"`γ_5 = γ_1γ_2γ_3γ_4`, Hermitian, `γ_5² = 𝟙`"*). The **PI ruling 2026-08-07 on the conflicting companion entry** (that the Phase-A freeze governs over the `CANONICAL_INTERACTION.json` companion, whose `gamma5 = I*gamma(0)…gamma(3)`, `gamma5^2 = -Id4`) is reproduced in `specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md` §8 and documented at `reports/2026-08-07T0356Z_…md` §8.1. **Matches spec.**

4. **Flavor generator normalization** — `zetacheng/2-emergent-gravity @ 51d4bbe1 : derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` (§A, §C). Quote: *"Internal generators `λ^A`, `A = 0 … N²−1`, normalized `Tr[λ^A λ^B] = 2δ^{AB}`, with the singlet `λ⁰ = √(2/N)·1_N`"*; JSON `"un_generator_normalization":"trace(lam(A)*lam(B))=2*KroneckerDelta(A,B)"`. **Matches spec.** `CANONICAL_INTERACTION.md` §2 carries a `DRAFT v0.5` banner and is cited as provenance only.

5. **Interaction normalization** — `zetacheng/2-emergent-gravity @ 51d4bbe1 : derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` (§D machine block). Quote: `"canonical_interaction":{"expression":"(G/(2*N))*Sum(bilinear(lam(A),Id4)**2+bilinear(lam(A),I*gamma5)**2,(A,0,N**2-1))"}`; §B/§D: *"The source interaction has support only on the generator-sum `S` and `P` terms; the other families are required Fierz/HS representations."* **Matches spec.**

6. **Definitions of G, G_V, G_omega** — `zetacheng/2-emergent-gravity @ 51d4bbe1 : derivations/P2-NORMALISATION-AUDIT_g_omega.md` (Verdict `NORMALISATION MAPPING`: `c_J = -G/(2N)`, `G_omega = 2*c_J = -G/N`); and `zetacheng/3-vector-sector @ 8c363ef0 : derivations/u3-fierz/u3_fierz.md`. Paper-3 quote, line 10: *"Classification (Paper 3 convention `L_V = (G_V/2) J_mu J^mu`, `J_mu = psibar gamma_mu psi`)"*; lines 188–190: *"`L_int -> (G/2N) * (-3/2) * (2/3) J_mu J^mu = -(G/2N) J_mu J^mu = (G_omega/2) J_mu J^mu   with   G_omega = -G/N.`"* `u3_fierz.md` sha256 `6784d51a5a8d5f8b70b55213e4bf9b3eb50fc8c331397e80a239d16285d58f49` matches the Paper-2 audit's pin. **Value matches spec.** *Phrasing nuance (not a value difference):* Paper 3 writes the convention with the generic symbol `G_V` (`L_V = (G_V/2) J^2`) and identifies `G_omega = -G/N` as the omega-channel value; the spec/registry writes `L_V = (G_omega/2) J^2`, which is that convention specialised to the omega channel (`G_V = G_omega`). The coefficient `c_J = -G/(2N)` and the mapping `G_omega = 2 c_J = -G/N` are identical, so this is not a "value differs → STOP" event; it is recorded here for transparency.

7. **Sign convention for attraction and repulsion → NOT DEFINED** — `zetacheng/2-emergent-gravity @ 51d4bbe1 : derivations/P2-PHASE-01_channel_character.md`. Quote (Layer 2 verdict): *"**Layer 2 is withheld: `ATTRACTIVE/REPULSIVE NOT DEFINED BY THE FROZEN MATERIAL`.**"* **Matches spec.** This is a `NOT DEFINED` finding, distinct from `NOT YET IMPORTED`.

**No value differed from the specification; no STOP was triggered.** No `UNAVAILABLE EVIDENCE` arose — every pinned revision was reachable.

## A2 — exactly seven row-level changes

Six rows gain populated values (`Metric signature`, `Euclidean exponent mapping` (new), `Gamma matrices and gamma5`, `Flavor generator normalization`, `Interaction normalization`, `Definitions of G, G_V, G_omega`); one row changes status (`Sign convention for attraction and repulsion` → `NOT DEFINED`). The table gained one line (12 → 13 data rows). Untouched, still `NOT YET IMPORTED.`: `Wick rotation`, `Lattice/cutoff units`, `Field dimensions`, `Fourier transform`, `Error convention`, and the naming row (6 rows).

### Conventions table — BEFORE (base `b399e11`)

| Convention | Programme value |
|---|---|
| Metric signature | NOT YET IMPORTED. |
| Wick rotation | NOT YET IMPORTED. |
| Gamma matrices and gamma5 | NOT YET IMPORTED. |
| Flavor generator normalization | NOT YET IMPORTED. |
| Lattice/cutoff units | NOT YET IMPORTED. |
| Interaction normalization | NOT YET IMPORTED. |
| Definitions of \(G\), \(G_V\), \(G_\omega\) | NOT YET IMPORTED. |
| Sign convention for attraction and repulsion | NOT YET IMPORTED. |
| Field dimensions | NOT YET IMPORTED. |
| Fourier transform | NOT YET IMPORTED. |
| Error convention | NOT YET IMPORTED. |
| Naming of Sea, interface, lattice phase, wrinkle and topological object | NOT YET IMPORTED. |

### Conventions table — AFTER (row values summarised; full cell text incl. citations is in `CROSS_PAPER_CONVENTIONS.md`)

| Convention | Programme value (summary) |
|---|---|
| Metric signature | `(1,1,1,1)` Euclidean. + citation |
| Wick rotation | NOT YET IMPORTED. |
| Euclidean exponent mapping *(new)* | `exp(-S_E)` contains `exp(+X)`; `S_E = S_E,0 - X`; `g = +2c`. status: PI-supplied, not derived. + citation |
| Gamma matrices and gamma5 | `gamma5 = gamma(0)*gamma(1)*gamma(2)*gamma(3)`; Hermitian; `gamma5^2 = Id4`; `S,P,V,A,T` basis; `trace(Id4)=4`. + citation |
| Flavor generator normalization | `trace(lam(A) lam(B)) = 2*delta(A,B)`; `lam(0)=sqrt(2/N)*Id(N)`; `A=0..N^2-1`. + citation |
| Lattice/cutoff units | NOT YET IMPORTED. |
| Interaction normalization | `X = (G/(2N)) * Sum(bilinear(lam(A),Id4)^2 + bilinear(lam(A),I*gamma5)^2,(A,0,N^2-1))`; only S,P supported. + citation |
| Definitions of \(G\), \(G_V\), \(G_\omega\) | `G_omega = 2*c_J = -G/N`, `c_J = -G/(2N)`; factor 2 is a normalization mapping. + citation |
| Sign convention for attraction and repulsion | **NOT DEFINED.** + citation |
| Field dimensions | NOT YET IMPORTED. |
| Fourier transform | NOT YET IMPORTED. |
| Error convention | NOT YET IMPORTED. |
| Naming of Sea, interface, lattice phase, wrinkle and topological object | NOT YET IMPORTED. |

## A3 — closing sentence replaced

- **OLD:** *"This file does not override a paper's convention registry automatically. A convention conflict must be recorded and resolved explicitly."*
- **NEW:** *"This registry is **authoritative for the current cross-paper convention value used by downstream work** (PI ruling, 2026-08-08; recorded in `GLOBAL_DECISION_LOG.md`). Paper repositories retain their historical and frozen statements as evidence of what was used at each revision, and hold the derivation or ruling that establishes each value; new downstream work cites this registry. The authority centralised here is the **value, not the derivation** (consistent with `AGENTS.md` programme rules 2 and 3). Any disagreement between a paper artifact and this registry is **recorded and explicitly resolved, never silently overridden**; establishing this registry does not retroactively make an existing frozen statement an improper copy, and historical artifacts are never silently rewritten."*

The non-silence requirement the old sentence protected is preserved and strengthened.

## A4 — legend added

A legend distinguishing **a populated value**, **`NOT DEFINED`** (nobody has decided), and **`NOT YET IMPORTED.`** (may be decided, not yet transferred) was added above the closing paragraph.

## A5 — GLOBAL_DECISION_LOG.md entry (append-only, zero deletions)

`git diff --numstat GLOBAL_DECISION_LOG.md` → **`32  0  GLOBAL_DECISION_LOG.md`** (32 insertions, 0 deletions). The new entry `## 2026-08-08 — Cross-paper conventions registry: authority ruling and first import` follows the file's `Decision / Reason / Evidence / Affected papers / Required synchronization / Supersedes / Related gates and repositories` template and is inserted between the 2026-07-15 entry and the `## Entry template` block.

## A6 — SYNC_STATUS.md, one cell

Paper 2's `Conventions audited` cell only, `NOT IMPORTED` → `7 rows @ 51d4bbe1 (6 imported, 1 NOT DEFINED)`. `Last sync` and every other cell/row unchanged.

```
-| Paper 2 | `zetacheng/2-emergent-gravity` | NOT IMPORTED | NOT IMPORTED | NOT IMPORTED | NOT IMPORTED | NOT IMPORTED | NOT IMPORTED |
+| Paper 2 | `zetacheng/2-emergent-gravity` | NOT IMPORTED | NOT IMPORTED | NOT IMPORTED | NOT IMPORTED | 7 rows @ 51d4bbe1 (6 imported, 1 NOT DEFINED) | NOT IMPORTED |
```

## A7 — MASTER_PROGRESS.md untouched

`git diff --quiet MASTER_PROGRESS.md` → UNCHANGED. `INFRASTRUCTURE INITIALIZED` and all `NOT IMPORTED` rows stand. Six convention rows do not make a paper imported.

## A8 — nothing else touched

`git diff --stat` of base→head excluding the five scope paths is empty; every other path is blob-identical to base `b399e11`.

## A9 — scope manifest

`0-programme` provides no dedicated scope checker (its only test target is `tests/test_repository_structure.py`), so the base-to-head `--name-status` diff is supplied as the manifest:

```
M	CROSS_PAPER_CONVENTIONS.md
M	GLOBAL_DECISION_LOG.md
M	SYNC_STATUS.md
A	reports/2026-08-08T1904Z_cross-paper-conventions-import.md
A	specs/2026-08-08T1904Z_cross-paper-conventions-import.md
```

Manifest SHA-256: `70ce6cd75f4583e7bec025f54b89a1b9f1f164d27955e969fd6b04b0c37ad05d`. Final base-to-head scope: **2 additions, 3 modifications.** No forbidden operation (delete/rename/copy/type_change/unmerged/unknown) occurred.

## A10 — make check

`make check` runs `ruff check .`, `pytest`, and `pytest tests/test_repository_structure.py`. Output: `All checks passed!` (ruff); `3 passed` (pytest); `3 passed` (structure). Green. No pre-existing failure; no installation beyond the dev deps `make check` itself requires.

## A11 — branch only

`refs/remotes/origin/main` and remote `refs/heads/main` both at `b399e115786422f5985ae61293be15c26d647171` — unchanged, not moved by this task. The task branch `governance/cross-paper-conventions-import` was created from that pinned base and is the only ref pushed. No branch deleted. (Final pushed head SHA and full `git ls-remote` are in the executor's final response, per the self-reference rule for the report commit.)

## Commit hygiene (per commit)

Every commit was inspected before and after writing. In all three, the executor's default `Co-Authored-By:` and `Claude-Session:` trailers were **suppressed** to satisfy the spec's hygiene rule (no `Co-Authored-By`, no session identifier or URL, no tool attribution). Stored messages carry no trailer:

- commit 1 — `docs: record the cross-paper conventions import specification` (suppressed: `Co-Authored-By`, `Claude-Session`).
- commit 2 — `docs: cross-paper conventions first import (six values, one NOT DEFINED) with registry-authority ruling` (suppressed: `Co-Authored-By`, `Claude-Session`).
- commit 3 — this report (suppressed: `Co-Authored-By`, `Claude-Session`).

## Role-model finding (§3)

`0-programme/AGENTS.md` still describes a **fixed-agent** role model — *ChatGPT: conceptual discussion / ontology / interpretation; Codex: programme-repository maintenance and paper-repo implementation; Claude: independent review and gate verdicts; Principal Investigator: authorization*. This is the model Paper 2 replaced with a **function-based** one (Generator / Discriminator / Executor as hats, not identities) on 2026-08-06 (see Paper 2's `specs/2026-08-06T*_role-model-*`). It is **reported as a finding and left unfixed**, per §3 — out of scope for this conventions import.

## Writing across repositories

This task **wrote to a single repository** (`0-programme`) only; it performed **no write to any second repository** (forbidden by the invariants). Cross-repository interaction was **read-only**: `zetacheng/2-emergent-gravity @ 51d4bbe1` (fetched by SHA, checked out detached) and `zetacheng/3-vector-sector @ 8c363ef0` (shallow read-only clone to a workspace path outside `0-programme`). Both reads were straightforward; sha256 of the Paper-3 note matched the Paper-2 audit's pin, giving an independent cross-check. No paper file was copied into `0-programme`; quotations are quotations. No difficulty arose. The programme's "written across repositories never" property is preserved: nothing was written outside `0-programme`.

## Stops and clarifications

No hard STOP occurred. One primary category per stop; none were triggered.

- **SPECIFICATION_DEFECT** — none. (Secondary, non-blocking: the `G_omega` row's phrasing `L_V = (G_omega/2) J^2` vs Paper 3's generic `L_V = (G_V/2) J^2`; the value is identical, so this is the omega-channel specialisation, not a defect. Recorded under A1(6).)
- **ENVIRONMENT** — none. No installation beyond `make check`'s existing dev deps.
- **OBSERVATION_METHOD_ERROR** — none.
- **REPOSITORY_DEFECT** — none in `0-programme`. (Secondary, pre-existing in Paper 2 and already adjudicated there: the `gamma5` freeze-vs-JSON-companion disagreement, resolved by the 2026-08-07 PI ruling that the freeze governs; unchanged here.)
- **UNRESOLVED_GOVERNANCE_OR_EVIDENCE_AMBIGUITY** — none blocking. (Secondary observation: `0-programme`'s fixed-agent role model diverges from Paper 2's function-based model — reported above, not resolved here per §3.)

## Anything ambiguous / would have specified differently

- **Citation commit length.** The spec's example uses 8-hex short SHAs (`51d4bbe1`, `8c363ef0`); the registry cells follow that for readability, while this report and the decision-log entry additionally record the full 40-hex SHAs. A future amendment may prefer full SHAs everywhere to remove any residual ambiguity.
- **Registry cell length.** Multi-line values are rendered with `<br>` inside two-column table cells. This is faithful but dense; a future revision might split value and citation into separate columns, or move long values to per-row subsections, without changing the authoritative content.
- Otherwise the specification was internally consistent and consistent with `0-programme`'s `AGENTS.md`; no instruction had to be adjudicated.
