#!/usr/bin/python3
"""Unittest for max_integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer"""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_elements(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 0, 5, 3]), 5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.3, 0.7]), 2.3)

    def test_same_numbers(self):
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_sorted_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_reverse_sorted(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1000, 9999, 5000]), 9999)


if __name__ == "__main__":
    unittest.main()
