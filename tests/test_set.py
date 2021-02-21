import parsenvy


def test_set_several(monkeypatch):
    monkeypatch.setenv("foo", "bar,baz,barf")
    assert parsenvy.set("foo") == {"bar", "baz", "barf"}


def test_set_one(monkeypatch):
    monkeypatch.setenv("foo", "bar")
    assert parsenvy.set("foo") == {"bar"}


def test_set_one_comma(monkeypatch):
    monkeypatch.setenv("foo", ",")
    assert parsenvy.set("foo") == {"", ""}


def test_set_multiple_commas(monkeypatch):
    monkeypatch.setenv("foo", ",,,")
    assert parsenvy.set("foo") == {"", "", "", ""}


def test_set_empty(monkeypatch):
    monkeypatch.setenv("foo", "")
    assert parsenvy.set("foo", {"bar"}) == {"bar"}
