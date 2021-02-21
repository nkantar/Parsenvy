#!/usr/bin/env sh

python -m pip install --upgrade pip
pip install poetry
poetry config virtualenvs.create false
poetry install --no-root --no-interaction
