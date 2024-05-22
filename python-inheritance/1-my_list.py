#!/usr/bin/python3

class MyList(list):
    """
    A class that inherits from the built-in list class and
    provides a method to print the list in sorted order.
    """

    def print_sorted(self):
        "Prints the list in ascending sorted order."

        "Create a new sorted list from the elements of the current list"
        sorted_list = sorted(self)
        print(sorted_list)

        sorted_list = sorted(self)

        "Print the sorted list"
        print(sorted_list)
