#!/usr/bin/python3
"""
This module defines a function that reads and prints a text file (UTF8).
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints its content to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
