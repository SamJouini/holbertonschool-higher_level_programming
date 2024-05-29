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

    for key, value in dictionary.items():
        # Create a child element for the key
        key_element = ET.Element("key")
        key_element.text = str(key)

        # Create a child element for the value
        value_element = ET.Element("value")
        value_element.text = str(value)

        # Add the key and value elements as children of the root
        root.append(value_element)
        root.append(key_element)

    # Create an XML file with the filename
    with open(filename, "w") as file:
        file.write(f"<data>\n\n")

        # Iterate through the root elements
        for element in root:
            # Write the element to the file
            file.write(f"{element.tag} {element.text}\n")

        file.write(f"</data>")

    return True


def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.

    Args:
        filename (str): The filename for the XML file.

    Returns:
        dict: The deserialized dictionary.
    """
    dictionary = {}

    # Create an XML tree from the filename
    tree = ET.parse(filename)

    # Get the root element
    root = tree.getroot()

    for element in root:
        # Get the key and value from the element
        key = element.get("key")
        value = element.get("value")

        # Add the key and value to the dictionary
        dictionary[key] = value

    return dictionary
