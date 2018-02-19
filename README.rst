=============================
iconf |latest-version|
=============================

|travis-master| |coverage-master| |quality| |license|

Simple method used to load configuration variables from different sources.

Supports loadings variables from the environment, json file and/or Django settings.

The method will search for the keys in any of the 3 sources and returns the first match.

Search order:

1. Environment
2. JSON - used if path is set and the file exists
3. Django settings - used if Django is installed

This is useful if you need to set configuration variables(SECRET_KEY, DATABASE_NAME, etc...) via environment on a CI server and load the same variables from a json file in a production environment.

Installation
------------

pip install ``iconf`` (or add to your requirements.txt)


Usage
-----


.. code-block:: python

    import iconf

    # find and return keys from environment variables and/or django settings
    # and/or json file
    configs = iconf.get(keys=["KEY1", "KEY2"], path="configs.json")


    # import full json file
    configs = iconf.get(path="configs.json")

    # import from environment and/or django settings
    configs = iconf.get(["KEY1", "KEY2"])



Test
-----

run tests with python -m unittest discover

License
-------

3 Clause BSD.

Bug report and Help
-------------------

For bug reports open a github ticket. Patches gratefully accepted.


.. |travis-master| image:: https://travis-ci.org/adonisnafeh/iconf.svg?branch=master
   :alt: Build Status - master branch
   :target: https://travis-ci.org/adonisnafeh/iconf
.. |coverage-master| image:: https://coveralls.io/repos/github/adonisnafeh/iconf/badge.svg?branch=master
   :alt: Coverage of the code
   :target: https://coveralls.io/github/adonisnafeh/iconf?branch=master
.. |latest-version| image:: https://badge.fury.io/py/iconf.svg
   :alt: Latest version on Pypi
   :target: https://badge.fury.io/py/iconf
.. |quality| image:: https://img.shields.io/codacy/grade/66d6a8fafec04b5dac766547098e13e6.svg?style=flat-square
   :target: https://www.codacy.com/app/adonisnafeh/iconf
.. |license| image:: https://img.shields.io/github/license/adonisnafeh/iconf.svg?style=flat-square
   :alt: License
   :target: https://github.com/adonisnafeh/iconf/blob/master/LICENSE
