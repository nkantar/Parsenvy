import parsenvy


def test_tuple_several(monkeypatch):
    monkeypatch.setenv("foo", "bar,baz,barf")
    assert parsenvy.tuple("foo") == ("bar", "baz", "barf")


def test_tuple_one(monkeypatch):
    monkeypatch.setenv("foo", "bar")
    assert parsenvy.tuple("foo") == ("bar",)


def test_tuple_one_comma(monkeypatch):
    monkeypatch.setenv("foo", ",")
    assert parsenvy.tuple("foo") == ("", "")


def test_tuple_multiple_commas(monkeypatch):
    monkeypatch.setenv("foo", ",,,")
    assert parsenvy.tuple("foo") == ("", "", "", "")


def test_tuple_empty(monkeypatch):
    monkeypatch.setenv("foo", "")
    assert parsenvy.tuple("foo", ("bar",)) == ("bar",)
