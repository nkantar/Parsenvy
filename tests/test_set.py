import os

import pytest

import parsenvy


def test_set_valid():
    os.environ["SET_A_B_C"] = "a,b,c"
    assert parsenvy.set("SET_A_B_C") == set(["a", "b", "c"])


def test_set_none():
    assert parsenvy.set("SET_NONE") is None


def test_set_empty():
    os.environ["SET_EMPTY"] = ""
    assert parsenvy.set("SET_EMPTY") is None


def test_set_default():
    assert parsenvy.set("SET_NONE", set([1, 2])) == set([1, 2])
