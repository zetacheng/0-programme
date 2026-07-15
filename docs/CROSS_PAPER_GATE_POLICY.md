# Cross-Paper Gate Policy

Programme gates govern questions whose acceptance or failure changes more than one paper. Detailed calculations and paper-specific gate records stay in the owning paper repository.

## Opening a programme gate

A gate must identify the cross-paper question, upstream repositories and paper gates, downstream consequences, locked assumptions, required evidence, and kill criterion. Its initial status is `PROPOSED`.

## Verdict and acceptance

A reviewer verdict does not by itself change programme direction. The Principal Investigator accepts or rejects the verdict, after which synchronization actions are recorded. A downstream paper may use an upstream result as accepted only after the upstream gate is closed and accepted.

## Failure propagation

A failed upstream gate triggers a synchronization audit of every registered downstream dependency. Failed and inconclusive records remain in the programme history.
