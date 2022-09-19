#!/usr/bin/python3
"""Module creates an object from an "JSON" file.
"""
import json


def load_from_json_file(filename):
    """Function to load an object from filename
    """
    with open(filename, 'r') as file_content:
        return(json.load(file_content))
