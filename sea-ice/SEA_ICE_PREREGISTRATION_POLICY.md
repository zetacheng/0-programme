# Sea–Ice Cosmology — Pre-registration Policy

Status: PROPOSED
Version: draft 2026-07-19
Owner: `0-programme`

This policy makes the anti-escape principle enforceable. Each freeze below
is recorded, in the owning paper repo, as a committed document with a hash,
**before** the decisive calculation that depends on it. A calculation whose
freeze is not committed first is not admissible evidence.

## 1. Channel freeze — `P2-CHANNEL-FREEZE-01`

Before `P2-MULTIPHASE-GRAV-01` runs, the complete Hubbard–Stratonovich /
Fierz channel basis is frozen. The freeze document records:

- the original four-fermion interaction, verbatim;
- the complete independent bilinear basis (scalar, pseudoscalar, vector,
  axial, tensor — as the interaction's symmetry dictates);
- the Fierz identities relating them;
- which channels are **included** in `K_ij`;
- which channels are **excluded**, and why (symmetry, redundancy);
- the commit hash of the freeze.

Rationale: a `∀ phase` death gate is only meaningful if the channel list is
fixed. If channels can be added after a FAIL, the universal quantifier
silently degrades to "∃ over an ever-growing basis," and SI-2 can be
postponed indefinitely by appending one more channel. The HS decomposition
of a given interaction is finite and (up to Fierz) unique; it can be
written out in full. After the freeze, adding a channel is an extension
(AE-4), not a continuation.

## 2. Phase freeze

Before the SI-2 scan, the admissible-phase list is frozen. An admissible
phase must satisfy all of:

1. it is a stationary solution of the full effective action from the fixed
   theory;
2. all its condensates come from frozen channels;
3. its quadratic fluctuation operator is well-defined;
4. it is not excluded by an already-established gate;
5. its parameters lie within the pre-registered microscopic parameter
   domain (see §4);
6. it requires no new interaction or degree of freedom beyond the frozen
   set.

A phase found only by introducing new microscopic structure belongs to a
later extension and cannot rescue the simplest framework.

## 3. CLEAN-PASS metric freeze (SI-2)

This closes a gap that the three-tier PASS would otherwise open. "CLEAN vs
CONDITIONAL" cannot be judged after seeing the result. Before the SI-2
scan, register:

- the **parameter space** over which volume is measured;
- the **measure** on it (explicit — e.g. flat in stated variables, or a
  stated prior);
- the **minimum healthy volume** (as a fraction of the registered
  parameter domain) that qualifies as CLEAN rather than CONDITIONAL;
- the **perturbation magnitude** under which a CLEAN phase must remain
  healthy.

Without this freeze, a fine-tuned point could be reported as CLEAN by
choosing a flattering measure after the fact — precisely the retrospective
adjustment AE-3 forbids.

## 4. Parameter-domain freeze

The microscopic parameter domain (couplings, cutoff ratios, density/μ
ranges) is registered before SI-1/SI-2. A healthy phase found *outside*
this domain does not count for the simplest framework; it is an extension.

## 5. Observable and window freeze (SI-4, SI-6)

For each phenomenological gate, before evaluation, register: the precise
derived observable; the parameter values inherited from upstream gates; the
observational comparison window; the treatment of cosmological evolution;
and the permitted theoretical uncertainty.

- **SI-4 (`P4-INTERFACE-DE-01`)** — primary target is `ρ_DE,obs` (or an
  equivalent such as `H_0² Ω_Λ`). **Flagged high-risk:** the natural
  interface scale is likely `~Λ_micro⁴`, tens of orders above
  `ρ_DE,obs ~ (10⁻³ eV)⁴`. The default expectation is failure by scale
  mismatch unless a suppression mechanism (sequestering, exponential
  suppression, geometric dilution, collective cancellation, critical
  scaling) is *derived from the fixed theory* — not inserted. Register the
  window anyway and compute; do not presume the outcome, but do not present
  SI-4 as a routine downstream step.
- **SI-6 (`P1-SEAICE-RAR-01`)** — `a_0` must be derived from microscopic /
  interface parameters, not fitted. The empirical RAR interpolation
  function may not be used as an input. Register the galaxy sample and the
  benchmark before fitting.

## 6. No retrospective target adjustment (AE-3, restated operationally)

After a result is obtained, no window, admissible-phase list, channel
basis, CLEAN-PASS threshold, or failure criterion may be changed to alter
the verdict. A changed target is a new hypothesis with a new gate and a new
version. The prior freeze commit stands in the record as what was actually
registered.

## 7. Robustness classification (SI-2), restated

- CLEAN PASS — healthy region of at least the registered minimum volume,
  perturbation-stable. Supports continuation.
- CONDITIONAL PASS (fine-tuned) — isolated point / zero-measure / sub-minimum
  band / fine cancellation. Technical follow-up only; not a success.
- FAIL — `∀ phase: ¬HealthyGravity`. Hard termination (AE-1).

## 8. Extension policy (AE-4, restated operationally)

A declared extension `T0 → T1` states: the added structure; the failed gate
motivating it; the prior results that still hold; the prior claims that no
longer transfer; the new prediction constraining it; and its own kill
criterion. It inherits no evidential status from `T0`.
