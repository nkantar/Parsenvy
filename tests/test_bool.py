import os

import pytest

import parsenvy


def test_boolean_true():
    os.environ["BOOL_TRUE"] = "true"
    assert parsenvy.bool("BOOL_TRUE") is True

    os.environ["BOOL_1"] = "1"
    assert parsenvy.bool("BOOL_1") is True


def test_boolean_false():
    os.environ["BOOL_FALSE"] = "false"
    assert parsenvy.bool("BOOL_FALSE") is False

    os.environ["BOOL_0"] = "0"
    assert parsenvy.bool("BOOL_0") is False


def test_boolean_none():
    assert parsenvy.bool("BOOL_NONE") is None


def test_boolean_default():
    assert parsenvy.bool("BOOL_NONE", "foo") == "foo"


def test_boolean_error():
    os.environ["BOOL_EMPTY"] = ""
    with pytest.raises(ValueError):
        parsenvy.bool("BOOL_EMPTY")

    os.environ["BOOL_STR"] = "nope"
    with pytest.raises(ValueError):
        parsenvy.bool("BOOL_STR")
