"""
Main Parsenvy module.

This module provides all of Parsenvy's functionality by exposing functions the
user is meant to utilize.
"""


import builtins
from functools import wraps
import os
from typing import Any, Callable, List, Optional, Set, Tuple


TRUES = ["true", "1"]
FALSES = ["false", "0"]


def default_if_none(func: Callable[[builtins.str, Any], Any]) -> Optional[Any]:
    """
    Decorate function to return default if desired env var isn't defined.

    Args:
        func (callable): Function to return if desired env var is defined.

    Returns:
        callable (optional): Decorated function.

    """

    @wraps(func)
    def wrapper_default_if_none(*args: Any) -> Optional[Any]:
        value = os.environ.get(args[0])

        # if env var isn't defined, try returning default, or fall back to None
        if value is None:
            try:
                return args[1]
            except IndexError:
                return None

        # grab default if present to pass to function
        try:
            default = args[1]
        except IndexError:
            default = None

        return func(value, default)

    return wrapper_default_if_none


@default_if_none
def bool(
    value: builtins.str,
    default: Optional[builtins.bool] = None,
) -> Optional[builtins.bool]:
    if value.lower() in TRUES:
        return True

    if value.lower() in FALSES:
        return False

    raise ValueError(
        f"Invalid boolean value specified: {value} "
        "Parsenvy accepts 'true', '1', 'false', and '0' as boolean values."
    )


@default_if_none
def int(
    value: builtins.str,
    default: Optional[builtins.int] = None,
) -> Optional[builtins.int]:
    try:
        return builtins.int(value)
    except ValueError:
        raise TypeError(
            f"Invalid integer value specified: {value} "
            "Parsenvy accepts only valid integers as integer values."
        )


@default_if_none
def float(
    value: builtins.str,
    default: Optional[builtins.float] = None,
) -> Optional[builtins.float]:
    try:
        return builtins.float(value)
    except ValueError:
        raise TypeError(
            f"Invalid float value specified: {float} "
            "Parsenvy accepts only valid floats and integers as float values"
        )


@default_if_none
def list(
    value: builtins.str,
    default: Optional[List[Any]] = None,
) -> Optional[List[Any]]:
    if value == "":
        return default

    return value.split(",")


@default_if_none
def tuple(
    value: builtins.str,
    default: Optional[Tuple[Any, ...]] = None,
) -> Optional[Tuple[Any, ...]]:
    if value == "":
        return default

    return builtins.tuple(value.split(","))


@default_if_none
def str(
    value: builtins.str,
    default: Optional[builtins.str] = None,
) -> Optional[builtins.str]:
    if value == "":
        return default

    return value


@default_if_none
def set(
    value: builtins.str,
    default: Optional[Set[Any]] = None,
) -> Optional[Set[Any]]:
    if value is None or value == "":
        return default

    return builtins.set(value.split(","))
