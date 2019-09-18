import builtins
import os
from typing import Any, List, Optional, Set, Tuple, Union


TRUES = ["true", "1"]
FALSES = ["false", "0"]


def bool(
    arg: builtins.str, default: Optional[builtins.bool] = None
) -> Optional[builtins.bool]:
    value = os.environ.get(arg)

    if value is None:
        return default

    if value.lower() in TRUES:
        return True

    if value.lower() in FALSES:
        return False

    raise ValueError(
        f"Invalid boolean value specified: {value}\n"
        "Parsenvy accepts 'true', '1', 'false', and '0' as boolean values."
    )


def int(
    arg: builtins.str, default: Optional[builtins.int] = None
) -> Optional[builtins.int]:
    value = os.environ.get(arg)

    if value is None:
        return default

    try:
        return builtins.int(value)
    except ValueError:
        raise TypeError(
            f"Invalid integer value specified: {value}\n"
            "Parsenvy accepts only valid integers as integer values."
        )


def float(
    arg: builtins.str, default: Optional[builtins.float] = None
) -> Optional[builtins.float]:
    value = os.environ.get(arg)

    if value is None:
        return default

    try:
        return builtins.float(value)
    except ValueError:
        raise TypeError(
            f"Invalid float value specified: {float}\n"
            "Parsenvy accepts only valid floats and integers as float values"
        )


def list(arg: builtins.str, default: Optional[List[Any]] = None) -> Optional[List[Any]]:
    value = os.environ.get(arg)

    if value is None or value == "":
        return default

    return value.split(",")


def tuple(
    arg: builtins.str, default: Optional[Tuple[Any, ...]] = None
) -> Optional[Tuple[Any, ...]]:
    value = os.environ.get(arg)

    if value is None or value == "":
        return default

    return builtins.tuple(value.split(","))


def str(
    arg: builtins.str, default: Optional[builtins.str] = None
) -> Optional[builtins.str]:
    value = os.environ.get(arg)

    if value is None or value == "":
        return default

    return value


def set(arg: builtins.str, default: Optional[Set[Any]] = None) -> Optional[Set[Any]]:
    value = os.environ.get(arg)

    if value is None or value == "":
        return default

    return builtins.set(value.split(","))
