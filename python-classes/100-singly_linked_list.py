#!/usr/bin/python3
"Define the Node class"


class Node:
    "Constructor method to initialize a new node"
    def __init__(self, data, next_node=None):
        "Set the data attribute of the node"
        self.data = data
        "Set the next_node attribute of the node"
        self.next_node = next_node

    @property   # Property getter for the data attribute
    def data(self):
        return self.__data

    @data.setter   # Property setter for the data attribute
    def data(self, value):
        "Check if the value is an integer"
        if not isinstance(value, int):
            "Raise a TypeError if the value is not an integer"
            raise TypeError("data must be an integer")
        self.__data = value

    @property   # Property getter for the next_node attribute
    def next_node(self):
        return self.__next_node

    @next_node.setter   # Property setter for the next_node attribute
    def next_node(self, value):
        "Property setter for the next_node attribute"
        if value is not None and not isinstance(value, Node):
            "Raise a TypeError if the value is not None or a Node object"
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
