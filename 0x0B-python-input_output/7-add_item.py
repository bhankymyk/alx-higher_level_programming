#!/usr/bin/python3
"""This module adds all arguments to a Python
 list, and then save them to a file"""
from sys import argv
import os.path
if not os.path.exists("add_item.json"):
    with open("add_item.json", "w", encoding='utf-8') as f:
        f.write("[]")
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
my_list = load_from_json_file("add_item.json")
argc = len(argv)
for i in range(1, argc):
    my_list.append(argv[i])
save_to_json_file(my_list, "add_item.json")
