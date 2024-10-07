#!/usr/bin/python3
import xml.etree.ElementTree as ET
"""Serializing and Deserializing with XML """


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML format and save it to a file.

    Parameters:
        dictionary (dict): The dictionary to be serialized.
        filename (str): The name of the output XML file.
    """
    # Create the root element
    root = ET.Element("data")

    # Iterate through the dictionary and add child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Convert all values to string

    # Create an ElementTree object and write to file
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    Parameters:
        filename (str): The name of the input XML file.

    Returns:
        dict: The deserialized Python dictionary.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Initialize an empty dictionary
        deserialized_data = {}

        # Iterate through XML elements and reconstruct the dictionary
        for child in root:
            deserialized_data[child.tag] = child.text

        return deserialized_data
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
