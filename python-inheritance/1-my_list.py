#!/usr/bin/python3

class MyList(list):
    """
    A class that inherits from the built-in list class and
    provides a method to print the list in sorted order.
    """

    def print_sorted(self):
        "Prints the list in ascending sorted order."

        sorted_list = sorted(self)
        print(sorted_list)
