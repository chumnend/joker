all: install-deps

.PHONY: install-deps
install-deps:
	@pip install --upgrade pip setuptools
	@pip install -e .

.PHONY: start
start:
	@pserve development.ini --reload
