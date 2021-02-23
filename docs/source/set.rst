###
Set
###

.. autofunction:: parsenvy.parsenvy.set


Usage
-----

.. code-block:: shell

    export ALLOWED_CATEGORIES=python,vim,git

.. code-block:: python

    >>> import parsenvy
    >>> parsenvy.set('ALLOWED_CATEGORIES')
    {'python', 'vim', 'git'}
