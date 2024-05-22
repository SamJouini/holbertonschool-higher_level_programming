#!/usr/bin/python3
"""
A class that inherits from the built-in list class and
provides a method to print the list in sorted order.
"""


class MyList(list):
    "Prints the list in ascending sorted order."

    def print_sorted(self):

        sorted_list = sorted(self)
        "Create a new sorted list from the elements of the current list"
        print(sorted_list)
        "Print the sorted list"
