from _pytest.monkeypatch import MonkeyPatch
import pytest

import parsenvy


def test_float_positive_integer(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", str(float(13)))
    assert parsenvy.float("foo") == float(13)


def test_float_positive_decimal(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", str(float(13.42)))
    assert parsenvy.float("foo") == float(13.42)


def test_float_negative_integer(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", str(float(-13)))
    assert parsenvy.float("foo") == float(-13)


def test_float_negative_decimal(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", str(float(-13.42)))
    assert parsenvy.float("foo") == float(-13.42)


def test_float_zero(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", str(float(0)))
    assert parsenvy.float("foo") == float(0)


def test_float_negative_zero(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", str(float(-0)))
    assert parsenvy.float("foo") == float(-0)


def test_float_invalid(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", "bar")
    with pytest.raises(TypeError):
        parsenvy.float("foo")


def test_float_empty(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", "")
    with pytest.raises(TypeError):
        parsenvy.float("foo")
