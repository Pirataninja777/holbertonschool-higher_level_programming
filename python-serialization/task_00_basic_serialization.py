#!/usr/bin/python3
import json
"""Serialize"""


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Parameters:
        data (dict): A Python dictionary containing the data to serialize.
        filename (str): The name of the output JSON file. If the file
        already exists, it will be replaced.
    """
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)


def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file to recreate the
    original Python dictionary.

    Parameters:
        filename (str): The name of the input JSON file.

    Returns:
        dict: A Python dictionary with the deserialized
        JSON data from the file.
    """
    with open(filename, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)
