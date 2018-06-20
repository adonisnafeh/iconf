#!/usr/bin/env python
from __future__ import absolute_import, division, print_function, \
    unicode_literals
from setuptools import setup

setup(name='iconf',
      version='0.0.2',
      description='Simple method used to load configuration variables '
                  'from different sources.',
      author='Adonis Nafeh',
      author_email='adonisnafeh@gmail.com',
      url='https://github.com/adonisnafeh/iconf',
      download_url='https://github.com/adonisnafeh/iconf/tarball/master',
      keywords='json, django settings, configuration, loader, '
               'environment variables, ci server, continuous integration, '
               'circle ci, travis ci, jenkins',
      packages=['iconf', ],
      include_package_data=True,
      zip_safe=False,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      exclude=[
          'docs',
          '*tests',
          '*tests.*',
      ],
      long_description=open('README.rst').read())
