#!/usr/bin/python3
"""Import JSON"""


import sys
from 5-save_to_json_file import *
from 6-load_from_json_file import *

if __name__ = "__main__":
    filename = "add_item.json"
    try:
        existing_file = load_from_json_file(filename)
    except FileNotFoundError:
        existing_file = []
    save_to_json_file(existing_file +argv[:1], filename)
