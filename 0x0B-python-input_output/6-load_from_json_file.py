#!/usr/bin/python3

"""Import JSON"""


import json

"""Function that creates an object form json file"""


def load_from_json_file(filename):
    """
    creates object from json file
    Args:
        filename: file
    """
    with open(filename, 'r', encoding="utf-8") as new:
        return json.load(new)
