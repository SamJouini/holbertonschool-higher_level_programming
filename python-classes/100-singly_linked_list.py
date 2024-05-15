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


class SinglyLinkedList:
    "Initialize the head of the linked list to None"
    def __init__(self):
        self._head = None

    def __str__(self):
        "String representation of the linked list"
        result = ""
        current_node = self._head
        while current_node:
            "Append the data of each node to the result string"
            result += str(current_node.data) + "\n"
            current_node = current_node.next_node
        return result.strip()

    def sorted_insert(self, value):
        "Create a new node with the given value"
        new_node = Node(value)

        if not self._head or value < self._head.data:
            "If the list is empty or the value is smaller than the head"
            new_node.next_node = self._head
            "Insert the new node at the beginning of the list"
            self._head = new_node
            return

        current_node = self._head
        "Traverse the list to find the correct position for insertion"
        while current_node.next_node and value > current_node.next_node.data:
            current_node = current_node.next_node

        new_node.next_node = current_node.next_node
        "Traverse the list to find the correct position for insertion"
        current_node.next_node = new_node
