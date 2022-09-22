#!/usr/bin/python3
"""
This is the unittest module for the rectangle class
"""


import unittest
import pep8
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_rectangle(unittest.TestCase):
    """
    This class will unittest the Rectangle class
    """
    def test_module_docstring(self):
        """
        Test rectangle module documentation exists
        """
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Test Rectangle class documentation exists
        """
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_method_docstring(self):
        """
        Tests base class methods for documentation
        """
        self.assertTrue(len(Rectangle.__init__.__doc__) >= 1)
        self.assertTrue(len(Rectangle.width.__doc__) >= 1)
        self.assertTrue(len(Rectangle.height.__doc__) >= 1)
        self.assertTrue(len(Rectangle.x.__doc__) >= 1)
        self.assertTrue(len(Rectangle.y.__doc__) >= 1)
        self.assertTrue(len(Rectangle.area.__doc__) >= 1)
        self.assertTrue(len(Rectangle.display.__doc__) >= 1)
        self.assertTrue(len(Rectangle.__str__.__doc__) >= 1)
        self.assertTrue(len(Rectangle.update.__doc__) >= 1)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) >= 1)

if __name__ == '__main__':
    unittest.main()
