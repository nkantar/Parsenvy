import os

# Python 3 isn't just the future - it's the present
try:
    import builtins
# but that doesn't mean we can't be *a little* backwards compatible
except ImportError:
    import __builtin__ as builtins


def _env_var(key):
    try:
        return os.environ[key]
    except KeyError:
        return None


def bool(arg, default=None):
    var = _env_var(arg)
    trues = ['true', '1']
    falses = ['false', '0']

    if var is not None:
        if builtins.str(var).lower() in trues:
            return True
        elif builtins.str(var).lower() in falses:
            return False
        else:
            raise TypeError
    else:
        return default


def int(arg, default=None):
    var = _env_var(arg)

    if var is not None:
        try:
            return builtins.int(var)
        except ValueError:
            raise TypeError
    else:
        return default


def float(arg, default=None):
    var = _env_var(arg)

    if var is not None:
        try:
            return builtins.float(var)
        except ValueError:
            raise TypeError
    else:
        return default


def list(arg, default=None):
    var = _env_var(arg)

    if var is not None and var != '':
        return var.split(',')
    else:
        return default


def tuple(arg, default=None):
    val_list = list(arg, default=default)

    if val_list is not None:
        return builtins.tuple(val_list)
    else:
        return val_list


def str(arg, default=None):
    var = _env_var(arg)

    if var is not None:
        return var
    else:
        return default


def set(arg, default=None):
    val_list = list(arg, default=default)

    if val_list is not None:
        return builtins.set(val_list)
    else:
        return val_list


def dict(arg, default=None):
    var = _env_var(arg)

    if var is not None:
        try:
            pair_list = var.split(',')
            element_lists = [pair.split(':')
                             for pair
                             in pair_list]
            all_elements = []
            [all_elements.extend(pair) for pair in element_lists]
            final_dict = {}
            for index, key in enumerate(all_elements):
                if index % 2 == 0:
                    final_dict.update({key: all_elements[index + 1]})
        except IndexError:
            raise TypeError

        return final_dict
    else:
        return default
