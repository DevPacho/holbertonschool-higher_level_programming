#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_many_cases(self):
        """
        Test cases for identify a max value in a list with unittest.
        """

        """Positives"""
        l1 = [1, 2, 3, 4]
        self.assertEqual(max_integer(l1), 4)

        """Negatives"""
        l2 = [-5, -9, -10]
        self.assertEqual(max_integer(l2), -5)

        """Floats"""
        l3 = [-4.6, 9.8, 7.9904, 20.9]
        self.assertEqual(max_integer(l3), 20.9)

        """Chars"""
        l4 = ['F', 'f', 'z', 'A']
        self.assertEqual(max_integer(l4), 'z')

        """Floats and ints"""
        l5 = [-50, -50.1, 50, 50.1]
        self.assertEqual(max_integer(l5), 50.1)

        """Lists"""
        l6 = [[2, 3], [2, 3, 4], [2]]
        self.assertEqual(max_integer(l6), [2, 3, 4])

        """String"""
        l7 = "Pacho"
        self.assertEqual(max_integer(l7), "o")

        """Strings"""
        l8 = ["Hi", "Pacho", "Holbie", "C17"]
        self.assertEqual(max_integer(l8), "Pacho")

        """Empty"""
        l9 = []
        self.assertEqual(max_integer(l9), None)

        """Only 1 arg"""
        l10 = [555]
        self.assertEqual(max_integer(l10), 555)

    def test_errors(self):
        """
        Error cases for identify a max value in a list with unittest.
        """

        """0"""
        self.assertRaises(TypeError, max_integer, 0)

        """Char, number"""
        self.assertRaises(TypeError, max_integer, ["P", 1222])

        """Number, list"""
        self.assertRaises(TypeError, max_integer, [2, [2, 1]])

        """No list"""
        l11 = {1, 2, 3, 4, 5, 6}
        self.assertRaises(TypeError)

        """None"""
        l12 = None
        self.assertRaises(TypeError)

        """String"""
        l13 = [333, 9.2, "Pacho", 90]
        self.assertRaises(TypeError)


if __name__ == '__main__':
    unittest.main()
