import os

import pytest

import parsenvy


def test_float_valid():
    os.environ["FLOAT_1_23"] = "1.23"
    assert parsenvy.float("FLOAT_1_23") == 1.23


def test_float_none():
    assert parsenvy.float("FLOAT_NONE") is None


def test_float_default():
    assert parsenvy.float("FLOAT_NONE", 1.23) == 1.23


def test_float_error():
    os.environ["FLOAT_EMPTY"] = ""
    with pytest.raises(TypeError):
        parsenvy.float("FLOAT_EMPTY")

    os.environ["FLOAT_STR"] = "nope"
    with pytest.raises(TypeError):
        parsenvy.float("FLOAT_STR")
