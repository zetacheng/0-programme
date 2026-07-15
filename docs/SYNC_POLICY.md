# Repository Synchronization Policy

## Branches

```text
sync/<paper-name>
programme/<programme-topic>
review/<cross-paper-review>
fix/<infrastructure-issue>
archive/<retired-programme-route>
```

## Rules

- `main` contains accepted programme metadata only.
- Scientific calculations remain in paper repositories.
- Synchronization work occurs on a `sync/` branch.
- Do not squash scientific history when importing references.
- Tags mark programme-level milestones.

## Synchronization record

Every synchronization must identify the owning paper repository, accepted commit, source records reviewed, conventions checked, affected dependencies, and programme files updated. A paper status change is incomplete until `SYNC_STATUS.md` is updated.
