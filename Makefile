# bob_AI — AI Foundations Course (macOS / Linux convenience targets)
# Windows users: use run.bat instead.

PY := python3
VENV := .venv
BIN := $(VENV)/bin

.PHONY: help setup check clean

help:
	@echo "bob_AI targets:"
	@echo "  make setup   - create venv and install requirements"
	@echo "  make check   - verify the environment is ready"
	@echo "  make clean   - remove the virtual environment"

setup:
	$(PY) -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -r requirements.txt
	@echo ""
	@echo "Setup complete. Next: make check"

check:
	$(BIN)/python module_01_setup/setup_check.py

clean:
	rm -rf $(VENV)
	@echo "Removed $(VENV)."
