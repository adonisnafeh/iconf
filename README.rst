=============================
appconf |latest-version|
=============================

|travis-master| |coverage-master| |quality| |license|

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


.. |travis-master| image:: https://travis-ci.org/adonisnafeh/appconf.svg?branch=master
   :alt: Build Status - master branch
   :target: https://travis-ci.org/adonisnafeh/appconf
.. |coverage-master| image:: https://coveralls.io/repos/github/adonisnafeh/appconf/badge.svg?branch=master
   :alt: Coverage of the code
   :target: https://coveralls.io/github/adonisnafeh/appconf?branch=master
.. |latest-version| image:: https://badge.fury.io/py/appconf.svg
   :alt: Latest version on Pypi
   :target: https://badge.fury.io/py/appconf
.. |quality| image:: https://img.shields.io/codacy/grade/afacb4b4c83f410fb7cb45458375d1bd.svg?style=flat-square
   :target: https://www.codacy.com/app/adonisnafeh/appconf
.. |license| image:: https://img.shields.io/github/license/adonisnafeh/appconf.svg?style=flat-square
   :alt: License
   :target: https://github.com/adonisnafeh/appconf/blob/master/LICENSE
