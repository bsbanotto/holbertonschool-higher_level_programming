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
from io import StringIO
from unittest.mock import patch


class test_rectangle(unittest.TestCase):
    """
    This class will unittest the Rectangle class
    """

    def test_module_docstring(self):
        """
        Test rectangle module documentation exists
        """
        self.assertTrue(len(__import__('models').rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Test Rectangle class documentation exists
        """
        self.assertTrue(len(__import__('models').rectangle.Rectangle.
                        __doc__) >= 1)

    def test_method_docstring(self):
        """
        Tests Rectangle methods for documentation
        """
        self.assertTrue(len(Rectangle.__doc__) >= 1)
        self.assertTrue(len(Rectangle.__init__.__doc__) >= 1)
        self.assertTrue(len(Rectangle.area.__doc__) >= 1)
        self.assertTrue(len(Rectangle.display.__doc__) >= 1)
        self.assertTrue(len(Rectangle.__str__.__doc__) >= 1)
        self.assertTrue(len(Rectangle.update.__doc__) >= 1)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) >= 1)

    def test_pep8_compliance(self):
        """
        Tests to ensure models/rectangle and
        /tests/test_models/rectangle_base.py are pep8 compliant
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/rectangle.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_rectangle.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_make_correct_rectangle(self):
        """
        Tests for correct rectangle creation
        """
        rectangle1 = Rectangle(1, 2, 3, 4, 0)
        self.assertEqual(rectangle1.width, 1)
        self.assertEqual(rectangle1.height, 2)
        self.assertEqual(rectangle1.x, 3)
        self.assertEqual(rectangle1.y, 4)
        self.assertEqual(rectangle1.id, 0)
        rectangle2 = Rectangle(10, 10, 0, 0, -1)
        self.assertEqual(rectangle2.width, 10)
        self.assertEqual(rectangle2.height, 10)
        self.assertEqual(rectangle2.x, 0)
        self.assertEqual(rectangle2.y, 0)
        self.assertEqual(rectangle2.id, -1)

    def test_make_incorrect_rectangle(self):
        """
        Tests with errors in making a rectangle
        """
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            Rectangle("width", 1, 1, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, "height", 1, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, "x", 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, "y")
        with self.assertRaises(ValueError):
            Rectangle(0, 1, 1, 1)
        with self.assertRaises(ValueError):
            Rectangle(-4, 1, 1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 0, 1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, -4, 0, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -2, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 0, -7)

    def test_area(self):
        """
        Tests proper function of area method
        """
        rectangle1 = Rectangle(2, 4, 0, 0, 1)
        self.assertEqual(rectangle1.area(), 8)
        rectangle2 = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(rectangle2.area(), 1)

    def test_display(self):
        """
        Tests proper function of display method
        """
        rectangle1 = Rectangle(3, 3, 0, 0, 1)
        rectangle2 = Rectangle(2, 2, 2, 2, 2)
        with patch('sys.stdout', new=StringIO()) as out:
            rectangle1.display()
            self.assertEqual('###\n###\n###\n', out.getvalue())
        with patch('sys.stdout', new=StringIO()) as out:
            rectangle2.display()
            self.assertEqual('\n\n  ##\n  ##\n', out.getvalue())

    def test___str__(self):
        """
        Tests proper function of __str__ method
        """
        rectangle1 = Rectangle(2, 4, 0, 0, 42)
        self.assertEqual(rectangle1.__str__(), "[Rectangle] (42) 0/0 - 2/4")
        rectangle2 = Rectangle(3, 6, 0, 0, 1)
        self.assertEqual(rectangle2.__str__(), "[Rectangle] (1) 0/0 - 3/6")

    def test_update(self):
        """
        Test for proper use of update method
        """
        pass

    def test_bad_update(self):
        """
        Test for improper use of update method
        """
        pass

    def test_to_dictionary(self):
        """
        Tests for proper use of to_dictionary method
        """
        pass

    def test_bad_to_dictionary(self):
        """
        Tests for improper use of to_dictionary method
        """
        pass

if __name__ == '__main__':
    unittest.main()
