import os

import pytest

import parsenvy


def test_str_valid():
    os.environ["STR_HELLO"] = "hello"
    assert parsenvy.str("STR_HELLO") == "hello"


def test_str_empty():
    os.environ["STR_EMPTY"] = ""
    assert parsenvy.str("STR_EMPTY") is None


def test_str_none():
    assert parsenvy.str("STR_NONE") is None


def test_str_default():
    assert parsenvy.str("STR_NONE", "hi") == "hi"
