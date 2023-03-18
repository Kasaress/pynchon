VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
ROOT = pynchon_wiki

all:
	@echo "make requirements	- Install all project requirements"
	@echo "make migrations		- Create migrations of changed models"
	@echo "make migrate		- Migrate changes to db of changed models"
	@echo "make seed		- Seed database with fake data"
	@echo "make import		- Import database with real data from csv"
	@exit 0

requirements:
	$(PIP) install -r ${ROOT}/requirements.txt

migrations:
	$(PYTHON) ${ROOT}/manage.py makemigrations

migrate:
	$(PYTHON) ${ROOT}/manage.py migrate

seed:
	$(PYTHON) ${ROOT}/manage.py seed

import:
	$(PYTHON) ${ROOT}/manage.py import