#!/usr/bin/python3
import sys
from 5-save_to_json_file import *
from 6-load_from_json_file import *

filename = "add_item.json"
try:
    existing_file = load_from_json_file(filename)
except FileNotFoundError:
    existing_file = []
new_file = existing_file + argv[:1]
save_to_json_file(new_file, filename)
