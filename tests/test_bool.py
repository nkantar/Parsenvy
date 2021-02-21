import pytest

import parsenvy


def test_bool_true_word(monkeypatch):
    """'true'"""
    monkeypatch.setenv("foo", "TrUe")  # capitalization is intentional

    assert parsenvy.bool("foo") is True


def test_bool_true_number(monkeypatch):
    """'1'"""
    monkeypatch.setenv("foo", "1")

    assert parsenvy.bool("foo") is True


def test_bool_false_word(monkeypatch):
    """'false'"""
    monkeypatch.setenv("foo", "fAlSe")  # capitalization is intentional

    assert parsenvy.bool("foo") is False


def test_bool_false_number(monkeypatch):
    """'0'"""
    monkeypatch.setenv("foo", "0")

    assert parsenvy.bool("foo") is False


def test_bool_neither(monkeypatch):
    """'bar'"""
    monkeypatch.setenv("foo", "bar")

    with pytest.raises(ValueError):
        parsenvy.bool("foo")


def test_bool_numbers(monkeypatch):
    """'01'"""
    monkeypatch.setenv("foo", "01")

    with pytest.raises(ValueError):
        parsenvy.bool("foo")


def test_bool_empty(monkeypatch):
    """''"""
    monkeypatch.setenv("foo", "")

    with pytest.raises(ValueError):
        parsenvy.bool("foo")
