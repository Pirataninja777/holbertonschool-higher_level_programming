#!/usr/bin/python3
import csv
import json
"""CSV to JSON"""


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file into JSON format and write it to 'data.json'.

    Parameters:
        csv_filename (str): The name of the input CSV file.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        # Read the CSV file
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        # Write the data to 'data.json'
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
