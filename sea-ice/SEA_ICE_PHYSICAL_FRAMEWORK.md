# Sea–Ice Cosmology — Physical Framework

Status: PROPOSED (programme-level interpretation; owns no evidence of its own)
Version: draft 2026-07-19
Owner: `0-programme` (interpretation only)

## What this document is, and is not

This is the **physical narrative** for the existing lattice-fermion
programme. It supplies interpretation and vocabulary. It does **not** own
any claim, gate, or piece of evidence. Every testable proposition it makes
is owned, tested, and killed by a specific paper-level gate, listed in
`SEA_ICE_RESEARCH_MAP.md`. If this document and a paper's `CLAIMS.md` ever
disagree, the paper wins.

The reason for this separation is structural. The programme's honesty
machinery — version-numbered retractions, "claim status must match claim
text," the CLAIMS↔GATES guard, pinned-SHA migration — all operate at
**paper level**. A gate that floats above the papers would bypass that
machinery: when it failed, one could say "the framework is affected"
without any paper claim changing status. Sea–Ice is therefore not allowed
an independent evidential status. It is a lens, not a ledger.

## Fixed ontology

The microscopic realization is **fixed**, not open:

> **Sea = the lattice-fermion condensate defined by the existing
> microscopic theory** (Papers 2 and 3).

Sea, Ice, wrinkle, and bound excitation are physical interpretations of
structures that must be derived from the existing lattice-fermion action,
or from an explicitly declared extension of it. They are not placeholders
for arbitrary new microscopic theories.

The hierarchy:

    Lattice-Fermion Sea
        → Condensed Ice Phase          (emergent spacetime + low-energy fields)
        → Sea–Ice Interface            (phase boundary; tension; dynamics)
        → Interface Wrinkles           (instability / pattern of the interface)
        → Bound Dark-Matter Excitations (normalizable modes trapped by wrinkles)

Roles:

- **Sea** — the high-density / high-energy collective phase of the
  lattice-fermion system. Dynamics from the full effective action
  `Γ[Φ_i]`, where `Φ_i` ranges over the channels the microscopic theory
  already permits (scalar, vector, axial, tensor, … Hubbard–Stratonovich).
  Owned by Papers 2, 3.
- **Ice** — a stable condensed phase of the *same* theory, from a
  physically admissible, dynamically stable stationary point
  `δΓ/δΦ_i = 0`. Observable spacetime is identified with this phase, not
  with the underlying medium. Owned by Paper 2.
- **Dark energy** — the effective 4D background stress-energy of the
  Sea–Ice interface (phase-difference energy + interface tension). **Not**
  the failed monopole action, **not** an inserted cosmological constant,
  **not** an unspecified bulk vacuum. Owned by Paper 4.
- **Dark matter** — normalizable, long-lived modes bound to interface
  wrinkles. The wrinkles are the trap; the dark matter is the trapped
  mode. Mathematically distinct from the continuum topological soliton
  excluded in Paper 5. Owned by Paper 4, bounded by Paper 5.
- **Galactic dynamics** — the derived weak-field response of the Ice and
  its bound modes, yielding `g_obs(g_bar)` and a derived `a_0`. Owned by
  Paper 1.

## Anti-escape principle

The framework is falsifiable only under the following rules. They exist to
stop the framework from surviving by retreat.

### AE-1 — Fixed microscopic realization

The Sea is the lattice-fermion condensate already studied. If that theory
fails the programme-death gate (`P2-MULTIPHASE-GRAV-01`, see the map), the
simplest Sea–Ice framework is **exhausted**. It may not be preserved by
replacing the Sea with an unspecified strongly-coupled vacuum, a
pre-geometric medium, an alternative condensate, or any other microscopic
realization. Any such replacement is a new theory `T0 → T1`, and per AE-4
it starts with no inherited evidence.

### AE-2 — No mechanism substitution after failure

The primary dark-energy and dark-matter mechanisms are fixed (interface
stress-energy; wrinkle-bound modes). If either fails its registered gate,
it may not be silently replaced by another mechanism within the same
programme version. An alternative mechanism is a new extension, not a
reinterpretation of the failed claim.

### AE-3 — No retrospective target adjustment

Numerical windows, admissible phases, the channel basis, the CLEAN-PASS
volume threshold (see the map's SI-2 entry), observables, and failure
criteria must be registered **before** the decisive calculation. After a
result is in hand, an acceptance window may not be widened to admit it
without declaring a new hypothesis and a new gate. Freezes are recorded
with a commit/document hash in `SEA_ICE_PREREGISTRATION_POLICY.md`.

### AE-4 — Extensions do not inherit status

A declared extension `T0 → T1` must state: what structure is added; which
failed gate motivates it; which prior results still hold; which prior
claims no longer transfer automatically; what new prediction constrains
it; and what would kill it. An extension is never counted as confirmation
of the simplest programme.

## Honest prior on the central gate

The programme-death gate `P2-MULTIPHASE-GRAV-01` does **not** start from a
neutral position. Two facts already in the ledger bear against it:

- The minimal single-channel induced-gravity result gives `ξ_ind < 0` for
  `L ≫ 1` — the minimal substrate does not self-generate a positive
  `M_Pl²` (Paper 2).
- The one vector channel already computed is **repulsive**,
  `G_ω = -G/N` (Paper 3, `P3-C-001` VERIFIED). A repulsive vector entering
  the graviton kernel contributes to `M_Pl,eff²` in the direction that
  makes a healthy (attractive) Newtonian limit *harder*, not easier.

Channel mixing can in principle flip the sign of the physical spin-2
residue, which is exactly why the multiphase gate is worth running. But
the honest prior is that SI-2 is **more likely to fail than to pass**, and
the document should not read as though a healthy phase is expected. This is
recorded so that a PASS, if it comes, is recognized as a genuine and
somewhat surprising result rather than the default.

## Three possible programme outcomes

- **A — Simplest framework survives.** At least one admissible phase has
  healthy gravity (CLEAN PASS, see map), a microscopic interface exists,
  and both cosmological mechanisms pass their gates.
- **B — Partial survival.** Healthy gravity and a derived interface exist,
  but one or both cosmological mechanisms fail. Scientifically useful; does
  not deliver the proposed unification. (A dark-energy failure need not
  fail the galactic gate — the interface can exist while its stress-energy
  fails to account for `ρ_DE`.)
- **C — Simplest framework terminates.** `P2-CHANNEL-FREEZE-01`+`P2-PHASE-01`
  find no admissible phase, or `P2-MULTIPHASE-GRAV-01` finds every
  admissible phase gravitationally pathological. Further work proceeds only
  as a separately labeled extension (AE-4).

## Core testable hypothesis

> The fixed lattice-fermion condensate possesses at least one stable phase
> with healthy emergent gravity; this phase coexists with another through a
> microscopically derived finite-tension interface whose background
> stress-energy accounts for the observed dark-energy scale; dynamically
> generated wrinkles of that interface support long-lived bound modes
> behaving as cold dark matter; and the same effective theory reproduces
> the galactic radial-acceleration relation with a derived `a_0`.

This hypothesis is intended to be **killed** if the registered gates fail.
Sea–Ice supplies the narrative; the paper-level gates, frozen bases,
pre-registered windows, and hard failure rules supply the discriminator.
