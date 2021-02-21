import parsenvy


def test_list_several(monkeypatch):
    """'bar,baz,barf'"""
    monkeypatch.setenv("foo", "bar,baz,barf")

    assert parsenvy.list("foo") == ["bar", "baz", "barf"]


def test_list_one(monkeypatch):
    """'bar'"""
    monkeypatch.setenv("foo", "bar")

    assert parsenvy.list("foo") == ["bar"]


def test_list_one_comma(monkeypatch):
    """','"""
    monkeypatch.setenv("foo", ",")

    assert parsenvy.list("foo") == ["", ""]


def test_list_multiple_commas(monkeypatch):
    """',,,'"""
    monkeypatch.setenv("foo", ",,,")

    assert parsenvy.list("foo") == ["", "", "", ""]


def test_list_empty(monkeypatch):
    """''"""
    monkeypatch.setenv("foo", "")

    assert parsenvy.list("foo", ["bar"]) == ["bar"]
