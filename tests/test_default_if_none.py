import pytest

from parsenvy.parsenvy import default_if_none


@pytest.fixture(scope="function")
def func():
    """Dummy function fixture."""

    def inner_func(arg, default=None):
        """Dummy function."""
        return arg

    return inner_func


def test_default_if_none_arg(func, monkeypatch):
    """Desired env var is set."""
    monkeypatch.setenv("foo", "bar")
    decorated_func = default_if_none(func)
    assert decorated_func("foo") == "bar"


def test_default_if_none_default(func, monkeypatch):
    """Desired env var isn't set, default is supplied."""
    monkeypatch.delenv("foo", raising=False)
    decorated_func = default_if_none(func)
    assert decorated_func("foo", "bar") == "bar"


def test_default_if_none_neither(func, monkeypatch):
    """Desired env var isn't set, default isn't supplied."""
    monkeypatch.delenv("foo", raising=False)
    decorated_func = default_if_none(func)
    assert decorated_func("foo") is None
