import builtins
from functools import wraps
import os
from typing import Any, Callable, List, Optional, Set, Tuple, Union


TRUES = ["true", "1"]
FALSES = ["false", "0"]


def default_if_none(func: Callable[[builtins.str, Any], Any]) -> Optional[Any]:
    @wraps(func)
    def wrapper_default_if_none(*args, **kwargs):
        if os.environ.get(args[0]) is None:
            try:
                return args[1]
            except IndexError:
                return None

        return func(*args, **kwargs)

    return wrapper_default_if_none


@default_if_none
def bool(
    arg: builtins.str, default: Optional[builtins.bool] = None
) -> Optional[builtins.bool]:
    value = os.environ.get(arg)

    if value.lower() in TRUES:  # type: ignore
        return True

    if value.lower() in FALSES:  # type: ignore
        return False

    raise ValueError(
        f"Invalid boolean value specified: {value}\n"
        "Parsenvy accepts 'true', '1', 'false', and '0' as boolean values."
    )


@default_if_none
def int(
    arg: builtins.str, default: Optional[builtins.int] = None
) -> Optional[builtins.int]:
    value = os.environ.get(arg)

    try:
        return builtins.int(value)  # type: ignore
    except ValueError:
        raise TypeError(
            f"Invalid integer value specified: {value}\n"
            "Parsenvy accepts only valid integers as integer values."
        )


@default_if_none
def float(
    arg: builtins.str, default: Optional[builtins.float] = None
) -> Optional[builtins.float]:
    value = os.environ.get(arg)

    try:
        return builtins.float(value)  # type: ignore
    except ValueError:
        raise TypeError(
            f"Invalid float value specified: {float}\n"
            "Parsenvy accepts only valid floats and integers as float values"
        )


@default_if_none
def list(arg: builtins.str, default: Optional[List[Any]] = None) -> Optional[List[Any]]:
    value = os.environ.get(arg)

    if value == "":
        return default

    return value.split(",")  # type: ignore


@default_if_none
def tuple(
    arg: builtins.str, default: Optional[Tuple[Any, ...]] = None
) -> Optional[Tuple[Any, ...]]:
    value = os.environ.get(arg)

    if value == "":
        return default

    return builtins.tuple(value.split(","))  # type: ignore


@default_if_none
def str(
    arg: builtins.str, default: Optional[builtins.str] = None
) -> Optional[builtins.str]:
    value = os.environ.get(arg)

    if value == "":
        return default

    return value


@default_if_none
def set(arg: builtins.str, default: Optional[Set[Any]] = None) -> Optional[Set[Any]]:
    value = os.environ.get(arg)

    if value is None or value == "":
        return default

    return builtins.set(value.split(","))
