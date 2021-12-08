all: install-deps

.PHONY: install-deps
install-deps:
	@pip install --upgrade pip setuptools
	@pip install -e ".[testing]"

.PHONY: start
start:
	@pserve development.ini --reload

.PHONY: test
test:
	@pytest