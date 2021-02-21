#!/usr/bin/env sh

set -x
set -e

python -m pip install --upgrade pip
pip install poetry
poetry config virtualenvs.create false
poetry install --no-root --no-interaction
