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
        self.base1 = Base(0)
        self.base2 = Base(1)
        self.base3 = Base(2)
        self.base4 = Base(3)
        self.base5 = Base(-42)
        self.assertEqual(self.base1.id, 0)
        self.assertEqual(self.base2.id, 1)
        self.assertEqual(self.base3.id, 2)
        self.assertEqual(self.base4.id, 3)
        self.assertEqual(self.base5.id, -42)

    def test_bad_init(self):
        """
        Tests for bad values passed to Base.id
        """
        with self.assertRaises(TypeError):
            Base(1, 12)

    def test_none_to_json_string(self):
        """
        Tests that None passed to_json_string is functioning correctly
        """
        json_none = Base.to_json_string(None)
        self.assertEqual(json_none, "[]")
        self.assertEqual(type(json_none), str)

        json_empty = Base.to_json_string([])
        self.assertEqual(json_empty, "[]")
        self.assertEqual(type(json_empty), str)

    def test_to_json_string(self):
        """
        Tests that two objects go to json file properly
        """
        Base.base_nb__objects = 0
        o1 = {"id": 420, "width": 7, "height": 14, "x": 0, "y": 2}
        o2 = {"id": 98, "width": 2, "height": 4, "x": 2, "y": 0}
        json_str = Base.to_json_string([o1, o2])
        self.assertEqual(type(json_str), str)
        self.assertEqual(len(json.loads(json_str)), 2)

    def test_save_to_file_rectangle(self):
        """
        Tests proper use of save_to_file method
        """
        r1 = Rectangle(10, 7, 2, 8, 0)
        Rectangle.save_to_file([r1])
        read_string = '[{"id": 0, "width": 10, "height": 7, "x": 2, "y": 8}]'

        with open("Rectangle.json", "r") as file:
            test_String = file.read()
        self.assertEqual(test_String, read_string)

    def test_save_to_file_square(self):
        """
        Tests improper use of save_to_file method
        """
        pass

    def test_from_json_string(self):
        """
        Tests that a two item list functions properly
        """
        list_input = [
            {"id": 420, "width": 7, "height": 14, "x": 0, "y": 2},
            {"id": 98, "width": 2, "height": 4, "x": 2, "y": 0}
        ]
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertTrue(type(list_output) is list)
        self.assertTrue(type(json_list_input) is str)
        self.assertEqual(len(list_output), 2)

    def test_None_from_json_string(self):
        """
        Tests from_json_string method on None
        """
        list_input = None
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertTrue(type(list_output) is list)
        self.assertTrue(type(json_list_input) is str)
        self.assertEqual(len(list_output), 0)

    def test_empty_from_json_string(self):
        """
        Tests from_json_string method on empty string
        """
        list_input = []
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        self.assertTrue(type(list_output) is list)
        self.assertTrue(type(json_list_input) is str)
        self.assertEqual(len(list_output), 0)

    def test_create_rectangle(self):
        """
        Tests create method for rectangle
        """
        r1 = Rectangle(3, 5, 1, 0, 0)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)

    def test_create_square(self):
        """
        Tests create method for square
        """
        s1 = Square(3, 5, 1, 0)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertNotEqual(s1, s2)

    def test_load_from_file_rectangle(self):
        """
        Tests proper use of load_from_file method
        """
        pass

    def test_load_from_file_square(self):
        """
        Tests improper use of load_from_file method
        """
        pass

if __name__ == '__main__':
    unittest.main()
