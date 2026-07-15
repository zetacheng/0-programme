PYTHON ?= python

.PHONY: structure lint test check

structure:
	$(PYTHON) -m pytest tests/test_repository_structure.py

lint:
	$(PYTHON) -m ruff check .

test:
	$(PYTHON) -m pytest

check: lint test structure
