# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from decimal import Decimal
from uuid import UUID

from six import binary_type

from json_encoder import json


def test_encode_time():
    result = json.dumps(datetime.time(1, 2, 3))
    assert result == '"01:02:03"'


def test_encode_date():
    result = json.dumps(datetime.date(2016, 2, 29))
    assert result == '"2016-02-29"'


def test_encode_datetime():
    result = json.dumps(datetime.datetime(2016, 2, 29, 1, 2, 3))
    assert result == '"2016-02-29T01:02:03"'


ZERO = datetime.timedelta(0)


class UTC(datetime.tzinfo):
    """
    UTC implementation taken from Python's docs.

    Used only when pytz isn't available.
    """

    def __repr__(self):
        return "<UTC>"

    def utcoffset(self, dt):
        return ZERO

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return ZERO


def test_encode_datetime_with_timezone():
    result = json.dumps(datetime.datetime(2016, 2, 29, 1, 2, 3, tzinfo=UTC()))
    assert result == '"2016-02-29T01:02:03+00:00"'


def test_encode_decimal():
    result = json.dumps(Decimal('0.001'))
    assert result == binary_type('0.001')


def test_encode_uuid():
    uuid = 'e3f143b1-445a-4efe-a38b-1b6c9f920932'
    result = json.dumps(UUID(uuid))
    assert result == '"{}"'.format(uuid)
