#####
Tuple
#####

.. autofunction:: parsenvy.parsenvy.tuple


Usage
-----

.. code-block:: shell

    export TUPLE_ENV_VAR=1,2,3

.. code-block:: python

    >>> import parsenvy
    >>> parsenvy.tuple('TUPLE_ENV_VAR')
    (1,2,3)
