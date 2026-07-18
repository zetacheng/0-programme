# PROG-SYNC-01 — P5-OMEGA-01 Cross-Repository Quotation Review

## Review question and method

Question: do Papers 1, 3 and 5 describe as open or live the continuum topological-stability gate that PF-006 records as failed?

Method: proof by direct quotation from the authoritative remote source at an exact commit. No paper repository was modified. A conflict is not forced: direct context may confirm, refute, or leave it unverified.

The scientific verdict used for comparison is the exact line from `zetacheng/kappa-c2a`, branch `topo-mass-radius` at `6a20b05e0899a878fde214c44cf77a8610d7516f`, `results/topo_verdict.txt`:

> MASS/RADIUS GATE FAILS: MINIMUM IS A CUTOFF-SCALE LATTICE LUMP.

PF-006 applies only to the tested one-loop continuum EFT combination of negative quartic coefficient plus endogenous nonlocal omega repulsion. It does not establish that the full cutoff-scale lattice theory has no baryonic object.

## Paper 5 — Topological Sector

Repository: `zetacheng/5-topological-sector`

Ref: `main`

Full commit SHA: `6de940c4dcbdf419cda4ef7578de2066f6d9a9c5`

File: `paper/paper5_internal_dimension_v0_23.tex`

Version: v0.23

Section: title-page status block (the abstract later repeats that the continuum-radius gate is open)

### Verbatim quotation

> Status: concept + test design + partial numerics; v0.20 records a
> MEASUREMENT-FORCED CORRECTION: the induced Skyrme coefficient is
> now known exactly and is NEGATIVE
> ($\kappa_U = -17/(1152\pi^2)$, chirally complete, closed form +
> Pauli--Villars confirmed), retracting this note's earlier
> positive-sign entries (S2-1, Gate 3) and re-scoping soliton
> stabilization to the endogenous flavor-singlet $\omega$ channel
> (existence and dynamization gates passed; continuum-radius gate
> open).

### Contextual interpretation

The quotation identifies the same continuum-radius gate and explicitly marks it open. PF-006 closes that tested continuum gate negatively. The paper's broader claim P5-CL-008 is currently too broad to mark failed without first narrowing it to the tested EFT route.

Conflict verdict: **CONFLICT CONFIRMED**.

### Minimal deferred edit

- Change the continuum-radius gate from open to failed.
- Include the exact verdict line.
- Preserve the cutoff-scale lattice-lump scope.
- Narrow P5-CL-008 to: “Within the tested one-loop EFT with negative $\kappa_U$ and the endogenous nonlocal omega kernel, a stable continuum $B=1$ topological soliton exists.”
- Mark only that narrowed claim `FAILED`.
- Do not state that the complete lattice theory has no baryons.

Affected claims: P5-CL-008; P5-CL-009 through P5-CL-013 require synchronization context but their upstream omega-health content is not refuted.

## Paper 3 — Vector Sector

Repository: `zetacheng/3-vector-sector`

Ref: `main`

Full commit SHA: `0cb95fe7052a675708999d44f66084e446a3d0bf`

File: `paper/paper3_vector_channel_v3_11.tex`

Version: v3.11

Section: “The model's own vector content: the $\omega$ route” → “What this does and does not establish”

### Verbatim quotation

> Third, this paper does not claim that the $\omega$ stabilizes any
> continuum object.  The repulsive kernel it supplies is an
> \emph{input} to a separate topological-stability gate, owned by
> the companion working note, whose kill criterion is the placement
> of the soliton radius inside the continuum window
> ($R_\star \gg a$ with $E''(R_\star) > 0$); the lattice $f$ and the
> screening mass $m_\omega$ that gate needs are external inputs not
> fixed by the one-loop computation reported here.

### Contextual interpretation

The ownership and non-claim boundary are correct, and the quotation does not claim stabilization. It nevertheless describes the downstream test prospectively as a separate gate with a kill criterion, rather than recording its now-closed negative verdict. The conflict is limited to tense and synchronization status.

Conflict verdict: **CONFLICT CONFIRMED — TENSE / STATUS SYNCHRONIZATION ONLY**.

### Minimal deferred edit

Change one sentence from an open future gate to a closed negative downstream gate, retain cross-paper ownership, and do not alter the omega derivation or accepted claims.

Affected claims: P3-C-006 requires a status/tense note. PF-006 does **not** undermine P3-C-001, P3-C-002, P3-C-004 or P3-C-005.

## Paper 1 — Dark Matter Structure

Repository: `zetacheng/1-dark-matter-structure`

Ref: `claude/paper1-gated-repo-governance-z478hp` (**unmerged**)

Full commit SHA: `8f5c63c1206b81a09df810c62ba92122d074ca38`

File: `paper/yukawa_sparc_paper_v163.tex`

Version: v16.3

Section: “Conclusions” → “Future directions”

### Verbatim quotation

> Since this list was drawn up, one route of a different
> type has acquired microscopic support in the companion programme: a
> nonlocal, topological dark-matter object whose size is set by the
> competition between the measured negative quartic coefficient
> (contraction) and an \emph{endogenous} isoscalar-vector repulsion
> (a Fierz-exact channel of the microscopic interaction, dynamized
> with healthy kinetic term, non-tachyonic mass, and
> topological-current coupling).  Its continuum-radius, mass,
> formation, and halo gates are open; it is registered here as the
> live microscopic direction, distinct from every route closed
> above.

### Contextual interpretation

This quotation explicitly identifies the failed route by both defining ingredients—negative quartic coefficient and endogenous omega repulsion—and calls its continuum-radius gate open and the route live. It therefore refers to the failed B=1 continuum soliton route, not merely to interface/wrinkle physics.

The legacy distinction was inspected directly in `zetacheng/kappa-c2a`, ref `de-interface-wrinkle` at `5ee543c9c7c37082c1053f438aa10a4a65ee7234`, file `derivation/de_interface_wrinkle.md`:

> dark matter = a NONUNIFORM collective deformation `q(x)=q_0+delta q(x)` (or interface
> height/thickness `h(x)`) of that interface — NOT a B=1 skyrmion (that is the
> now-reclassified UNIT-WINDING BARYONIC SOLITON GATE, verdict "cutoff-scale lattice
> lump", which does NOT test this hypothesis).

That direct distinction confirms the interface/wrinkle route is conceptually separate; it does not rescue Paper 1's quoted negative-quartic-plus-omega continuum route.

Conflict verdict: **CONFLICT CONFIRMED** on the unmerged governance branch.

### Minimal deferred edit

- Withdraw the negative-quartic-plus-endogenous-omega continuum soliton route as live.
- Distinguish it explicitly from the interface/wrinkle route.
- Do not merge the Paper 1 governance branch until synchronized.

Affected claims: no current Paper 1 claim-ledger ID directly owns this future-directions statement; cross-paper claim P5-CL-008 must be narrowed and synchronized. P1-CL-010 remains `RETIRED` and is unrelated to this conflict.

## Review disposition

| Paper | Disposition | Paper edit applied? |
|---|---|---|
| Paper 1 | CONFLICT CONFIRMED on unmerged branch | No |
| Paper 3 | CONFLICT CONFIRMED — tense/status synchronization only | No |
| Paper 5 | CONFLICT CONFIRMED | No |

PROG-SYNC-01 remains `OPEN` pending PI decision. No paper repository was changed.
