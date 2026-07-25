# PM-0007 — Candidate Dynamic Quaternionic Network Model

Status: BRAINSTORMING CANDIDATE — NON-CANONICAL

Evidence class: HYPOTHESIS

Version: draft 2026-07-25

Owner: Principal Investigator (`0-programme` records the hypothesis only)

> This document records research hypotheses and PI physical intuition only. It is not part of the current Paper 2 derivation, does not define the canonical interaction, and must not be cited as an established result unless independently derived and promoted through the programme governance process.

## Part 0 — Purpose, scope, and research hierarchy

The current Paper 2 programme begins from a provisional effective four-fermion interaction. This note preserves a candidate deeper microscopic origin proposed in PI discussion:

```text
dynamic stochastic network
    → spinorial/quaternionic link dynamics
    → integrate out link fluctuations
    → effective four-fermion interaction
    → Hubbard–Stratonovich sectors
    → collective fields
    → possible emergent gravity, gauge, and scalar phenomena
```

Only the first part of this chain—the network, its link variables, and the possible production of an effective interaction—is being brainstormed here. No later collective or gravitational result follows from recording the idea.

The two research routes are distinct:

### Current effective-theory route

```text
provisional effective interaction
    → Fierz / channel algebra
    → Hubbard–Stratonovich decomposition
    → SI-1
    → SI-2
```

### Candidate microscopic route

```text
dynamic random network
    → bond/link degrees of freedom
    → effective four-fermion interaction
    → current effective-theory route
```

The candidate microscopic model does not supersede the current effective-theory route. It would have to derive its own effective interaction and then enter the existing algebraic and governance chain without inheriting the status of that chain.

## Part I — PI physical intuition

The motivating PI intuition is that the underlying “energy sea” is itself fluctuating rather than a continuous background or a fixed lattice. Stable large-scale geometry, locality, and field behaviour would then be collective properties of a constrained stochastic network. Quaternionic link variables are considered because they offer associative, noncommutative spinorial transport with a scalar-plus-three-vector decomposition.

This intuition does not determine a graph ensemble, action, continuum limit, signature, interaction, or gravitational sector. Those are separate mathematical problems.

## Part II — Numbered working hypotheses

Every item in this part is a working hypothesis, not an established conclusion.

### H1 — Dynamic graph

Fundamental spacetime is not assumed to be continuous or based on a fixed lattice. The microscopic substrate is hypothesized to be a dynamically evolving graph or network.

Candidate microscopic changes include:

- fluctuating link strengths;
- graph rewiring;
- possibly vertex creation or removal.

For a first toy model, link fluctuations and graph rewiring may be studied before vertex creation. The motivating PI intuition is that the underlying energy sea is itself fluctuating.

### H2 — Constrained stochasticity

The microscopic network is hypothesized to be random or stochastic, but not an unconstrained uniform random graph. Its evolution is expected to obey local weights, transition rules, an action, or another dynamical constraint.

Possible required properties include:

- finite or controlled average degree;
- suppression of arbitrarily nonlocal links;
- stable local motifs or domains;
- an energetic or entropic cost for graph changes.

Microscopic randomness does not imply the absence of dynamical law.

### H3 — Fermions on vertices

Candidate fundamental matter degrees of freedom are fermionic variables attached to graph vertices:

\[
\psi_i.
\]

This note does not choose a final flavor, generation, gauge, or representation structure.

### H4 — Spinorial link transporter

Each active link may carry:

1. a bond strength or magnitude;
2. a spinorial transport variable.

Candidate notation:

\[
Q_{ij}=\rho_{ij}U_{ij},
\]

where:

- \(\rho_{ij}\) is a bond-strength, hopping-strength, or distance-related degree of freedom;
- \(U_{ij}\) is a spinorial link transporter.

The transporter is not initially called a fundamental spin connection, because that would risk presupposing the geometry the model is intended to generate.

In an infrared geometric regime, the spinorial transporter may be interpreted as an effective spin connection.

### H5 — Quaternionic candidate

The transporter may be quaternion-valued:

\[
U_{ij}\in\mathbb H,
\]

or, in a norm-preserving sector,

\[
U_{ij}\in SU(2)\simeq\{\text{unit quaternions}\}.
\]

The candidate motivation is:

- quaternions are four-dimensional over the reals;
- they have a natural scalar-plus-three-vector decomposition;
- they are noncommutative but associative;
- unit quaternions naturally encode spinorial rotations;
- \(SU(2)\) double-covers \(SO(3)\);
- quaternionic multiplication naturally carries orientation and rotation information.

These facts do not prove that the resulting network has four effective spacetime dimensions.

**Algebraic dimension**

\[
\dim_{\mathbb R}\mathbb H=4.
\]

**Spectral or effective dimension**

The large-scale dimension inferred from propagation, diffusion, correlation scaling, or return probability.

Algebraic dimension four does not automatically imply spectral dimension four.

### H6 — Possible algebraic selection principle

Quaternions may be selected by requiring a link algebra that is simultaneously:

- real;
- norm-compatible;
- locally invertible;
- associative;
- noncommutative;
- capable of spinorial transport.

A useful comparison is:

| Algebra | Candidate discriminator |
|---|---|
| \(\mathbb R\) | commutative and too simple for the proposed transport role |
| \(\mathbb C\) | commutative |
| \(\mathbb H\) | noncommutative but associative |
| \(\mathbb O\) | nonassociative |

The Frobenius theorem settles the classification of finite-dimensional associative real division algebras as \(\mathbb R\), \(\mathbb C\), and \(\mathbb H\). The open work is not to re-prove that classification, but to justify the proposed requirement list and show that those requirements are physically and mathematically appropriate for link transport. This remains a candidate algebraic-selection argument, not a completed uniqueness proof for the microscopic model.

### H7 — Locality from stable domains

The candidate hypothesis is more precise than “locality is a domain wall”:

> Effective locality is generated by stable strongly connected domains; domain walls delimit or suppress communication between such effective local regions.

An illustrative candidate graph distance is:

\[
d(i,j)=\min_{\text{paths }i\to j}
\sum_{(kl)\in\text{path}}\ell_{kl},
\]

with a possible candidate relation:

\[
\ell_{ij}\sim-\log|\rho_{ij}|.
\]

These expressions are illustrative definitions only, not derived results.

### H8 — Curvature from link holonomy

For an oriented closed loop \(\gamma\), define schematically:

\[
U_\gamma=U_{12}U_{23}\cdots U_{n1}.
\]

Quaternionic or spinorial transporters need not commute. A nontrivial loop product may therefore encode frustration or an effective curvature in a coarse-grained description.

Candidate interpretation:

```text
nontrivial link holonomy
    → effective curvature in an infrared geometric description
```

No Einstein curvature tensor has been derived.

### H9 — Emergent Lorentz symmetry

Microscopic Lorentz invariance is not assumed. The PI hypothesis is that Lorentz symmetry is an infrared statistical or universality phenomenon.

Random directional averaging alone is insufficient. A viable model would have to explain:

- a common low-energy limiting speed;
- suppression of Lorentz-violating operators;
- emergence of boost symmetry, not only rotational isotropy;
- an effective Lorentzian signature;
- consistency across all low-energy particle species.

Lorentz invariance is hypothesized to arise as an infrared universality property of the stochastic network, not merely as an arithmetic average over random microscopic directions.

### H10 — No ontological continuum

The PI position is that fundamental continuum spacetime is not assumed to exist. This does not remove the need for an effective large-scale description.

> No ontological continuum limit is postulated. Continuum field theory may nevertheless emerge as an infrared statistical description valid at scales much larger than the network correlation length.

Appropriate candidate terms include:

- infrared scaling regime;
- hydrodynamic regime;
- coarse-grained geometric regime;
- effective continuum description.

A scaling regime or large-scale limit is still required if the model is to reproduce continuum observations.

### H11 — Candidate origin of the four-fermion interaction

The current leading hypothesis is that the effective four-fermion interaction is generated by integrating out massive or short-range spinorial link fluctuations.

A schematic candidate hopping action is:

\[
S_{\rm hop}\sim
\sum_{\langle ij\rangle}
\bar\psi_iQ_{ij}\psi_j+\mathrm{h.c.}
\]

A link action is written only schematically:

\[
S_Q\sim\frac12 QKQ+\cdots.
\]

Formally, one may investigate whether:

\[
\int\mathcal DQ\,
e^{i(S_Q+S_{\rm hop})}
\quad\Longrightarrow\quad
S_{\rm eff}^{(4\psi)}
\sim
-(\bar\psi\Gamma\psi)\,
K^{-1}\,
(\bar\psi\Gamma\psi).
\]

The sign, channel structure, locality, flavor structure, tensor structure, and number of independent couplings must all be derived from the microscopic link kernel. This note does not select or freeze a canonical interaction.

## Part III — Ranked candidate sources of the four-fermion term

The current research prioritization is:

1. **Dynamic spinorial or quaternionic link fluctuations.** This most directly matches the proposed network ontology and supplies a concrete field to integrate out.
2. **Connectivity or local-volume fluctuations.** These may naturally generate density or scalar channels, but their operator content must be derived.
3. **A domain-order parameter.** This is calculationally clear but adds a new bosonic field rather than deriving all structure from links.
4. **High-energy fermion modes.** Integrating out free high-energy fermions alone generally does not generate an arbitrary four-fermion interaction without pre-existing interactions.

This ranking is a research choice, not evidence that the first mechanism works.

## Part IV — Coupling-sign hypothesis

The effective interaction sign should not be assigned independently at each point or in each channel.

A randomly signed bare mean may vanish, while a zero-mean fluctuating field can still generate a nonzero effective interaction through its covariance or variance. The resulting sign depends on the microscopic kernel, propagator, analytic-continuation convention, and Fierz structure.

> The effective coupling signs and channel ratios must be determined by a common microscopic covariance or kernel rather than assigned independently.

## Part V — Graph growth and the former “species doubling” intuition

The PI intuition that new lattice sites or graph growth may be related to cosmic expansion is preserved as a hypothesis.

It is distinct from standard lattice species doubling:

- **Standard species doubling** is a momentum-space multiplicity of low-energy fermion zeros on a regular lattice.
- **Graph growth** is an increase in vertices, connectivity, graph volume, or low-energy network modes.

Neutral candidate terminology includes **graph-growth-induced mode proliferation** and **spectral mode proliferation**.

A speculative chain is:

```text
vertex or graph-volume growth
    → increase or rearrangement of low-energy network modes
    → effective vacuum-energy or expansion dynamics
```

This does not explain cosmological expansion without further derivation.

When vertex creation is enabled, the model must connect consistently to the recorded space-generation mechanism:

\[
\frac{\dot N_{\rm site}}{N_{\rm site}}=3H.
\]

This is a falsifiable cross-check, not a consequence already derived from the network proposal.

Required future checks include:

- graph-volume growth;
- energy accounting;
- stability of effective dimension;
- preservation of low-energy dispersion;
- effective pressure or equation of state;
- consistency with \(\dot N_{\rm site}/N_{\rm site}=3H\);
- distinction from ordinary fermion doubling.

## Part VI — Quaternionic \(1+3\) hypothesis

The structural observation is:

\[
q=q_0+q_1i+q_2j+q_3k
=q_0+\mathbf q.
\]

This supplies a natural scalar-plus-three-vector decomposition. Open interpretations include:

- the real component may encode coherence, bond magnitude, or a clock-like variable;
- the three imaginary components may encode spatial orientation or rotational transport;
- the split may contribute to an emergent \(1+3\) structure.

However:

- the ordinary quaternion norm is Euclidean;
- a Lorentzian \(3+1\) signature is not automatically produced;
- a vacuum-selection, complexification, dynamical signature mechanism, or separate interpretation of network time would still be required.

The former pure-imaginary-vacuum model is historical motivation only. It was abandoned because the relevant pure-imaginary point was a maximum rather than the physical minimum, and it is not reused here as an established mechanism.

## Part VII — Dimensional-selection question

The central unresolved question is:

> Can quaternionic link dynamics cause a dynamically random network to possess an infrared spectral dimension near four?

A candidate diagnostic is the return probability:

\[
P(\sigma)\sim\sigma^{-d_s/2},
\]

with scale-dependent spectral dimension:

\[
d_s(\sigma)
=-2\frac{d\log P(\sigma)}{d\log\sigma}.
\]

The future research target would be:

\[
d_s(\sigma)\to4
\]

over an infrared scaling window. This has not been demonstrated.

## Part VIII — Minimum calculable toy model

### Candidate degrees of freedom

\[
\psi_i,\qquad
\rho_{ij},\qquad
U_{ij}.
\]

### Candidate model characteristics

- a finite or statistically homogeneous random graph;
- controlled average degree;
- fermions on vertices;
- quaternionic or \(SU(2)\)-valued link transporters;
- bond magnitudes \(\rho_{ij}\);
- a quadratic massive fluctuation kernel for links;
- an optional plaquette or loop-holonomy term;
- no vertex creation in the first version;
- no claim of physical gravity in the first version.

### Candidate first calculations

1. Integrate out Gaussian link fluctuations.
2. Derive the resulting four-fermion operator.
3. Determine its sign and independent channel structure.
4. Test whether the result is local or bilocal.
5. Perform its Fierz decomposition.
6. Inspect whether a symmetric rank-two derivative bilinear can arise.
7. Calculate simple network propagation or return probability.
8. Test whether stable domains form.

## Part IX — Three-stage falsifiability programme

The following are research stages, **not registry gates**. No status change or gate registration is made by this note. A paper-owned registry gate, with working name `P2-HOPPING-4F-01`, may later be proposed and created through the normal governance process after checking identifier availability and defining its scope and kill criterion.

### Stage Q1 — Algebraic selection

Determine whether the imposed physical requirements genuinely select quaternionic transport over real, complex, or octonionic alternatives.

The Frobenius classification of associative real division algebras is settled mathematics. The open discriminator is whether the proposed requirements—especially associativity, local invertibility, norm compatibility, noncommutativity, and spinorial transport—are justified and jointly necessary for the microscopic links.

### Stage Q2 — Effective interaction and geometry

Determine whether integrating out quaternionic link fluctuations produces:

- a controlled effective four-fermion interaction;
- viable channel signs;
- a candidate vierbein or stress/frame-current structure;
- nontrivial coarse-grained holonomy.

If the Stage-Q2 derivation succeeds and yields an interaction different from the operative canonical axiom, that outcome falsifies the axiom and triggers a full-chain amendment. The derivation owes no loyalty to the Paper 2 minimal chiral pair \(L_0\).

### Stage Q3 — Dimensional and Lorentzian emergence

Determine whether the model produces:

- an infrared spectral dimension near four;
- a common low-energy light cone;
- suppressed Lorentz violation;
- an effective Lorentzian signature.

Failure at an earlier stage prevents promotion to the next stage. These stages organize future discrimination; they do not themselves open or close any programme or paper gate.

## Part X — Relationship to the Level taxonomy

The taxonomy label **Level 0** is unrelated to the Paper 2 manuscript's minimal chiral pair \(L_0\).

### Level 0

Retired as the main physical model. Retained as a historical and algebraic benchmark.

### Level 1

Current provisional effective-theory baseline. SI-2 has not yet run; recorded minimal-model headwinds (\(\xi_{\rm ind}<0\); repulsive vector channel) give an honest prior of `FAIL`.

### Level 2

Effective four-fermion theory derived from a microscopic network model.

### Level 3A

Ordinary vector current-current model. Deprioritized as the direct origin of gravity.

### Level 3B

Derivative, frame-current, or stress-current interactions. Retained as a possible gravity-relevant effective structure.

### Level 4

Bond/link microscopic model. Highest-priority controlled bridge to Level 2.

### Level 5

Dynamic stochastic network programme. Long-term microscopic framework, presently non-canonical.

This document develops a Level-5 candidate in a restricted **Level-5-lite** form: fixed vertex count, controlled stochastic graph/link evolution, and a Gaussian link sector intended to make the first integration tractable.

## Part XI — Explicit non-claims

> **NON-CANONICAL SCOPE:** this note preserves a candidate microscopic idea. It owns no established evidence, changes no paper or gate, and confers no status on the candidate.

This document does **not** claim that:

- the candidate model is correct;
- fundamental spacetime is proven to be discrete;
- quaternions are proven to select four dimensions;
- algebraic dimension implies spectral dimension;
- Lorentz invariance has been derived;
- a Lorentzian signature has been derived;
- domain walls fully define locality;
- graph growth explains cosmic expansion;
- species doubling explains expansion;
- gravity has been derived;
- a massless spin-2 pole exists;
- universal coupling to \(T_{\mu\nu}\) exists;
- the Einstein equations have been obtained;
- the canonical four-fermion interaction has been fixed;
- Paper 2 must adopt this candidate model.

If Stage Q2 derives an interaction different from the operative canonical axiom, the derivation would falsify that axiom and require a governed full-chain amendment. This is a possible future discriminator, not a current claim about the result.

## Part XII — Open questions

1. What exact graph ensemble or stochastic evolution rule is used?
2. What fixes the average graph degree and effective dimensionality?
3. Are vertices created and removed, or only links rewired?
4. What is the exact quaternionic or spinorial link action?
5. Is \(U_{ij}\) a unit quaternion, a general quaternion, or a larger Clifford element?
6. What is the role of the bond magnitude \(\rho_{ij}\)?
7. What microscopic field is massive enough to integrate out?
8. What four-fermion operator is generated?
9. Are the resulting coupling signs healthy and uniquely fixed?
10. Which Fierz channels are independent?
11. Can a symmetric rank-two derivative bilinear arise naturally?
12. Can an effective vierbein be defined without assuming geometry?
13. Can nontrivial link holonomy reproduce a geometric curvature description?
14. Why does the infrared spectral dimension approach four?
15. Why is the infrared signature Lorentzian rather than Euclidean?
16. Why do all low-energy species share a common limiting speed?
17. How is microscopic Lorentz violation suppressed?
18. How are locality and causal propagation defined?
19. How is energy conserved under graph rewiring or vertex creation?
20. Can graph growth generate an acceptable cosmological effective stress tensor?
21. How is standard lattice species doubling treated?
22. What observations could falsify the model?

## Part XIII — Possible future observables and tests

If the minimum toy model survives Stages Q1 and Q2, future tests could include:

- diffusion return probability and a scale-dependent \(d_s(\sigma)\);
- low-energy dispersion relations for multiple fermion species;
- universality or splitting of limiting speeds;
- coefficients of leading Lorentz-violating operators;
- distribution and stability of strongly connected domains;
- holonomy statistics around minimal and coarse-grained loops;
- locality range of the induced four-fermion kernel;
- sign and Fierz-channel content of the induced interaction;
- energy and effective stress associated with controlled graph growth;
- compatibility of graph growth with \(\dot N_{\rm site}/N_{\rm site}=3H\).

Every quantitative test would require a separately specified model, conventions, reproducible implementation, and governed evidence record. None is supplied by this brainstorming note.
