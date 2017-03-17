import __builtin__
import os
import json


def _env_var(key, default=None):
    try:
        return os.environ[key]
    except KeyError:
        return default


def bool(arg, default=None):
    trues = ['true', '1']
    return arg.lower() in trues


def int(arg, default=None):
    arg = _env_var(arg, default)
    try:
        return __builtin__.int(arg)
    except ValueError:
        return default


def float(arg, default=None):
    return __builtin__.float(arg)


def list(arg, default=None):
    return arg.split(',')


def tuple(arg, default=None):
    pass  # TODO


def str(arg, default=None):
    return arg


def set(arg, default=None):
    pass  # TODO


def dict(arg, default=None):
    if not arg.startswith('{'):
        arg = '{0}{1}{0}'.format('{', arg, '}')
    return dict(json.loads(arg))
