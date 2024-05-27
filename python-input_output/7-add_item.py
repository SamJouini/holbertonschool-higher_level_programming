#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then save them to a file.
"""

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    existing_items = load_from_json_file(filename)
except FileNotFoundError:
    existing_items = []

new_items = sys.argv[1:]
all_items = existing_items + new_items

save_to_json_file(all_items, filename)
