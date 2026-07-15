## Programme change

Describe the programme-level coordination or infrastructure change.

## Owning repositories and provenance

List every affected paper repository, source commit, and authoritative record. Use `Not applicable` for infrastructure-only changes.

## Gates, claims, and dependencies

List affected programme gates, global claims, and dependency IDs. Confirm that detailed paper gates are not duplicated here.

## Synchronization

- [ ] `SYNC_STATUS.md` is updated if any paper status changed.
- [ ] Downstream repositories affected by a failed or changed upstream gate were audited.
- [ ] Convention conflicts were recorded explicitly.
- [ ] No complete manuscript, authoritative derivation, or production scientific code was added.
- [ ] No unreviewed scientific result was promoted.

## Validation

- [ ] `make lint`
- [ ] `make test`
- [ ] `make structure`
