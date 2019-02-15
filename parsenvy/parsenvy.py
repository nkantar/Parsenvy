import builtins
import os
from typing import Any, Iterable, List, Optional, Union


def _env_var(key: builtins.str) -> Optional[builtins.str]:
    try:
        return os.environ[key]
    except KeyError:
        return None


def bool(arg: builtins.str, default: builtins.bool = None) -> Optional[builtins.bool]:
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


def int(arg: builtins.str, default: builtins.int = None) -> Optional[builtins.int]:
    var: Optional[builtins.str] = _env_var(arg)

    if var is not None:
        try:
            return builtins.int(var)
        except ValueError:
            raise TypeError
    else:
        return default


def float(
    arg: builtins.str, default: builtins.float = None
) -> Optional[builtins.float]:
    var: Optional[builtins.str] = _env_var(arg)

    if var is not None:
        try:
            return builtins.float(var)
        except ValueError:
            raise TypeError
    else:
        return default


def list(arg: builtins.str, default: Iterable[Any] = None) -> Optional[builtins.list]:
    var: Optional[builtins.str] = _env_var(arg)

    if var is not None and var != "":
        return var.split(",")
    else:
        if default is not None:
            return builtins.list(default)
        else:
            return None


def tuple(
    arg: builtins.str, default: builtins.tuple = None
) -> Optional[builtins.tuple]:
    val_list: Optional[List[Any]] = list(arg, default=default)

    if val_list is not None:
        return builtins.tuple(val_list)
    else:
        try:
            return default
        except TypeError:
            return None


def str(arg: builtins.str, default: builtins.str = None) -> Optional[builtins.str]:
    var: Optional[builtins.str] = _env_var(arg)

    if var is not None:
        return var
    else:
        return default


def set(arg: builtins.str, default: builtins.set = None) -> Optional[builtins.set]:
    val_list: Optional[builtins.list] = list(arg, default=default)

    if val_list is not None:
        return builtins.set(val_list)
    else:
        try:
            return default
        except TypeError:
            return None


def dict(arg: builtins.str, default: builtins.dict = None) -> Optional[builtins.dict]:
    var: Optional[builtins.str] = _env_var(arg)

    if var is not None:
        try:
            pair_list: builtins.list = var.split(",")
            element_lists: builtins.list = [pair.split(":") for pair in pair_list]
            all_elements: builtins.list = []
            for pair in element_lists:
                all_elements.extend(pair)
            final_dict: builtins.dict = {}
            for index, key in enumerate(all_elements):
                if index % 2 == 0:
                    final_dict.update({key: all_elements[index + 1]})
        except IndexError:
            raise TypeError

        return final_dict
    else:
        return default
