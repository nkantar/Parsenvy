import builtins
import os
from typing import Any, Iterable, List, Optional, Set, Tuple, Union


def _env_var(key: builtins.str) -> Optional[builtins.str]:
    return os.environ.get(key, None)


def bool(
    arg: builtins.str, default: Optional[builtins.bool] = None
) -> Optional[builtins.bool]:
    var: Optional[builtins.str] = _env_var(arg)
    trues: List[builtins.str] = ["true", "1"]
    falses: List[builtins.str] = ["false", "0"]

    if var is not None:
        if builtins.str(var).lower() in trues:
            return True
        elif builtins.str(var).lower() in falses:
            return False
        else:
            raise TypeError
    else:
        return default


def int(
    arg: builtins.str, default: Optional[builtins.int] = None
) -> Optional[builtins.int]:
    var: Optional[builtins.str] = _env_var(arg)

    if var is not None:
        try:
            return builtins.int(var)
        except ValueError:
            raise TypeError
    else:
        return default


def float(
    arg: builtins.str, default: Optional[builtins.float] = None
) -> Optional[builtins.float]:
    var: Optional[builtins.str] = _env_var(arg)

    if var is not None:
        try:
            return builtins.float(var)
        except ValueError:
            raise TypeError
    else:
        return default


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
