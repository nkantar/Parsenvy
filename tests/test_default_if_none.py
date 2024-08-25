import builtins

from _pytest.monkeypatch import MonkeyPatch

from parsenvy.parsenvy import default_if_none


@default_if_none
def dummy_str(
    env_var: builtins.str,
    default: builtins.str | None = None,
) -> builtins.str | None:
    if env_var == "":
        return default

    return env_var


def test_default_if_none_arg(monkeypatch: MonkeyPatch) -> None:
    """Desired env var is set."""
    monkeypatch.setenv("foo", "bar")
    assert dummy_str("foo") == "bar"


def test_default_if_none_default(monkeypatch: MonkeyPatch) -> None:
    """Desired env var isn't set, default is supplied."""
    monkeypatch.delenv("foo", raising=False)
    assert dummy_str("foo", "bar") == "bar"


def test_default_if_none_neither(monkeypatch: MonkeyPatch) -> None:
    """Desired env var isn't set, default isn't supplied."""
    monkeypatch.delenv("foo", raising=False)
    assert dummy_str("foo") is None


def test_default_if_none_blank(monkeypatch: MonkeyPatch) -> None:
    """Desired env var is set to blank, default is supplied."""
    monkeypatch.setenv("foo", "")
    assert dummy_str("foo", "bar") == "bar"
