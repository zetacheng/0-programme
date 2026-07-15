from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = {
    ".github/ISSUE_TEMPLATE/cross-paper-gate.yml",
    ".github/ISSUE_TEMPLATE/programme-decision.yml",
    ".github/ISSUE_TEMPLATE/synchronization.yml",
    ".github/pull_request_template.md",
    ".github/workflows/ci.yml",
    ".gitignore",
    "AGENTS.md",
    "CITATION.cff",
    "CROSS_PAPER_CONVENTIONS.md",
    "DEPENDENCIES.md",
    "GLOBAL_CLAIMS.md",
    "GLOBAL_DECISION_LOG.md",
    "GLOBAL_GATES.md",
    "HANDOFF.md",
    "LICENSE",
    "MASTER_PROGRESS.md",
    "MASTER_ROADMAP.md",
    "Makefile",
    "PAPER_MAP.md",
    "README.md",
    "SYNC_STATUS.md",
    "archive/README.md",
    "docs/CROSS_PAPER_GATE_POLICY.md",
    "docs/RESEARCH_WORKFLOW.md",
    "docs/RESULT_STATUS_POLICY.md",
    "docs/SYNC_POLICY.md",
    "handoffs/README.md",
    "handoffs/chatgpt-to-codex/.gitkeep",
    "handoffs/claude-to-pi/.gitkeep",
    "handoffs/codex-to-claude/.gitkeep",
    "papers/README.md",
    "papers/paper1.md",
    "papers/paper2.md",
    "papers/paper3.md",
    "papers/paper4.md",
    "papers/paper5.md",
    "programme/CRITICAL_PATH.md",
    "programme/FAILURE_REGISTER.md",
    "programme/ONTOLOGY.md",
    "programme/THEORY_MAP.md",
    "programme/VISION.md",
    "pyproject.toml",
    "reviews/README.md",
    "reviews/programme/.gitkeep",
    "tests/README.md",
    "tests/test_repository_structure.py",
}

REQUIRED_DIRECTORIES = {
    ".github/ISSUE_TEMPLATE",
    ".github/workflows",
    "archive",
    "docs",
    "handoffs/chatgpt-to-codex",
    "handoffs/claude-to-pi",
    "handoffs/codex-to-claude",
    "papers",
    "programme",
    "reviews/programme",
    "tests",
}


def test_required_files_exist() -> None:
    missing = sorted(path for path in REQUIRED_FILES if not (ROOT / path).is_file())
    assert not missing, f"Missing required files: {missing}"


def test_required_directories_exist() -> None:
    missing = sorted(path for path in REQUIRED_DIRECTORIES if not (ROOT / path).is_dir())
    assert not missing, f"Missing required directories: {missing}"


def test_repository_declares_programme_identity() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert readme.startswith("# 0-programme")
    assert "contains no complete paper manuscript" in readme
