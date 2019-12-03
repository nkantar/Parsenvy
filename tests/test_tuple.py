import os

import pytest

import parsenvy


def test_tuple_valid():
    os.environ["TUPLE_HELLO_WORLD"] = "hello,there,world"
    assert parsenvy.tuple("TUPLE_HELLO_WORLD") == ("hello", "there", "world")


def test_tuple_none():
    assert parsenvy.tuple("TUPLE_NONE") is None


def test_tuple_empty():
    os.environ["TUPLE_EMPTY"] = ""
    assert parsenvy.tuple("TUPLE_EMPTY") is None


def test_tuple_default():
    assert parsenvy.tuple("TUPLE_NONE", ("hello", "there", "world")) == (
        "hello",
        "there",
        "world",
    )
