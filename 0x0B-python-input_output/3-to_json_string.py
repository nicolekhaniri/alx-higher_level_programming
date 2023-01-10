#!/usr/bin/python3

import json

"""Function to return json representation of an object"""


def to_json_string(my_obj):
    """
    Args:
        my_obj: Python object
    Returns:
        json representation of object
    """
    return json.dumps(my_obj)
