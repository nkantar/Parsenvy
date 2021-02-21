import pytest

import parsenvy


def test_float_positive_integer(monkeypatch):
    monkeypatch.setenv("foo", str(float(13)))
    assert parsenvy.float("foo") == float(13)


def test_float_positive_decimal(monkeypatch):
    monkeypatch.setenv("foo", str(float(13.42)))
    assert parsenvy.float("foo") == float(13.42)


def test_float_negative_integer(monkeypatch):
    monkeypatch.setenv("foo", str(float(-13)))
    assert parsenvy.float("foo") == float(-13)


def test_float_negative_decimal(monkeypatch):
    monkeypatch.setenv("foo", str(float(-13.42)))
    assert parsenvy.float("foo") == float(-13.42)


def test_float_zero(monkeypatch):
    monkeypatch.setenv("foo", str(float(0)))
    assert parsenvy.float("foo") == float(0)


def test_float_negative_zero(monkeypatch):
    monkeypatch.setenv("foo", str(float(-0)))
    assert parsenvy.float("foo") == float(-0)


def test_float_invalid(monkeypatch):
    monkeypatch.setenv("foo", "bar")
    with pytest.raises(TypeError):
        parsenvy.float("foo")


def test_float_empty(monkeypatch):
    monkeypatch.setenv("foo", "")
    with pytest.raises(TypeError):
        parsenvy.float("foo")
