########################################################
Parsenvy: Enviously Elegant Environment Variable Parsing
########################################################

**Parsenvy** is an *enviously* elegant environment variable parsing Python library.

.. image:: https://readthedocs.org/projects/parsenvy/badge/?version=latest&style=plastic
        :target: https://parsenvy.readthedocs.io/en/latest
        :alt: main Documentation Status

.. image:: https://github.com/nkantar/Parsenvy/actions/workflows/code-quality-checks.yml/badge.svg?branch=main
        :target: https://github.com/nkantar/Parsenvy/actions/workflows/code-quality-checks.yml
        :alt: Github Actions

.. image:: https://badge.fury.io/py/parsenvy.svg
        :target: https://badge.fury.io/py/parsenvy
        :alt: badgefury svg

.. image:: https://img.shields.io/github/commits-since/nkantar/Parsenvy/3.0.2
        :target: https://github.com/nkantar/Parsenvy/blob/main/CHANGELOG.md#unreleased
        :alt: Unreleased chages

.. image:: https://img.shields.io/github/license/nkantar/Parsenvy
        :target: https://github.com/nkantar/Parsenvy/blob/main/LICENSE
        :alt: License: BSD-3-Clause

Environment variables are strings by default. This can be *rather* inconvenient if you're dealing with a number of them, and in a variety of desired types. Parsenvy aims to provide an intuitive, explicit interface for retrieving these values in appropriate types with *human-friendly* syntax.


Features
--------

- Compatible with Python 3.6+ only (the last Python 2 compatible version was `1.0.2 <https://github.com/nkantar/Parsenvy/releases/tag/1.0.2>`_).
- Fully tested on Linux, macOS, and Windows.
- No dependencies outside of the Python standard library.
- BSD (3-Clause) licensed.
- Utterly awesome.
- Now with `docs <https://parsenvy.readthedocs.io>`_!


Examples
--------

.. code-block:: python

    >>> import parsenvy

    >>> parsenvy.bool('DEBUG_ENABLED')  # DEBUG_ENABLED=True
    True

    >>> parsenvy.int('POSTS_PER_PAGE')  # POSTS_PER_PAGE=13
    13

    >>> parsenvy.float('EXCHANGE_RATE')  # EXCHANGE_RATE=42.911
    42.911

    >>> parsenvy.list('INVALID_USERNAMES')  # INVALID_USERNAMES=admin,superuser,user,webmaster
    ['admin', 'superuser', 'user', 'webmaster']

    >>> parsenvy.tuple('SAMPLE_GREETING')  # SAMPLE_GREETING=Hello,world!
    ('Hello', 'world!')

    >>> parsenvy.set('ALLOWED_CATEGORIES')  # ALLOWED_CATEGORIES=python,vim,git
    {'python', 'vim', 'git'}

    >>> parsenvy.str('DB_PREFIX')  # DB_PREFIX=dj_
    'dj_'


Install
-------

.. code-block:: shell

    pip install parsenvy


Contributing
------------

Contributions are welcome, and more information is available in the `contributing guide <https://parsenvy.readthedocs.io/en/latest/contributing.html>`_.
