#!/usr/bin/python3
import json

"""Function that returns a Python object represented by json string"""

def from_json_string(my_str):
    new = json.loads(my_str)
    return new
