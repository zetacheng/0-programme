"""Governance guard for the canonical programme-state documents.

Mechanically enforces the landing invariants for ``docs/PROGRAMME_STATE.md``
and the root ``CURRENT_STATUS.md``. These checks are structural only.

NOTE: this guard deliberately does NOT attempt to prove that no historical
``PROGRAMME_STATE.md`` version was silently skipped. Changelog completeness
against the true version history remains a Discriminator/PI review
responsibility; this test only verifies the invariants stated in each
function below.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROGRAMME_STATE = ROOT / "docs" / "PROGRAMME_STATE.md"
CURRENT_STATUS = ROOT / "CURRENT_STATUS.md"


def _parse_header_table(text: str) -> dict:
    """Return ``{key: value}`` from the leading two-column Markdown table.

    Reads consecutive ``| key | value |`` rows, skipping the ``| Field | Value |``
    header and the ``|---|---|`` separator, and stops at the first non-table
    line once the table has begun. Only surrounding whitespace is trimmed from
    each cell.
    """
    rows: dict = {}
    started = False
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            if started:
                break
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if len(cells) != 2:
            if started:
                break
            continue
        key, value = cells
        if set(key) <= {"-"} and set(value) <= {"-"}:  # |---|---| separator
            continue
        if key.lower() == "field" and value.lower() == "value":
            started = True
            continue
        started = True
        rows[key] = value
    return rows


def _programme_state_header() -> dict:
    assert PROGRAMME_STATE.is_file(), "docs/PROGRAMME_STATE.md is missing"
    return _parse_header_table(PROGRAMME_STATE.read_text(encoding="utf-8"))


def _lookup(header: dict, prefix: str):
    """First header value whose key starts with ``prefix`` (case-insensitive)."""
    for key, value in header.items():
        if key.lower().startswith(prefix.lower()):
            return value
    return None


def test_programme_state_header_is_canonical_not_draft() -> None:
    """Version is not a draft; Status/Approved by/Discriminator are decided."""
    header = _programme_state_header()

    version = header.get("Version")
    assert version, "header table has no non-empty 'Version' field"
    assert not version.lower().endswith("-draft"), (
        f"Version must not end in '-draft': {version!r}"
    )

    for field in ("Status", "Approved by", "Discriminator"):
        value = _lookup(header, field)
        assert value, f"header table is missing or has an empty '{field}' field"
        low = value.lower()
        assert "pending" not in low and "draft" not in low, (
            f"header field {field!r} must not contain 'pending' or 'draft': {value!r}"
        )


def test_programme_state_changelog_integrity() -> None:
    """The §8 changelog carries the header Version once, with unique labels."""
    text = PROGRAMME_STATE.read_text(encoding="utf-8")

    section = re.search(
        r"^##\s+8\.\s+Changelog\s*$(?P<body>.*)\Z",
        text,
        flags=re.MULTILINE | re.DOTALL,
    )
    assert section, "no '## 8. Changelog' section found"
    changelog = section.group("body")

    # Changelog entries look like: '- **1.0 (2026-07-21)** — ...'. The version
    # label is the first whitespace-delimited token inside the bold span.
    bold_labels = re.findall(r"^-\s+\*\*(.+?)\*\*", changelog, flags=re.MULTILINE)
    version_labels = [label.split()[0] for label in bold_labels]
    assert version_labels, "no changelog entry labels parsed from the §8 section"

    version = _programme_state_header()["Version"]
    assert version in version_labels, (
        f"header Version {version!r} is not present as a changelog entry label; "
        f"changelog labels found: {version_labels}"
    )

    # Version labels must be unique; a duplicate would mean two entries claim the
    # same version. (This does NOT prove the history is gap-free — see module doc.)
    assert len(version_labels) == len(set(version_labels)), (
        f"duplicate changelog version labels: {version_labels}"
    )


def test_canonical_main_shas_match_between_documents() -> None:
    """The 'Canonical main SHAs' header value is byte-identical in both files."""
    assert CURRENT_STATUS.is_file(), "CURRENT_STATUS.md is missing at the repo root"

    ps_header = _programme_state_header()
    cs_header = _parse_header_table(CURRENT_STATUS.read_text(encoding="utf-8"))

    ps_value = ps_header.get("Canonical main SHAs")
    cs_value = cs_header.get("Canonical main SHAs")
    assert ps_value, "PROGRAMME_STATE.md header lacks a 'Canonical main SHAs' value"
    assert cs_value, "CURRENT_STATUS.md header lacks a 'Canonical main SHAs' value"

    assert ps_value == cs_value, (
        "'Canonical main SHAs' drift between the two documents:\n"
        f"  docs/PROGRAMME_STATE.md: {ps_value!r}\n"
        f"  CURRENT_STATUS.md:       {cs_value!r}"
    )
