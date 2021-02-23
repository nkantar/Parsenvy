####
List
####

.. autofunction:: parsenvy.parsenvy.list


Usage
-----

.. code-block:: shell

    export INVALID_USERNAMES=admin,superuser,user,webmaster

.. code-block:: python

    >>> import parsenvy
    >>> parsenvy.list('INVALID_USERNAMES')
    ['admin', 'superuser', 'user', 'webmaster']
