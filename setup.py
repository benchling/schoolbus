#!/usr/bin/env python

from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(name='schoolbus',
	  version='0.2.1',
	  description='schoolbus is a library to guess whether an email is from an academic institution.',
	  long_description=long_description,
	  author='Joshua Ma',
	  author_email='josh@benchling.com',
	  url='https://github.com/benchling/schoolbus',
	  packages=['schoolbus'],
	  install_requires=['publicsuffix >= 1.0.4'])
