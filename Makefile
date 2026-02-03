SHELL := /bin/bash

.PHONY: setup migrate run test

setup:
	python -m venv .venv
	. .venv/bin/activate && python -m pip install --upgrade pip
	. .venv/bin/activate && python -m pip install -r requirements.txt

migrate:
	. .venv/bin/activate && python manage.py migrate

run:
	. .venv/bin/activate && python manage.py runserver

test:
	. .venv/bin/activate && python manage.py test
