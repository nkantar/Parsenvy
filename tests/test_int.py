from _pytest.monkeypatch import MonkeyPatch
import pytest

import parsenvy


def test_int_none() -> None:
    assert parsenvy.int("foo") is None


def test_int_positive(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", "13")
    assert parsenvy.int("foo") == 13


def test_int_negative(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", "-42")
    assert parsenvy.int("foo") == -42


def test_int_zero(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", "0")
    assert parsenvy.int("foo") == 0


def test_int_negative_zero(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", "-0")
    assert parsenvy.int("foo") == 0


def test_int_invalid(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", "bar")
    with pytest.raises(TypeError):
        parsenvy.int("foo")


def test_int_empty(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", "")
    with pytest.raises(TypeError):
        parsenvy.int("foo")
