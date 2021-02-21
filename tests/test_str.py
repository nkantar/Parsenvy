import parsenvy


def test_str_valid(monkeypatch):
    monkeypatch.setenv("foo", "bar")
    assert parsenvy.str("foo") == "bar"


def test_str_empty(monkeypatch):
    monkeypatch.setenv("foo", "")
    assert parsenvy.str("foo", "bar") == "bar"
