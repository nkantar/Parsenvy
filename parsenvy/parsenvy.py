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
    env_var: builtins.str,
    default: Optional[builtins.bool] = None,
) -> Optional[builtins.bool]:
    """
    Parse environment variable value into a boolean.

    Args:
        env_var (str): Name of desired environment variable.
        default (bool, optional): Optional fallback value.

    Returns:
        bool (optional): Environment variable typecast into a boolean.

    """
    if env_var.lower() in TRUES:
        return True

    if env_var.lower() in FALSES:
        return False

    raise ValueError(
        f"Invalid boolean value specified: {env_var} "
        "Parsenvy accepts 'true', '1', 'false', and '0' as boolean values."
    )


@default_if_none
def int(
    env_var: builtins.str,
    default: Optional[builtins.int] = None,
) -> Optional[builtins.int]:
    """
    Parse environment variable value into a integer.

    Args:
        env_var (str): Name of desired environment variable.
        default (int, optional): Optional fallback value.

    Returns:
        int (optional): Environment variable typecast into a integer.

    """
    try:
        return builtins.int(env_var)
    except ValueError:
        raise TypeError(
            f"Invalid integer value specified: {env_var} "
            "Parsenvy accepts only valid integers as integer values."
        )


@default_if_none
def float(
    env_var: builtins.str,
    default: Optional[builtins.float] = None,
) -> Optional[builtins.float]:
    """
    Parse environment variable value into a float.

    Args:
        env_var (float): Name of desired environment variable.
        default (float, optional): Optional fallback value.

    Returns:
        float (optional): Environment variable typecast into a float.

    """
    try:
        return builtins.float(env_var)
    except ValueError:
        raise TypeError(
            f"Invalid float value specified: {env_var} "
            "Parsenvy accepts only valid floats and integers as float values"
        )


@default_if_none
def list(
    env_var: builtins.str,
    default: Optional[List[Any]] = None,
) -> Optional[List[Any]]:
    """
    Parse environment variable value into a list.

    Args:
        env_var (str): Name of desired environment variable.
        default (List, optional): Optional fallback value.

    Returns:
        List (optional): Environment variable typecast into a list.
    """
    if env_var == "":
        return default

    return env_var.split(",")


@default_if_none
def tuple(
    env_var: builtins.str,
    default: Optional[Tuple[Any, ...]] = None,
) -> Optional[Tuple[Any, ...]]:
    """
    Parse environment variable value into a tuple.

    Args:
        env_var (str): Name of desired environment variable.
        default (tuple, optional): Optional fallback value.

    Returns:
        tuple (optional): Environment variable typecast into a tuple.

    """
    if env_var == "":
        return default

    return builtins.tuple(env_var.split(","))


@default_if_none
def str(
    env_var: builtins.str,
    default: Optional[builtins.str] = None,
) -> Optional[builtins.str]:
    """
    Parse environment variable value into a str.

    Args:
        env_var (str): Name of desired environment variable.
        default (str, optional): Optional fallback value.

    Returns:
        str (optional): Environment variable typecast into a str.

    """
    if env_var == "":
        return default

    return env_var


@default_if_none
def set(
    env_var: builtins.str,
    default: Optional[Set[Any]] = None,
) -> Optional[Set[Any]]:
    """
    Parse environment variable value into a set.

    Args:
        env_var (str): Name of desired environment variable.
        default (set, optional): Optional fallback value.

    Returns:
        set (optional): Environment variable typecast into a set.

    """
    if env_var is None or env_var == "":
        return default

    return builtins.set(env_var.split(","))
