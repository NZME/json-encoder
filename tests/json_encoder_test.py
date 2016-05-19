# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from decimal import Decimal
from uuid import UUID

from json_encoder import json, get_json_library
from json_encoder.json.encoder import json_encoder


def test_used_json_library():
    library = get_json_library()
    try:
        import simplejson as json
    except ImportError:
        import json

    assert library is json


class TestEncoderOverwritable(object):
    original = None

    def setup_method(self, method):
        # store original encoder
        self.original = json_encoder.registry[datetime.time]

    def test_encoder_overwritable(self):
        # define and register my special encoder for instances of time
        @json_encoder.register(datetime.time)
        def _(obj):
            return repr(obj)

        value = datetime.time(1, 2, 3)
        result = json.dumps(value)
        assert result == '"{}"'.format(repr(value))

    def teardown_method(self, method):
        # set back original encoder
        json_encoder.register(datetime.time, self.original)


#  encoder related tests

def test_encode_decimal():
    result = json.dumps(Decimal('0.001'))
    assert result == str('0.001')


def test_encode_uuid():
    uuid = 'e3f143b1-445a-4efe-a38b-1b6c9f920932'
    result = json.dumps(UUID(uuid))
    assert result == '"{}"'.format(uuid)


ZERO = datetime.timedelta(0)


class UTC(datetime.tzinfo):
    """
    UTC implementation taken from Python's docs.
    Used for tests only
    """

    def __repr__(self):
        return "<UTC>"

    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO


def test_encode_time():
    result = json.dumps(datetime.time(1, 2, 3))
    assert result == '"01:02:03"'


def test_encode_time_with_timezone():
    result = json.dumps(datetime.time(
        hour=1, minute=2, second=3, microsecond=4, tzinfo=UTC()
    ))
    assert result == '"01:02:03.000004+00:00"'


def test_encode_date():
    result = json.dumps(datetime.date(2016, 2, 29))
    assert result == '"2016-02-29"'


def test_encode_datetime():
    result = json.dumps(datetime.datetime(2016, 2, 29, 1, 2, 3))
    assert result == '"2016-02-29T01:02:03"'


def test_encode_datetime_with_timezone():
    result = json.dumps(datetime.datetime(2016, 2, 29, 1, 2, 3, tzinfo=UTC()))
    assert result == '"2016-02-29T01:02:03+00:00"'
