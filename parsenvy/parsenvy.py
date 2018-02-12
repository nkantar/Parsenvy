import builtins
import os
from typing import Any, List, Union


def _env_var(key: builtins.str) -> builtins.str:
    try:
        return os.environ[key]
    except KeyError:
        return None


def bool(arg: builtins.str, default: builtins.bool=None) -> builtins.bool:
    var: builtins.str = _env_var(arg)
    trues: List[builtins.str] = ['true', '1']
    falses: List[builtins.str] = ['false', '0']

    if var is not None:
        if builtins.str(var).lower() in trues:
            return True
        elif builtins.str(var).lower() in falses:
            return False
        else:
            raise TypeError
    else:
        return default


def int(arg: builtins.str, default: builtins.int=None) -> builtins.int:
    var: builtins.str = _env_var(arg)

    if var is not None:
        try:
            return builtins.int(var)
        except ValueError:
            raise TypeError
    else:
        return default


def float(arg: builtins.str, default: builtins.float=None) -> builtins.float:
    var: builtins.str = _env_var(arg)

    if var is not None:
        try:
            return builtins.float(var)
        except ValueError:
            raise TypeError
    else:
        return default


def list(arg: builtins.str,
         default: Union[builtins.list,
                        builtins.tuple,
                        builtins.set]=None) -> builtins.list:
    var: builtins.str = _env_var(arg)

    if var is not None and var != '':
        return var.split(',')
    else:
        try:
            return builtins.list(default)
        except TypeError:
            return None


def tuple(arg: builtins.str, default: builtins.tuple=None) -> builtins.tuple:
    val_list: List[Any] = list(arg, default=default)

    if val_list is not None:
        return builtins.tuple(val_list)
    else:
        try:
            return default
        except TypeError:
            return None


def str(arg: builtins.str, default: builtins.str=None) -> builtins.str:
    var: builtins.str = _env_var(arg)

    if var is not None:
        return var
    else:
        return default


def set(arg: builtins.str, default: builtins.set=None) -> builtins.set:
    val_list: builtins.list = list(arg, default=default)

    if val_list is not None:
        return builtins.set(val_list)
    else:
        try:
            return default
        except TypeError:
            return None


def dict(arg: builtins.str, default: builtins.dict=None) -> builtins.dict:
    var: builtins.str = _env_var(arg)

    if var is not None:
        try:
            pair_list: builtins.list = var.split(',')
            element_lists: builtins.list = [pair.split(':')
                                            for pair
                                            in pair_list]
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
