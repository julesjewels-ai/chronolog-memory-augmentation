PYTHON = venv/bin/python
PIP = venv/bin/pip
PYTEST = venv/bin/pytest

.PHONY: install run test clean

install:
	python3 -m venv venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "\nEnvironment setup complete. Run 'make run' to start."

run:
	$(PYTHON) main.py --help

run-start:
	$(PYTHON) main.py start --interval 2

test:
	$(PYTEST) -v

clean:
	rm -rf venv
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +