import os

import pytest

import parsenvy


def test_int_valid():
    os.environ["INT_2"] = "2"
    assert parsenvy.int("INT_2") == 2


def test_int_none():
    assert parsenvy.int("INT_NONE") is None


def test_int_default():
    assert parsenvy.int("INT_NONE", 3) == 3


def test_int_error():
    os.environ["INT_EMPTY"] = ""
    with pytest.raises(TypeError):
        parsenvy.int("INT_EMPTY")

    os.environ["INT_STR"] = "nope"
    with pytest.raises(TypeError):
        parsenvy.int("INT_STR")
