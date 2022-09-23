#!/usr/bin/python3
"""
This is the unittest module for the square class
"""


import unittest
import pep8
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from unittest.mock import patch


class test_square(unittest.TestCase):
    """
    This class will unittest the Rectangle class
    """
    def test_module_docstring(self):
        """
        Test rectangle module documentation exists
        """
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Test Rectangle class documentation exists
        """
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_method_docstring(self):
        """
        Tests base class methods for documentation
        """
        self.assertTrue(len(Square.__init__.__doc__) >= 1)
        self.assertTrue(len(Square.size.__doc__) >= 1)
        self.assertTrue(len(Square.__str__.__doc__) >= 1)
        self.assertTrue(len(Square.update.__doc__) >= 1)
        self.assertTrue(len(Square.to_dictionary.__doc__) >= 1)
if __name__ == '__main__':
    unittest.main()
