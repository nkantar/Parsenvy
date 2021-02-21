import pytest

import parsenvy


def test_bool_true_word(monkeypatch):
    monkeypatch.setenv("foo", "TrUe")  # capitalization is intentional
    assert parsenvy.bool("foo") is True


def test_bool_true_number(monkeypatch):
    monkeypatch.setenv("foo", "1")
    assert parsenvy.bool("foo") is True


def test_bool_false_word(monkeypatch):
    monkeypatch.setenv("foo", "fAlSe")  # capitalization is intentional
    assert parsenvy.bool("foo") is False


def test_bool_false_number(monkeypatch):
    monkeypatch.setenv("foo", "0")
    assert parsenvy.bool("foo") is False


def test_bool_neither(monkeypatch):
    monkeypatch.setenv("foo", "bar")
    with pytest.raises(ValueError):
        parsenvy.bool("foo")


def test_bool_numbers(monkeypatch):
    monkeypatch.setenv("foo", "01")
    with pytest.raises(ValueError):
        parsenvy.bool("foo")


def test_bool_empty(monkeypatch):
    monkeypatch.setenv("foo", "")
    with pytest.raises(ValueError):
        parsenvy.bool("foo")
