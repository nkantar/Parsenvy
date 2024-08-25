from _pytest.monkeypatch import MonkeyPatch

import parsenvy


def test_str_valid(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", "bar")
    assert parsenvy.str("foo") == "bar"


def test_str_empty(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", "")
    assert parsenvy.str("foo", "bar") == "bar"
