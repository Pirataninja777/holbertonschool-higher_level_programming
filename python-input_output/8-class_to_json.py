#!/usr/bin/python3
"""This dictionary will only include serializable types like strings,
integers, booleans, lists, and dictionaries, as required."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structures
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary with the object's attributes.
    """
    return obj.__dict__
