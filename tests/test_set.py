from _pytest.monkeypatch import MonkeyPatch
import parsenvy


def test_set_several(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", "bar,baz,barf")
    assert parsenvy.set("foo") == {"bar", "baz", "barf"}


def test_set_one(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", "bar")
    assert parsenvy.set("foo") == {"bar"}


def test_set_one_comma(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", ",")
    assert parsenvy.set("foo") == {"", ""}


def test_set_multiple_commas(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", ",,,")
    assert parsenvy.set("foo") == {"", "", "", ""}


def test_set_empty(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", "")
    assert parsenvy.set("foo", {"bar"}) == {"bar"}
