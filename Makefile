all: install-deps

.PHONY: install-deps
install-deps:
	@pip install --upgrade pip setuptools
	@pip install -e ".[dev]"

.PHONY: start
start:
	@pserve development.ini --reload

.PHONY: test
test:
	@pytest --cov --cov-report=term-missing

.PHONY: format
format:
	@black joker