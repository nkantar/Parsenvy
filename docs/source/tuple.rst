#####
Tuple
#####

.. autofunction:: parsenvy.parsenvy.tuple


Usage
-----

.. code-block:: shell

    export SAMPLE_GREETING=Hello,world!

.. code-block:: python

    >>> import parsenvy
    >>> parsenvy.tuple('SAMPLE_GREETING')
    ('Hello', 'world!')
