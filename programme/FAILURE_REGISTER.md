# Programme Failure Register

| Failure ID | Route | Owning paper | Failed gate | Reason | Consequence | Can it be reopened? | Evidence |
|---|---|---|---|---|---|---|---|
| PF-001 | Positive induced Skyrme coefficient stabilising a soliton | Paper 5 | `paper-owned:5-topological-sector#P5-C2A-03`; `paper-owned:5-topological-sector#P5-C2A-04` | The reported `kappa_Skyrme > 0` result from July 8 was a fit-leakage artifact. The chirally complete closed form is negative: `kappa_U = -17/(1152 pi^2)`. | Withdraws the one-loop positive Skyrme stabiliser and the positive Berry-Maxwell route associated with gate S2-1. | No — closed in exact form | `zetacheng/5-topological-sector`, P5-CL-003 `VERIFIED`; independently reproduced by reviewer in `reviews/claude/2026-07-16-c2a.md`. |
| PF-002 | Cross-channel couplings are not Fierz-inherited; single-coupling economy postulate | Papers 2 and 5 | `paper-owned:3-vector-sector#P3-FIERZ-01` | A `gamma5`-without-the-`i` convention error was used. The chirally invariant pair Fierzes to `\|c_V\| = \|c_A\| = 1/2`, not zero. | The zero-coupling claim and the single-coupling economy justification are withdrawn. Cross-channel ratios are Fierz-inherited, with flavor-singlet `G_omega = -G/N`; Paper 2 v2.15 and Paper 5 v0.23 record the retraction. | No — exact Fierz identity and convention correction | `zetacheng/3-vector-sector`, P3-C-001 `VERIFIED`; Paper 2 v2.15 Fierz retraction; Paper 5 P5-CL-014 `FAILED` and v0.23 retraction. |
| PF-003 | Dimensional-transmutation / monopole generator for dark energy | Paper 4 | `paper-owned:4-dark-energy-cosmology#P4-MONOPOLE-01` | The pre-registered window required `S_mono` in `[140,550]`, based on `kappa_U = +0.144`. The verified input instead gives `S_mono = 640 kappa_U = -85/(9 pi^2) = -0.95`, about 150 times too small and of opposite sign. | The chain terminates; Paper 4 v5.6–v5.8 viability-gate claims were retracted in v6.0. | No — sign-robust | Paper 4 v6.3, section “The pre-registered verdict”; upstream input is Paper 5 P5-CL-003. Current migration record: `zetacheng/4-dark-energy-cosmology`, unmerged `sync/legacy-de-migration` at `ea3c7ffc56a9ad3f087945cea817d08398ecbe24`. |
| PF-004 | Yukawa halo kernel with a physical finite screening-radius population | Paper 1 | `paper-owned:1-dark-matter-structure#P1-MLPRIOR-01` | The finite-`r_c` population collapses from 58% to 7% under a lognormal 0.1-dex `Upsilon_*` prior and to 2% with `mu = 1` fixed. Survivors are gas-dominated dwarfs. | Free-`mu` results are diagnostics of mimicry capacity, not evidence for a physical screening-radius population. | No | `zetacheng/yukawa-sparc-fits`: `ml_prior_lognormal.py`, `ml_prior_mufixed.py`; independently reproduced by reviewer. Owning-repository record: Paper 1 P1-CL-009 `FAILED` on unmerged governance branch `8f5c63c1206b81a09df810c62ba92122d074ca38`. |
| PF-005 | Attractive four-fermion vector route to a composite repulsive vector | Paper 3 | `paper-owned:3-vector-sector#P3-VEC-O2` | Subcritical RPA gives `V_eff(q) > 0` for all tested `q`; resummation enhances attraction and never flips its sign. No below-threshold bound state appears at natural coupling. | The repulsive Fierz-inherited channel `G_omega = -G/N` is the surviving vector content. | No | `zetacheng/3-vector-sector`: claim P3-C-003 is `FAILED`; computational gate P3-VEC-O2 is `PASS` and independently accepted. Paper v3.9 pole audit retained in the Paper 3 history. |
| PF-006 | Omega-stabilised continuum topological object in the tested one-loop EFT | Paper 5 | `paper-owned:5-topological-sector#P5-OMEGA-01` | The negative one-loop quartic plus the endogenous nonlocal omega repulsion does not produce an interior continuum minimum; the energy runs toward the cutoff regime. See the extended record below. | No `g0` opens a continuum window and no `g0_crit` exists in the tested EFT. The evidence supports a cutoff-scale lattice lump, not the absence of a microscopic baryonic object. | Not at this order | `zetacheng/kappa-c2a`, branch `topo-mass-radius` at `6a20b05e0899a878fde214c44cf77a8610d7516f`, `results/topo_verdict.txt`; supplied independent reviewer verification dated 2026-07-16. |

Failures must never be deleted merely because the programme changes direction. A later reopening must preserve the original entry and provenance and create a new reopening record.

## PF-006 — Extended record

### Verbatim verdict

The authoritative legacy file `zetacheng/kappa-c2a`, branch `topo-mass-radius` at `6a20b05e0899a878fde214c44cf77a8610d7516f`, `results/topo_verdict.txt`, states:

> MASS/RADIUS GATE FAILS: MINIMUM IS A CUTOFF-SCALE LATTICE LUMP.

### Independent review evidence — 2026-07-16

The supplied independent-review record states that the reviewer ran the branch's own:

```text
python -m scripts.topological_mass_radius
```

or the exact repository-supported equivalent in a clean Linux environment. The reproduced result was stronger than the finite scan alone suggested.

#### Monotonic collapse

At

\[
m=0.30,\qquad g_0=20,
\]

the total energy decreases as \(R\) approaches zero:

\[
E_{\rm tot}(R=4)=+2.544,
\]

while

\[
E_{\rm tot}(R=0.02)=-2.109.
\]

The branch reports:

```text
interior = False
collapse = True
```

#### Saturation in radius

The omega contribution saturates as \(R\to0\):

\[
E_\omega(R=1)=0.0642,
\]

\[
E_\omega(R=0.01)=0.0913.
\]

The mechanism is that the momentum integral is restricted to

\[
q<\Lambda,
\]

because the composite omega description is valid only within the EFT band.

A local \(1/R^3\) contact repulsion would require the momentum integral to run to arbitrarily high momentum, which this EFT does not permit.

#### Saturation in coupling

The omega contribution also saturates as \(g_0\to\infty\).

At

\[
R=0.02,
\]

the reproduced values are:

\[
g_0=1\quad\Rightarrow\quad E_\omega=0.008,
\]

\[
g_0=20\quad\Rightarrow\quad E_\omega=0.091,
\]

\[
g_0=400\quad\Rightarrow\quad E_\omega=0.220,
\]

\[
g_0=10^4\quad\Rightarrow\quad E_\omega=0.260,
\]

\[
g_0=10^6\quad\Rightarrow\quad E_\omega=0.268.
\]

Meanwhile:

\[
E_4(R=0.02)=-2.21.
\]

Increasing the coupling by six orders of magnitude cannot compensate for the negative quartic term.

The structural reason is:

\[
D_{00}\propto\frac{g_0}{1+g_0\Pi_V}
\longrightarrow
\frac{1}{\Pi_V}
\qquad
(g_0\to\infty).
\]

The RPA denominator screens the coupling.

Therefore the conclusion

```text
no g0 opens a continuum window; no g0_crit exists
```

is not merely an empirical result of a finite parameter scan.

Within this EFT it follows structurally from

\[
\kappa_U<0,
\]

\[
E_4(R)\sim-\frac{|B|}{R},
\]

the bounded omega contribution

\[
D_{00}\leq\frac{1}{\Pi_V},
\]

and

\[
E_2(R)\to0
\qquad
(R\to0).
\]

No numerical minimizer or solver choice determines the verdict.

#### Regulator direction

The EFT regulator clips

\[
\Pi_V\geq0.
\]

This is the regulator choice favourable to repulsion.

The collapse is therefore not manufactured by an artificially attractive regulator.

### Precise scope of PF-006

This gate establishes that within the tested one-loop EFT band there is no stable continuum \(B=1\) soliton produced by the combination of the negative quartic coefficient and the endogenous nonlocal omega kernel. The energy runs toward the cutoff regime \(R\sim1/\Lambda\), where the EFT ceases to be reliable. The correct conclusion is the verdict's own: a cutoff-scale lattice lump. The gate does not establish that the full cutoff-scale lattice theory contains no baryonic object. That is a separate lattice question.

This record does not state that the complete microscopic theory has no baryons, and it does not state that every possible topological stabilization mechanism is dead.

The failed route is specifically:

\[
\text{negative one-loop quartic}
+
\text{endogenous nonlocal omega repulsion}
\]

within the tested continuum EFT band.

### Cross-repository synchronization consequence

Open synchronization item for `zetacheng/5-topological-sector`:

- The current broad wording of P5-CL-008 must not simply be marked failed without narrowing its scope.
- A later Paper 5 synchronization edit should restate the claim as: “Within the tested one-loop EFT with negative \(\kappa_U\) and the endogenous nonlocal omega kernel, a stable continuum \(B=1\) topological soliton exists.”
- That narrowed claim becomes `FAILED`.
- The broader proposition “The complete cutoff-scale lattice theory contains no baryonic object” has not been tested and must not be marked failed.
- `topo-mass-radius` remains unmigrated and is the authoritative evidence for `paper-owned:5-topological-sector#P5-OMEGA-01`.
- The Paper 5 repository must eventually import or reference that evidence.
- No Paper 5 edit is made in this sweep.
