import builtins
import os
from typing import Any, Iterable, List, Optional, Set, Tuple, Union


def _env_var(key: builtins.str) -> Optional[builtins.str]:
    return os.environ.get(key, None)


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


def list(
    arg: builtins.str, default: Optional[Iterable[Any]] = None
) -> Optional[List[Any]]:
    var: Optional[builtins.str] = _env_var(arg)

    if var is not None and var != "":
        return var.split(",")
    else:
        if default is not None:
            return builtins.list(default)
        else:
            return None


def tuple(
    arg: builtins.str, default: Optional[Tuple[Any]] = None
) -> Optional[Tuple[Any]]:
    val_list: Optional[List[Any]] = list(arg, default=default)

    if val_list is not None:
        return builtins.tuple(val_list)
    else:
        try:
            return default
        except TypeError:
            return None


def str(
    arg: builtins.str, default: Optional[builtins.str] = None
) -> Optional[builtins.str]:
    var: Optional[builtins.str] = _env_var(arg)

    if var is not None:
        return var
    else:
        return default


def set(arg: builtins.str, default: Optional[Set[Any]] = None) -> Optional[Set[Any]]:
    val_list: Optional[List[Any]] = list(arg, default=default)

    if val_list is not None:
        return builtins.set(val_list)
    else:
        try:
            return default
        except TypeError:
            return None
