#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    "Define unittests for max_integer([..])."

    def test_max_integer_empty_list(self):
        "Test an empty list."
        self.assertIsNone(max_integer([]), None)

    def test_max_integer_positive_integers(self):
        "Test a list with positive integers."
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_integer_negative_integers(self):
        "Test a list with negative integers."
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_max_integer_mixed_integers(self):
        "Test a list with mixed positive and negative integers."
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([4, -3, 2, -1]), 4)

    def test_max_integer_one_element(self):
        "Test a list with only one element."
        self.assertEqual(max_integer([5]), 5)

    def test_max_integer_duplicate_values(self):
        "Test a list with duplicate values."
        self.assertEqual(max_integer([1, 2, 3, 3, 2, 1]), 3)

    def test_max_integer_float_values(self):
        "Test a list with float values."
        self.assertEqual(max_integer([1.0, 2.5, 3.0, 4.2]), 4.2)

if __name__ == '__main__':
    unittest.main()
