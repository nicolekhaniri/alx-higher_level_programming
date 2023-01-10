#!/usr/bin/python3

"""Import JSON"""


import json

"""Function that writes an object to a text file"""


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj: To be written into text file
        filename: Name of the file
    Return:
        The new file
    """
    with open(filename, 'w', encoding="utf-8") as new:
        json.dump(my_obj, new)
