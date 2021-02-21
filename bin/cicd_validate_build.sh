#!/usr/bin/env sh

STAGE=$1
VERSION=$2
INDEX_URL=""

if [ "$STAGE" = "test" ]; then 
    INDEX_URL="--index-url https://test.pypi.org/simple/"
fi;

mkdir "validate_$STAGE"
cd "validate_$STAGE"
python -m venv "venv_$STAGE"
source "venv_$STAGE/bin/activate"
pip install $INDEX_URL parsenvy=="$VERSION"
TEST_INT=42 python -c "import parsenvy; assert parsenvy.int('TEST_INT') == '42'"
deactivate
cd ..
