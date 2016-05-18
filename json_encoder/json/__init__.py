# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from decimal import Decimal

from json_encoder import get_json_library
from json_encoder.json.encoder import json_encoder


def dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True,
        allow_nan=True, cls=None, indent=None, separators=None,
        default=None, sort_keys=False, **kw):
    """Serialize ``obj`` as a JSON formatted stream to ``fp`` (a
    ``.write()``-supporting file-like object).

    If ``skipkeys`` is true then ``dict`` keys that are not basic types
    (``str``, ``unicode``, ``int``, ``long``, ``float``, ``bool``, ``None``)
    will be skipped instead of raising a ``TypeError``.

    If ``ensure_ascii`` is true (the default), all non-ASCII characters in the
    output are escaped with ``\\uXXXX`` sequences, and the result is a ``str``
    instance consisting of ASCII characters only.  If ``ensure_ascii`` is
    ``False``, some chunks written to ``fp`` may be ``unicode`` instances.
    This usually happens because the input contains unicode strings or the
    ``encoding`` parameter is used. Unless ``fp.write()`` explicitly
    understands ``unicode`` (as in ``codecs.getwriter``) this is likely to
    cause an error.

    If ``check_circular`` is false, then the circular reference check
    for container types will be skipped and a circular reference will
    result in an ``OverflowError`` (or worse).

    If ``allow_nan`` is false, then it will be a ``ValueError`` to
    serialize out of range ``float`` values (``nan``, ``inf``, ``-inf``)
    in strict compliance of the JSON specification, instead of using the
    JavaScript equivalents (``NaN``, ``Infinity``, ``-Infinity``).

    If ``indent`` is a non-negative integer, then JSON array elements and
    object members will be pretty-printed with that indent level. An indent
    level of 0 will only insert newlines. ``None`` is the most compact
    representation.  Since the default item separator is ``', '``,  the
    output might include trailing whitespace when ``indent`` is specified.
    You can use ``separators=(',', ': ')`` to avoid this.

    If ``separators`` is an ``(item_separator, dict_separator)`` tuple
    then it will be used instead of the default ``(', ', ': ')`` separators.
    ``(',', ':')`` is the most compact JSON representation.

    ``default(obj)`` is a function that should return a serializable version
    of obj or raise TypeError. The default simply raises TypeError.

    If *sort_keys* is ``True`` (default: ``False``), then the output of
    dictionaries will be sorted by key.

    To use a custom ``JSONEncoder`` subclass (e.g. one that overrides the
    ``.default()`` method to serialize additional types), specify it with
    the ``cls`` kwarg; otherwise ``JSONEncoder`` is used.
    """
    json_library = kw.pop('json', None) or get_json_library()
    return json_library.dump(
        obj,
        fp,
        skipkeys=skipkeys,
        ensure_ascii=ensure_ascii,
        check_circular=check_circular,
        allow_nan=allow_nan,
        cls=cls,
        indent=indent,
        separators=separators,
        default=default or json_encoder,  # encode common types
        sort_keys=sort_keys,
        **kw
    )


def dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True,
          allow_nan=True, cls=None, indent=None, separators=None,
          default=None, sort_keys=False, **kw):
    """Serialize ``obj`` to a JSON formatted ``str``.

    If ``skipkeys`` is false then ``dict`` keys that are not basic types
    (``str``, ``unicode``, ``int``, ``long``, ``float``, ``bool``, ``None``)
    will be skipped instead of raising a ``TypeError``.

    If ``ensure_ascii`` is false, all non-ASCII characters are not escaped, and
    the return value may be a ``unicode`` instance. See ``dump`` for details.

    If ``check_circular`` is false, then the circular reference check
    for container types will be skipped and a circular reference will
    result in an ``OverflowError`` (or worse).

    If ``allow_nan`` is false, then it will be a ``ValueError`` to
    serialize out of range ``float`` values (``nan``, ``inf``, ``-inf``) in
    strict compliance of the JSON specification, instead of using the
    JavaScript equivalents (``NaN``, ``Infinity``, ``-Infinity``).

    If ``indent`` is a non-negative integer, then JSON array elements and
    object members will be pretty-printed with that indent level. An indent
    level of 0 will only insert newlines. ``None`` is the most compact
    representation.  Since the default item separator is ``', '``,  the
    output might include trailing whitespace when ``indent`` is specified.
    You can use ``separators=(',', ': ')`` to avoid this.

    If ``separators`` is an ``(item_separator, dict_separator)`` tuple
    then it will be used instead of the default ``(', ', ': ')`` separators.
    ``(',', ':')`` is the most compact JSON representation.

    ``default(obj)`` is a function that should return a serializable version
    of obj or raise TypeError. The default simply raises TypeError.

    If *sort_keys* is ``True`` (default: ``False``), then the output of
    dictionaries will be sorted by key.

    To use a custom ``JSONEncoder`` subclass (e.g. one that overrides the
    ``.default()`` method to serialize additional types), specify it with
    the ``cls`` kwarg; otherwise ``JSONEncoder`` is used.

    """
    json_library = kw.pop('json', None) or get_json_library()
    return json_library.dumps(
        obj,
        skipkeys=skipkeys,
        ensure_ascii=ensure_ascii,
        check_circular=check_circular,
        allow_nan=allow_nan,
        cls=cls,
        indent=indent,
        separators=separators,
        default=default or json_encoder,  # encode common types
        sort_keys=sort_keys,
        **kw
    )


def load(fp, cls=None, object_hook=None, parse_float=None,
         parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
    """Deserialize ``fp`` (a ``.read()``-supporting file-like object containing
    a JSON document) to a Python object.

    If the contents of ``fp`` is encoded with an ASCII based encoding other
    than utf-8 (e.g. latin-1), then an appropriate ``encoding`` name must
    be specified. Encodings that are not ASCII based (such as UCS-2) are
    not allowed, and should be wrapped with
    ``codecs.getreader(fp)(encoding)``, or simply decoded to a ``unicode``
    object and passed to ``loads()``

    ``object_hook`` is an optional function that will be called with the
    result of any object literal decode (a ``dict``). The return value of
    ``object_hook`` will be used instead of the ``dict``. This feature
    can be used to implement custom decoders (e.g. JSON-RPC class hinting).

    ``object_pairs_hook`` is an optional function that will be called with the
    result of any object literal decoded with an ordered list of pairs.  The
    return value of ``object_pairs_hook`` will be used instead of the ``dict``.
    This feature can be used to implement custom decoders that rely on the
    order that the key and value pairs are decoded (for example,
    collections.OrderedDict will remember the order of insertion). If
    ``object_hook`` is also defined, the ``object_pairs_hook`` takes priority.

    To use a custom ``JSONDecoder`` subclass, specify it with the ``cls``
    kwarg; otherwise ``JSONDecoder`` is used.

    """
    json_library = kw.pop('json', None) or get_json_library()
    return json_library.load(
        fp,
        cls=cls,
        object_hook=object_hook,
        parse_float=parse_float or Decimal,  # parse to decimal first
        parse_int=parse_int,
        parse_constant=parse_constant,
        object_pairs_hook=object_pairs_hook,
        **kw
    )


def loads(s, cls=None, object_hook=None, parse_float=None,
          parse_int=None, parse_constant=None, object_pairs_hook=None,
          **kw):
    """Deserialize ``s`` (a ``str`` or ``unicode`` instance containing a JSON
    document) to a Python object.

    If ``s`` is a ``str`` instance and is encoded with an ASCII based encoding
    other than utf-8 (e.g. latin-1) then an appropriate ``encoding`` name
    must be specified. Encodings that are not ASCII based (such as UCS-2)
    are not allowed and should be decoded to ``unicode`` first.

    ``object_hook`` is an optional function that will be called with the
    result of any object literal decode (a ``dict``). The return value of
    ``object_hook`` will be used instead of the ``dict``. This feature
    can be used to implement custom decoders (e.g. JSON-RPC class hinting).

    ``object_pairs_hook`` is an optional function that will be called with the
    result of any object literal decoded with an ordered list of pairs.  The
    return value of ``object_pairs_hook`` will be used instead of the ``dict``.
    This feature can be used to implement custom decoders that rely on the
    order that the key and value pairs are decoded (for example,
    collections.OrderedDict will remember the order of insertion). If
    ``object_hook`` is also defined, the ``object_pairs_hook`` takes priority.

    ``parse_float``, if specified, will be called with the string
    of every JSON float to be decoded. By default this is equivalent to
    float(num_str). This can be used to use another datatype or parser
    for JSON floats (e.g. decimal.Decimal).

    ``parse_int``, if specified, will be called with the string
    of every JSON int to be decoded. By default this is equivalent to
    int(num_str). This can be used to use another datatype or parser
    for JSON integers (e.g. float).

    ``parse_constant``, if specified, will be called with one of the
    following strings: -Infinity, Infinity, NaN, null, true, false.
    This can be used to raise an exception if invalid JSON numbers
    are encountered.

    To use a custom ``JSONDecoder`` subclass, specify it with the ``cls``
    kwarg; otherwise ``JSONDecoder`` is used.

    """
    json_library = kw.pop('json', None) or get_json_library()
    return json_library.loads(
        s,
        cls=cls,
        object_hook=object_hook,
        parse_float=parse_float or Decimal,  # parse to decimal first
        parse_int=parse_int,
        parse_constant=parse_constant,
        object_pairs_hook=object_pairs_hook,
        **kw
    )

