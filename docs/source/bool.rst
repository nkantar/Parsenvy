#######
Boolean
#######

Boolean is one of the simples type, it's value usually being either **true** or
**false**. However, different languages express and codify it differently

**Python:**

.. code-block:: python

    >>> my_bool = True
    >>> your_bool = False

**C**

.. code-block:: c

    int my_bool = 1
    int your_bool = 0

**JavaScript**

.. code-block:: javascript

    my_bool = true
    your_bool = false

Usage
-----

In the shell:

.. code-block:: bash

    export BOOL_ENV_VAR=true

In python:

.. code-block:: python

    >>> import parsenvy
    >>> parsenvy.bool('BOOL_ENV_VAR')
    True
