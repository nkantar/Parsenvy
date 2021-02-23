#####
Tuple
#####

.. autofunction:: parsenvy.parsenvy.tuple


Usage
-----

.. code-block:: shell

    export ALLOWED_CATEGORIES=python,vim,git

.. code-block:: python

    >>> import parsenvy
    >>> parsenvy.tuple('ALLOWED_CATEGORIES')
    ('Hello', 'world!')
