import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REGISTER_FILES = (
    ROOT / "DEPENDENCIES.md",
    ROOT / "GLOBAL_CLAIMS.md",
    ROOT / "GLOBAL_DECISION_LOG.md",
    ROOT / "GLOBAL_GATES.md",
    ROOT / "programme" / "CRITICAL_PATH.md",
    ROOT / "programme" / "FAILURE_REGISTER.md",
    ROOT / "reviews" / "PROG-SYNC-01.md",
)

PAPER_GATE_REF = re.compile(
    r"paper-owned:(?P<repository>[a-z0-9][a-z0-9.-]*)#"
    r"(?P<gate>P[1-5]-[A-Z0-9][A-Z0-9/-]*)"
)
GLOBAL_GATE_REF = re.compile(r"\b(?:PROG|PG)-[A-Z0-9][A-Z0-9-]*\b")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def without_fenced_code(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)


def split_markdown_row(line: str) -> list[str]:
    return [cell.strip().replace(r"\|", "|") for cell in re.split(r"(?<!\\)\|", line)[1:-1]]


def markdown_tables(path: Path) -> list[list[dict[str, str]]]:
    lines = read(path).splitlines()
    tables: list[list[dict[str, str]]] = []
    index = 0
    while index + 1 < len(lines):
        if not lines[index].startswith("|") or not lines[index + 1].startswith("|"):
            index += 1
            continue
        header = split_markdown_row(lines[index])
        separator = split_markdown_row(lines[index + 1])
        if len(header) != len(separator) or not all(
            re.fullmatch(r":?-{3,}:?", cell) for cell in separator
        ):
            index += 1
            continue
        rows: list[dict[str, str]] = []
        index += 2
        while index < len(lines) and lines[index].startswith("|"):
            cells = split_markdown_row(lines[index])
            assert len(cells) == len(header), f"Malformed table row in {path}: {lines[index]}"
            rows.append(dict(zip(header, cells, strict=True)))
            index += 1
        tables.append(rows)
    return tables


def table_with_column(path: Path, column: str) -> list[dict[str, str]]:
    matches = [table for table in markdown_tables(path) if table and column in table[0]]
    assert len(matches) == 1, f"Expected one table with {column!r} in {path}"
    return matches[0]


def backticked_vocabulary(text: str, anchor: str) -> set[str]:
    anchored = text[text.index(anchor) :]
    paragraph = anchored.split("\n\n", 1)[0]
    return set(re.findall(r"`([A-Z]+)`", paragraph))


def test_global_gate_references_resolve() -> None:
    gates_text = without_fenced_code(read(ROOT / "GLOBAL_GATES.md"))
    headings = set(re.findall(r"^## ((?:PROG|PG)-[A-Z0-9-]+)\b", gates_text, re.MULTILINE))
    references: set[str] = set()
    for path in REGISTER_FILES:
        text = without_fenced_code(read(path))
        text = re.sub(r"^## ((?:PROG|PG)-[A-Z0-9-]+)\b.*$", "", text, flags=re.MULTILINE)
        references.update(GLOBAL_GATE_REF.findall(text))
    unknown = sorted(references - headings)
    assert not unknown, f"Unknown global gate references: {unknown}"


def test_paper_owned_gate_references_have_repository_and_gate() -> None:
    for path in REGISTER_FILES:
        text = without_fenced_code(read(path))
        starts = [match.start() for match in re.finditer(r"paper-owned:", text)]
        matches = {match.start(): match.group(0) for match in PAPER_GATE_REF.finditer(text)}
        missing = [text[start : start + 80].split()[0] for start in starts if start not in matches]
        assert not missing, f"Malformed paper-owned gate references in {path}: {missing}"


def test_paper_owned_gate_repositories_are_registered() -> None:
    repositories = set(re.findall(r"`zetacheng/([^`]+)`", read(ROOT / "PAPER_MAP.md")))
    for path in REGISTER_FILES:
        for match in PAPER_GATE_REF.finditer(without_fenced_code(read(path))):
            assert match.group("repository") in repositories, (
                f"Unregistered owner {match.group('repository')!r} in {path}"
            )


def test_gate_columns_require_explicit_paper_owners() -> None:
    gate_columns = {
        ROOT / "DEPENDENCIES.md": ("Upstream gate", "Downstream gate"),
        ROOT / "GLOBAL_CLAIMS.md": ("Owning gate",),
        ROOT / "programme" / "FAILURE_REGISTER.md": ("Failed gate",),
    }
    for path, columns in gate_columns.items():
        tables = markdown_tables(path)
        for table in tables:
            if not table:
                continue
            for column in columns:
                if column not in table[0]:
                    continue
                for row in table:
                    cell = row[column]
                    remainder = PAPER_GATE_REF.sub("", cell)
                    remainder = re.sub(r"[\s`;,.—-]", "", remainder)
                    assert not remainder, f"Bare or malformed gate reference in {path}: {cell}"


def test_failure_entries_have_evidence() -> None:
    rows = table_with_column(ROOT / "programme" / "FAILURE_REGISTER.md", "Failure ID")
    assert rows
    assert all(row["Evidence"].strip() for row in rows)


def test_failure_ids_are_unique() -> None:
    rows = table_with_column(ROOT / "programme" / "FAILURE_REGISTER.md", "Failure ID")
    identifiers = [row["Failure ID"] for row in rows]
    assert len(identifiers) == len(set(identifiers)), f"Duplicate failure IDs: {identifiers}"


def test_global_claims_have_owning_repository_and_claim_id() -> None:
    rows = table_with_column(ROOT / "GLOBAL_CLAIMS.md", "Global claim ID")
    repositories = set(re.findall(r"`zetacheng/([^`]+)`", read(ROOT / "PAPER_MAP.md")))
    for row in rows:
        owner = row["Owning repository"].strip("`")
        assert owner.startswith("zetacheng/")
        assert owner.removeprefix("zetacheng/") in repositories
        assert row["Owning claim ID"].strip()


def test_register_statuses_use_defined_vocabularies() -> None:
    dependency_text = read(ROOT / "DEPENDENCIES.md")
    dependency_statuses = set(
        re.findall(r"^- `([A-Z]+)`$", dependency_text, flags=re.MULTILINE)
    )
    claim_text = read(ROOT / "GLOBAL_CLAIMS.md")
    claim_statuses = backticked_vocabulary(claim_text, "Allowed statuses are")
    gate_text = without_fenced_code(read(ROOT / "GLOBAL_GATES.md"))
    gate_statuses = backticked_vocabulary(gate_text, "Allowed status values are")

    for row in table_with_column(ROOT / "DEPENDENCIES.md", "Dependency ID"):
        assert row["Status"] in dependency_statuses
    for row in table_with_column(ROOT / "GLOBAL_CLAIMS.md", "Global claim ID"):
        assert row["Status"] in claim_statuses

    recorded_gate_statuses = re.findall(r"^Status: ([A-Z]+)$", gate_text, flags=re.MULTILINE)
    assert recorded_gate_statuses
    assert set(recorded_gate_statuses) <= gate_statuses
