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
from io import StringIO
from unittest.mock import patch


class test_base(unittest.TestCase):
    """
    This class will unittest the Base class
    """

    def test_module_docstring(self):
        """
        Test base module documentation exists
        """
        self.assertTrue(len(__import__('models').base.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Test Base class documentation exists
        """
        self.assertTrue(len(__import__('models').base.Base.__doc__) >= 1)

    def test_method_docstring(self):
        """
        Tests Base methods for documentation
        """
        self.assertTrue(len(Base.__doc__) >= 1)
        self.assertTrue(len(Base.__init__.__doc__) >= 1)
        self.assertTrue(len(Base.to_json_string.__doc__) >= 1)
        self.assertTrue(len(Base.save_to_file.__doc__) >= 1)
        self.assertTrue(len(Base.from_json_string.__doc__) >= 1)
        self.assertTrue(len(Base.create.__doc__) >= 1)
        self.assertTrue(len(Base.load_from_file.__doc__) >= 1)

    def test_pep8_compliance(self):
        """
        Tests to ensure models/base and /tests/test_models/test_base.py
        are pep8 compliant
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_base.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_init(self):
        """
        Tests self.id is created correctly
        """
        self.base1 = Base()
        self.base2 = Base(2)
        self.base3 = Base()
        self.base4 = Base()
        self.base5 = Base(-42)
        self.base6 = Base(None)
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 2)
        self.assertEqual(self.base3.id, 2)
        self.assertEqual(self.base4.id, 3)
        self.assertEqual(self.base5.id, -42)
        self.assertEqual(self.base6.id, 4)

if __name__ == '__main__':
    unittest.main()
