Parsenvy: Enviously Elegant Environment Variable Parsing
========================================================

**Parsenvy** is an *enviously* elegant environment variable parsing Python library.

Environment variables are strings by default. This can be *rather* inconvenient if you're dealing with a number of them, and in a variety of desired types. Parsenvy aims to provide an intuitive, explicit interface for retrieving these values in appropriate types with *human-friendly* syntax.

Features
--------

- Compatible with both Python 2 and 3
- No dependencies aside from Python's core ``os`` and ``builtins``/``__builtin__`` modules
- Fully tested
- BSD (3-Clause) licensed

TODO
----

- Type-annotated
- Thoroughly documented

Examples
--------

.. code-block:: python

    >>> from parsenvy import parsenvy
    >>> parsenvy.bool('BOOL_ENV_VAR')  # BOOL_ENV_VAR=True
    True
    >>> parsenvy.int('INT_ENV_VAR')  # INT_ENV_VAR=13
    13
    >>> parsenvy.float('FLOAT_ENV_VAR')  # FLOAT_ENV_VAR=555.55
    555.55
    >>> parsenvy.list('LIST_ENV_VAR')  # LIST_ENV_VAR=shiver,me,timbers
    ['shiver', 'me', 'timbers']
    >>> parsenvy.tuple('TUPLE_ENV_VAR')  # TUPLE_ENV_VAR=hello,world
    ('hello', 'world')
    >>> parsenvy.str('STR_ENV_VAR')  # STR_ENV_VAR=meep
    'meep'
    >>> parsenvy.set('SET_ENV_VAR')  # SET_ENV_VAR=wat,wut,wot
    set(['wat', 'wut', 'wot'])
    >>> parsenvy.dict('DICT_ENV_VAR')  # DICT_ENV_VAR=a:1,b:2
    {'a': '1', 'b': '2'}

Install
-------

.. code-block:: shell

    pip install parsenvy

Contributing
------------

Contributions of all sorts are welcome, be they bug reports, patches, or even just feedback. Creating a `new issue <https://github.com/nkantar/Parsenvy/issues/new>`_ or `pull request <https://github.com/nkantar/Parsenvy/compare>`_ is probably the best way to get started.

