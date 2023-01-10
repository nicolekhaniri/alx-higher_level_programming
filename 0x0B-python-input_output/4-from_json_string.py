#!/usr/bin/python3

"""Import JSON"""


import json

"""Function that returns a Python object represented by json string"""


def from_json_string(my_str):
    """Returns an object"""
    return json.loads(my_str)
