#!/usr/bin/env python3
"""
Create a class named CountedIterator that extends
the built-in iterator obtained from the iter function.
"""


class CountedIterator:
    def __init__(self, iterable):
        "Initialize the iterator object using the provided iterable"
        self.iterator = iter(iterable)
        "Initialize the counter to keep track of the number of items iterated"
        self.count = 0

    def __next__(self):
        "Increment the counter before fetching the next item"
        self.count += 1
        """
        Fetch the next item from the original iterator using next()
        If there are no more items, next() will raise a StopIteration exception
        """
        return next(self.iterator)

    def get_count(self):
        "Return the current value of the counter"
        return self.count
