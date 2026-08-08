# Cross-Paper Conventions

| Convention | Programme value |
|---|---|
| Metric signature | `(1, 1, 1, 1)` Euclidean.<br>source: Paper-2 Phase-A freeze, conventions block — `zetacheng/2-emergent-gravity @ 51d4bbe1 : derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` (§C, `metric_signature`). |
| Wick rotation | NOT YET IMPORTED. |
| Euclidean exponent mapping | The canonical interaction expression `X` is written as it appears in the Boltzmann exponent: `exp(-S_E)` contains `exp(+X)`, i.e. `S_E = S_E,0 - X`. For a channel coefficient `c` in `X`, the Hubbard-Stratonovich coefficient is `g = +2c`.<br>status: PI-supplied convention, not derived from frozen material.<br>source: `zetacheng/2-emergent-gravity @ 51d4bbe1 : DECISION_LOG.md, entry 2026-08-08` (PI ruling, Euclidean exponent mapping). |
| Gamma matrices and gamma5 | `gamma5 = gamma(0)*gamma(1)*gamma(2)*gamma(3)`; Hermitian; `gamma5^2 = Id4`. Euclidean Hermitian basis `S=Id4`, `P=gamma5`, `V=gamma(mu)`, `A=I*gamma(mu)*gamma5`, `T=I*(gamma(mu)gamma(nu)-gamma(nu)gamma(mu))/2`; `trace(Id4) = 4`.<br>source: Paper-2 Phase-A freeze — `zetacheng/2-emergent-gravity @ 51d4bbe1 : derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` (§C); PI ruling 2026-08-07 on the conflicting companion entry, reproduced in `specs/2026-08-07T0356Z_p2-phase-01-fierz-and-branch-depths.md` §8 (the Phase-A freeze governs over the `CANONICAL_INTERACTION.json` companion). |
| Flavor generator normalization | `trace(lam(A) lam(B)) = 2*delta(A,B)`; `lam(0) = sqrt(2/N)*Id(N)`; `A = 0 .. N^2-1`, a U(N) index set including the singlet.<br>source: Paper-2 Phase-A freeze, conventions block (`un_generator_normalization`) — `zetacheng/2-emergent-gravity @ 51d4bbe1 : derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md`. `CANONICAL_INTERACTION.md` §2 is provenance only (it still carries a DRAFT v0.5 banner); the establishing citation is the frozen freeze artifact, not the draft that fed it. |
| Lattice/cutoff units | NOT YET IMPORTED. |
| Interaction normalization | `X = (G/(2N)) * Sum( bilinear(lam(A),Id4)^2 + bilinear(lam(A),I*gamma5)^2, (A,0,N^2-1) )`. Only S and P are supported in the interaction; V, A and T are Fierz/HS representation families, not independent couplings.<br>source: Paper-2 Phase-A freeze, `canonical_interaction_expression` — `zetacheng/2-emergent-gravity @ 51d4bbe1 : derivations/P2-CHANNEL-FREEZE-01_phaseA_freeze.md` (§D). |
| Definitions of \(G\), \(G_V\), \(G_\omega\) | Paper 3 writes `L_V = (G_omega/2) * J_mu J^mu` with `J_mu = psibar gamma_mu psi`. The Fierz-induced vector singlet coefficient of `(psibar gamma_mu psi)^2` is `c_J = -G/(2N)`, hence `G_omega = 2*c_J = -G/N`. The apparent factor of two between `-G/N` and `-G/(2N)` is a normalization mapping, not a discrepancy: one names a coupling in the `(G/2)J^2` convention, the other is the coefficient of `J^2` itself.<br>source: Paper-2 normalisation audit — `zetacheng/2-emergent-gravity @ 51d4bbe1 : derivations/P2-NORMALISATION-AUDIT_g_omega.md`; Paper-3 note `zetacheng/3-vector-sector @ 8c363ef0 : derivations/u3-fierz/u3_fierz.md` (convention at lines 10-11; assembly at lines 185-190). |
| Sign convention for attraction and repulsion | **NOT DEFINED.** No rule anywhere in the programme maps a channel coefficient's sign to a physical attraction or repulsion label. The Paper-2 channel-character derivation searched for one and returned `ATTRACTIVE/REPULSIVE NOT DEFINED BY THE FROZEN MATERIAL`.<br>note: this is **not** the same as `NOT YET IMPORTED` (see legend).<br>source: `zetacheng/2-emergent-gravity @ 51d4bbe1 : derivations/P2-PHASE-01_channel_character.md` (Layer 2 verdict). |
| Field dimensions | NOT YET IMPORTED. |
| Fourier transform | NOT YET IMPORTED. |
| Error convention | NOT YET IMPORTED. |
| Naming of Sea, interface, lattice phase, wrinkle and topological object | NOT YET IMPORTED. |

## Legend

- **A populated value** — the current programme value, with a citation (repository, path, commit) to the paper artifact that establishes it. Downstream work cites this registry for the value.
- **`NOT DEFINED`** — the programme has searched and found that no rule establishes this convention anywhere; nobody has decided it. This is a finding, not a gap awaiting transfer.
- **`NOT YET IMPORTED.`** — a value may exist in a paper repository but has not yet been verified and transferred into this registry. Somebody may have decided; nobody has imported it.

`NOT DEFINED` and `NOT YET IMPORTED.` are distinct findings and must not be blurred.

This registry is **authoritative for the current cross-paper convention value used by downstream work** (PI ruling, 2026-08-08; recorded in `GLOBAL_DECISION_LOG.md`). Paper repositories retain their historical and frozen statements as evidence of what was used at each revision, and hold the derivation or ruling that establishes each value; new downstream work cites this registry. The authority centralised here is the **value, not the derivation** (consistent with `AGENTS.md` programme rules 2 and 3). Any disagreement between a paper artifact and this registry is **recorded and explicitly resolved, never silently overridden**; establishing this registry does not retroactively make an existing frozen statement an improper copy, and historical artifacts are never silently rewritten.
