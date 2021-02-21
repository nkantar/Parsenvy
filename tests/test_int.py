import pytest

import parsenvy


def test_int_positive(monkeypatch):
    monkeypatch.setenv("foo", "13")
    assert parsenvy.int("foo") == 13


def test_int_negative(monkeypatch):
    monkeypatch.setenv("foo", "-42")
    assert parsenvy.int("foo") == -42


def test_int_zero(monkeypatch):
    monkeypatch.setenv("foo", "0")
    assert parsenvy.int("foo") == 0


def test_int_negative_zero(monkeypatch):
    monkeypatch.setenv("foo", "-0")
    assert parsenvy.int("foo") == 0


def test_int_invalid(monkeypatch):
    monkeypatch.setenv("foo", "bar")
    with pytest.raises(TypeError):
        parsenvy.int("foo")


def test_int_empty(monkeypatch):
    monkeypatch.setenv("foo", "")
    with pytest.raises(TypeError):
        parsenvy.int("foo")
