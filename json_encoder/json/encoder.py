# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date, time
from uuid import UUID

from six import text_type, PY34

if PY34:
    from functools import singledispatch
else:
    from singledispatch import singledispatch


@singledispatch
def json_encoder(obj):
    raise TypeError(repr(obj) + " is not JSON serializable")


@json_encoder.register(UUID)
def encode_uuid(obj):
    return text_type(obj)


@json_encoder.register(date)
@json_encoder.register(time)
def encode_date_time(obj):
    return obj.isoformat()
