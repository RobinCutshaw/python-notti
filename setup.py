#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from setuptools import setup, find_packages
import sys
import warnings

dynamic_requires = []

version = 0.1

setup(
    name='notti',
    version=0.1,
    author='Robin Cutshaw',
    author_email='robin@internetlabs.com',
    url='http://github.com/RobinCutshaw/python-notti',
    packages=find_packages(),
    scripts=[],
    description='Python API for controlling Notti lights',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    include_package_data=True,
    zip_safe=False,
)
