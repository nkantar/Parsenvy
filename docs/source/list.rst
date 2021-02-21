####
List
####

.. autofunction:: parsenvy.parsenvy.list


Usage
-----

.. code-block:: shell

    export LIST_ENV_VAR=1,2,3

.. code-block:: python

    >>> import parsenvy
    >>> parsenvy.list('LIST_ENV_VAR')
    (1,2,3)
