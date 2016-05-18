# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import codecs
import os
import re
import sys

from setuptools import setup, find_packages


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


install_requires = ['six>=1.10.0']
if sys.version_info[0:2] < (3, 4):
    # required for python < 3.4s
    install_requires.append('singledispatch>=3.4.0.3')

setup(
    name='json-encoder',
    version=find_version('json_encoder', '__init__.py'),
    author='NZME',
    author_email='sysadmin@grabone.co.nz',
    long_description=read('README.md'),
    setup_requires=['pytest-runner'],
    install_requires=install_requires,
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
    ],
    extras_require={
        'simplejson': ['simplejson>=3.8.2'],
    },
    tests_require=['pytest']
)
