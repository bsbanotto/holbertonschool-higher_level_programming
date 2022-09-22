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
    This class will unit test the Base class
    """

    def test_module_docstring(self):
        """
        Test base module documentation exists
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Test Base class documentation exists
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

    def test_init(self):
        """
        Tests that id is created correctly
        """
        base1 = Base()
        base2 = Base(2)
        base3 = Base()
        base4 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 2)
        self.assertEqual(base4.id, 3)

    def test_none_to_json_string(self):
        """
        Tests that None passed to_json_string is functioning correctly
        """
        json_none = Base.to_json_string(None)
        self.assertEqual(json_none, "[]")
        self.assertEqual(type(json_none), str)

    def test_two_object_dict_to_json_string(self):
        """
        Tests that two objects go to json file properly
        """
        Base.base_nb__objects = 0
        o1 = {"id": 420, "width": 7, "height": 14, "x": 0, "y": 2}
        o2 = {"id": 98, "width": 2, "height": 4, "x": 2, "y": 0}
        json_str = Base.to_json_string([o1, o2])
        self.assertEqual(type(json_str), str)
        self.assertEqual(len(json.loads(json_str)), 2)

    def test_two_object_dict_from_json_string(self):
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
