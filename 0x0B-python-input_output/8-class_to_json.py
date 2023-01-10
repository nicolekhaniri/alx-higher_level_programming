#!/usr/bin/python3
import json

"""returns dictioary description"""


def class_to_json(obj):
    """
    returns dictionary description
    """
    return obj.__dict__

