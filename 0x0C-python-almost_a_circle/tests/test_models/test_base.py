#!/usr/bin/python3
"""
This module contains unit tests for base.py file
"""


import unittest
import pep8
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class test_base(unittest.TestCase):
    """
    This class will unit test the base class
    """

    def test_module_docstring(self):
        """
        Test base module documentation exists
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Test base class documentation exists
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_method_docstring(self):
        """
        Tests base class methods for documentation
        """
        self.assertTrue(len(Base.__init__.__doc__) >= 1)
        self.assertTrue(len(Base.to_json_string.__doc__) >= 1)
        self.assertTrue(len(Base.save_to_file.__doc__) >= 1)
        self.assertTrue(len(Base.from_json_string.__doc__) >= 1)
        self.assertTrue(len(Base.create.__doc__) >= 1)
        self.assertTrue(len(Base.load_from_file.__doc__) >= 1)