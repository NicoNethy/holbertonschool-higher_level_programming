#!/usr/bin/python3
"""Task 4"""
import json


def from_json_string(my_str):
    """Function that returns an object represented by a JSON string"""
    return json.loads(my_str)
