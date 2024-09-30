#!/usr/bin/python3
"""import JavaScript object notation for string function"""


import json


def from_json_string(my_str):
    """devuelve un objeto PYTHON en un string JavaScript-on"""
    return json.loads(my_str)
