# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import codecs
import os
import re

import pkg_resources
from setuptools import setup, find_packages


def version_number(package, deep=3):
    version = pkg_resources.get_distribution(package).version.split('.')[:deep]
    version.extend([0] * (deep - len(version)))
    return int(''.join(version))


pip_version = version_number('pip')
assert pip_version >= 812, "installation require pip>=8.1.2 to solve this issue run 'pip install --upgrade pip'"

setuptools_version = version_number('setuptools')
assert setuptools_version >= 2022, "installation require setuptools>=20.2.2 to solve this issue run 'pip install --upgrade setuptools'"


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


setup(
    name='json-encoder',
    version=find_version('json_encoder', '__init__.py'),
    author='NZME',
    author_email='sysadmin@grabone.co.nz',
    long_description=read('README.md'),
    install_requires=[
        'six>=1.10.0',
        "singledispatch>=3.4.0.3; python_version < '3.4'",
    ],
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
    }
)
