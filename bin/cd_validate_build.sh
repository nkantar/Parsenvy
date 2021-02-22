#!/usr/bin/env sh

set -x
set -e

VERSION=$(poetry version -s)

mkdir "validate_build"
cd "validate_build"
python -m venv "venv"
. "venv/bin/activate"
pip install "../dist/Parsenvy-$VERSION-py3-none-any.whl"
TEST_INT=42 python -c "import parsenvy; assert parsenvy.int('TEST_INT') == 42"
deactivate
cd ..
