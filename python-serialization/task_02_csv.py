#!/usr/bin/python3
"""
Reading data from one format (CSV) and converting it
into another format (JSON) using serialization techniques.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to a JSON file.

    Args:
        csv_filename (str): The name of the CSV file to be converted.

    Returns:
        True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        json_data = json.dumps(data, indent=4)

        with open('data.json', 'w') as json_file:
            json_file.write(json_data)

        return True

    except FileNotFoundError:
        print(f"Error: {csv_filename} not found.")
        return False

    except Exception as e:
        print(f"Error: {e}")
        return False
