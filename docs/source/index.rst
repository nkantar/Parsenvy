####################################
Welcome to Parsenvy's documentation!
####################################

Enviously Elegant Environment Variable Parsing.

Environment variables are strings by default. This can be rather inconvenient
if you're dealing with a number of them, and in a variety of desired types.
Parsenvy aims to provide an intuitive, explicit interface for retrieving these
values in appropriate types with human-friendly syntax.

**Example:**

In the shell:

.. code-block:: bash

    export BOOL_ENV_VAR=true

In python:

.. code-block:: python

    >>> import parsenvy
    >>> parsenvy.bool('BOOL_ENV_VAR')
    True


.. toctree::
   :maxdepth: 1
   :caption: Contents:

   bool
   dict
   float
   int
   list
   set
   str
   tuple


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
