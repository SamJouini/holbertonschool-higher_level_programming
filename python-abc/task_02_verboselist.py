#!/usr/bin/env python3

class VerboseList(list):
    """
    Define a class named VerboseList that
    inherits from the built-in list class
    """
    def append(self, item):
        "Override the append method"
        super().append(item)
        "Call the original append method of the list class to add the item"
        print("Added [{}] to the list.".format(item))
        "Print a message indicating that the item was added"

    def extend(self, item):
        "Override the extend method"
        super().extend(item)
        "Call the original extend method of the list class to extend the list"
        print("Extended the list with [{}] items.".format(item))
        "Print a message indicating the number of items added"

    def remove(self, item):
        "Override the remove method"
        print("Removed [{}] from the list.".format(item))
        "Print a message indicating that the item is being removed"
        super().remove(item)
        """
        Call the original remove method of the list class
        to remove the specified item.
        """

    def pop(self, item=-1):
        "Override the pop method"

        print("Popped [{}] from the list.".format(self[item]))
        "Print a message indicating that the item was popped"
        return super().pop(item)
        "Return the popped item"
