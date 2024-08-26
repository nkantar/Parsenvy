from _pytest.monkeypatch import MonkeyPatch
import parsenvy


def test_list_none() -> None:
    assert parsenvy.list("foo") is None


def test_list_several(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", "bar,baz,barf")
    assert parsenvy.list("foo") == ["bar", "baz", "barf"]


def test_list_one(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", "bar")
    assert parsenvy.list("foo") == ["bar"]


def test_list_one_comma(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", ",")
    assert parsenvy.list("foo") == ["", ""]


def test_list_multiple_commas(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", ",,,")
    assert parsenvy.list("foo") == ["", "", "", ""]


def test_list_empty(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", "")
    assert parsenvy.list("foo", ["bar"]) == ["bar"]
