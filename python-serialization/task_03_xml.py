#!/usr/bin/python3
"""
Serialization and deserialization using XML as an alternative format to JSON.
"""
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename for the XML file.

    Returns:
        bool: True if the serialization was successful, False otherwise.
    """

    # Create the root element
    root = ET.Element("data")

    # Iterate through the dictionary items
    for key, value in dictionary.items():
        # Create a child element for the key and set its text to the value
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Create an ElementTree object from the root element
    tree = ET.ElementTree(root)
    # Write the XML tree to the specified file
    tree.write(filename)

    # Return True to indicate successful serialization
    return True

def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.

    Args:
        filename (str): The filename for the XML file.

    Returns:
        dict: The deserialized dictionary.
    """

    # Create an XML tree from the filename
    tree = ET.parse(filename)

    # Get the root element
    root = tree.getroot()
    deserialized_data = {}

    # Iterate through the child elements of the root
    for child in root:
        # Add the child's tag as the key and its text as the value to the dictionary
        deserialized_data[child.tag] = child.text

    # Return the deserialized dictionary
    return deserialized_data
