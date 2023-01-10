#!/usr/bin/python3

"""Import JSON"""


import json

"""Function that creates an object form json file"""


def load_from_json_file(filename):
    """
    creates object from json file
    """
    with open(filename) as new:
        json.load(new)
