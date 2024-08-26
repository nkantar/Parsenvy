"""
Main Parsenvy module.

This module provides all of Parsenvy's functionality by exposing functions the
user is meant to utilize.
"""

import builtins
from os import getenv
from typing import Any, List, Optional, Set, Tuple


TRUES = ["true", "1"]
FALSES = ["false", "0"]


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
    if (value := getenv(env_var)) is None:
        return default

    if value.lower() in TRUES:
        return True

    if value.lower() in FALSES:
        return False

    raise ValueError(
        f"Invalid boolean value specified: {value} "
        "Parsenvy accepts 'true', '1', 'false', and '0' as boolean values."
    )


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
    if (value := getenv(env_var)) is None:
        return default

    try:
        return builtins.int(value)
    except ValueError:
        raise TypeError(
            f"Invalid integer value specified: {value} "
            "Parsenvy accepts only valid integers as integer values."
        )


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
    if (value := getenv(env_var)) is None:
        return default

    try:
        return builtins.float(value)
    except ValueError:
        raise TypeError(
            f"Invalid float value specified: {value} "
            "Parsenvy accepts only valid floats and integers as float values"
        )


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
    if (value := getenv(env_var)) is None:
        return default

    if value == "":
        return default

    return value.split(",")


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
    if (value := getenv(env_var)) is None:
        return default

    if value == "":
        return default

    return builtins.tuple(value.split(","))


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
    if (value := getenv(env_var)) is None:
        return default

    if value is None or value == "":
        return default

    return builtins.set(value.split(","))


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
    if (value := getenv(env_var)) is None:
        return default

    if value == "":
        return default

    return value
