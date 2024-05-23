#!/usr/bin/python3
"Define the Node class"


class Node:
    """
    Class: Node
    Description: Represents a node in a singly linked list.

    Attributes:
        __data (int): The data stored in the node (private attribute).
        __next_node (Node):
        The reference to the next node in the list (private attribute).

    Raises:
        TypeError:
            - If the provided data is not an integer.
            - If the provided next_node is not None or a Node object.
    """

    def __init__(self, data, next_node=None):
        """
        Constructor method for the Node class.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional):
            The reference to the next node. Defaults to None.

        Description:
            Initializes a new node with the given data and next_node reference.
            The data and next_node are validated
            and stored in private attributes.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Property: data
        Description: Retrieves the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for the data property.

        Args:
            value (int): The new data value to be set.

        Description:
            Sets the data stored in the node.
            The new data value is validated to ensure it is an integer.
            If the value is valid,
            it is stored in the private __data attribute.

        Raises:
            TypeError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Property: next_node
        Description: Retrieves the reference to the next node in the list.

        Returns:
            Node: The reference to the next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for the next_node property.

        Args:
            value (Node): The new next_node reference to be set.

        Description:
            Sets the reference to the next node in the list.
            The new next_node value is validated
            to ensure it is None or a Node object.
            If the value is valid,
            it is stored in the private __next_node attribute.

        Raises:
            TypeError: If the provided value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class: SinglyLinkedList
    Description: Represents a singly linked list.

    Attributes:
        _head (Node): The head node of the linked list (private attribute).
    """

    def __init__(self):
        """
        Constructor method for the SinglyLinkedList class.

        Description:
            Initializes an empty singly linked list
            by setting the head to None.
        """
        self._head = None

    def __str__(self):
        """
        String representation method for the SinglyLinkedList class.

        Returns:
            str: A string representation of the linked list,
            with each node's data on a new line.
        """
        result = ""
        current_node = self._head
        while current_node:
            result += str(current_node.data) + "\n"
            current_node = current_node.next_node
        return result.strip()

    def sorted_insert(self, value):
        """
        Method: sorted_insert
        Description: Inserts a new node with
        the given value in the sorted linked list.

        Args:
            value (int): The value to be inserted in the linked list.

        Description:
            Creates a new node with the given value
            and inserts it in the correct position
            to maintain the sorted order of the linked list.
        """
        new_node = Node(value)

        if not self._head or value < self._head.data:
            new_node.next_node = self._head
            self._head = new_node
            return

        current_node = self._head
        while current_node.next_node and value > current_node.next_node.data:
            current_node = current_node.next_node

        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
