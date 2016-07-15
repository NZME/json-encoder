json-encoder
=======================

* json encoder using `singledispatch pattern`_ instead of JSONEncoder class overwrites.

* No more *json.dumps(data, csl=MyJSONEncoder)* everywhere.

* Default serialization for time, date, datetime, UUID and Decimal

* Easy to use, easy to change serialization behaviour

* Not tight to any json implementation *json, simplejson, ujson* ...


.. image:: https://travis-ci.org/NZME/json-encoder.svg?branch=master
    :target: https://travis-ci.org/NZME/json-encoder

Installation
------------

.. code-block:: bash

    $ pip install json-encoder

Quick start
-----------

* Use "json_encoder.json" instead of default python json::

    from json_encoder import json
    
    result = json.dumps(json)

Configuration
-------------

* Chose json implementation::

    # simplejson library is uses as default json implementation 
    # if simplejson isn't installed then python json implementation is used
    # to use other json implementation globally, do:
    
    import ujson as json
    from json_encoder import use_json_library
    
    use_json_library(json)

* To change json implementation for concrete call do::

    from json_encoder import json
    import simplejson
    
    result = json.dumps(json, json=simplejson)

* To make your object JSON serializable do::

    # example how to make python fraction object json serializable
    
    from fractions import Fraction
    from json_encoder.encoder import json_encoder
    
    @json_encoder.register(Fraction)
    def encode_decimal(obj):
        return '{}/{}'.format(obj.numerator, obj.denominator)

* To overwrite JSON serializer behaviour defined in json_encoder.encoder::

    from uuid import UUID
    from six import text_type
    from json_encoder.encoder import json_encoder
    
    @json_encoder.register(UUID)
    def encode_uuid(obj):
        return text_type(obj).replace('-', '')

Requirements
------------

* `singledispatch`_ >= 3.4.0.3 for python 2.x only

.. _singledispatch pattern: https://docs.python.org/3/library/functools.html#functools.singledispatch
.. _singledispatch: https://bitbucket.org/ambv/singledispatch
