# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__version__ = '0.4.1'

_json_library = None


def use_json_library(json):
    global _json_library
    _json_library = json


def get_json_library():
    global _json_library
    return _json_library


try:
    use_json_library(__import__('simplejson'))
except ImportError:
    use_json_library(__import__('json'))
