=============================
appconf
=============================


Simple method used to load configuration variables from different sources.

Supports loadings variables from the environment, json file and/or Django settings.

The method will search for the keys in any of the 3 sources and returns the first match.

Search order:

1. Environment
2. JSON - used if path is set
3. Django settings - used if Django is installed

This is useful if you need to set configuration variables(SECRET_KEY, DATABASE_NAME, etc...) via environment on a CI server and load the same variables from a json file in a production environment.

Installation
------------

pip install ``appconf`` (or add to your requirements.txt)


Usage
-----


.. code-block:: python

    import appconf

    # find and return keys from environment variables and/or django settings
    # and/or json file
    configs = appconf.get(keys=["KEY1", "KEY2"], path="configs.json")


    # import full json file
    configs = appconf.get(path="configs.json")

    # import from environment and/or django settings
    configs = appconf.get(["KEY1", "KEY2"])



Test
-----

run tests with python -m unittest discover

License
-------

3 Clause BSD.

Bug report and Help
-------------------

For bug reports open a github ticket. Patches gratefully accepted.

