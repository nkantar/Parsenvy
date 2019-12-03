import os

import pytest

import parsenvy


def test_list_valid():
    os.environ["LIST_A_B_C"] = "a,b,c"
    assert parsenvy.list("LIST_A_B_C") == ["a", "b", "c"]


def test_list_none():
    assert parsenvy.list("LIST_NONE") is None


def test_list_empty():
    os.environ["LIST_EMPTY"] = ""
    assert parsenvy.list("LIST_EMPTY") is None


def test_list_default():
    assert parsenvy.list("LIST_NONE", [1, 2]) == [1, 2]
