#!/usr/bin/python3

import json

"""Function to return json representation of an object"""


def to_json_string(my_obj):
    new = json.dumps(my_obj)
    return new
