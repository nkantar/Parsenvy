Parsenvy: Enviously Elegant Environment Variable Parsing
========================================================

**Parsenvy** is an *enviously* elegant environment variable parsing Python library.

Environment variables are strings by default. This can be *rather* inconvenient if you're dealing with a number of them, and in a variety of desired types. Parsenvy aims to provide an intuitive, explicit interface for retrieving these values in appropriate types with *human-friendly* syntax.

.. image:: https://travis-ci.org/nkantar/Parsenvy.svg?branch=master
    :target: https://travis-ci.org/nkantar/Parsenvy
.. image:: https://ci.appveyor.com/api/projects/status/ypywtakntwsf6l00/branch/master?svg=true
    :target: https://ci.appveyor.com/project/nkantar/Parsenvy
.. image:: https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg 
   :target: https://saythanks.io/to/nkantar


Features
--------

- Compatible with Python 3.6+ only (the last Python 2 compatible version was `1.0.2 <https://github.com/nkantar/Parsenvy/releases/tag/1.0.2>`_)
- No dependencies aside from Python's core ``builtins``, ``os``, and ``typing`` modules
- Fully tested
- BSD (3-Clause) licensed


Examples
--------

.. code-block:: python

    >>> import parsenvy
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

Please note that this project is released with a `Contributor Code of Conduct <https://github.com/nkantar/Parsenvy/blob/master/CODE_OF_CONDUCT.md>`_. By participating in this project you agree to abide by its terms.
