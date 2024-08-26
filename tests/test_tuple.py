from _pytest.monkeypatch import MonkeyPatch
import parsenvy


def test_tuple_none() -> None:
    assert parsenvy.tuple("foo") is None


def test_tuple_several(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", "bar,baz,barf")
    assert parsenvy.tuple("foo") == ("bar", "baz", "barf")


def test_tuple_one(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", "bar")
    assert parsenvy.tuple("foo") == ("bar",)


def test_tuple_one_comma(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", ",")
    assert parsenvy.tuple("foo") == ("", "")


def test_tuple_multiple_commas(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", ",,,")
    assert parsenvy.tuple("foo") == ("", "", "", "")


def test_tuple_empty(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("foo", "")
    assert parsenvy.tuple("foo", ("bar",)) == ("bar",)
