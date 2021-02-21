#######
Boolean
#######


.. autofunction:: parsenvy.parsenvy.bool


Usage
-----

.. code-block:: shell

    export BOOL_ENV_VAR=true

.. code-block:: python

    >>> import parsenvy
    >>> parsenvy.bool('BOOL_ENV_VAR')
    True
