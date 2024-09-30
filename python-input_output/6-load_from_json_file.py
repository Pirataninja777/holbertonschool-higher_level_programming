#!/usr/bin/python3
"""function that creates an object from JSON file"""
import json


def load_from_json_file(filename):
    """crea un obj desde un file JavaScript ObJ notation"""
    with open(filename, 'r') as f:
        return json.load(f)
