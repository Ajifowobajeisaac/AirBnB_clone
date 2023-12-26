#!/usr/bin/python3

import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime

class TestPlace(unittest.TestCase):

    def setUp(self):
        """
        Set up for the tests.
        """
        self.place = Place()

    def tearDown(self):
        """
        Clean up after the tests.
        """
        del self.place

    def test_instance_type(self):
        """
        Test that the created instance is of type Place.
        """
        self.assertTrue(isinstance(self.place, Place))

    def test_inheritance(self):
        """
        Test that Place inherits from BaseModel.
        """
        self.assertTrue(issubclass(Place, BaseModel))

    def test_id(self):
        """
        Test that the place has an id.
        """
        self.assertEqual(type(self.place.id), str)

    def test_created_at(self):
        """
        Test that the place has a created_at attribute.
        """
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertEqual(type(self.place.created_at), datetime)

    def test_updated_at(self):
        """
        Test that the place has an updated_at attribute.
        """
        self.assertTrue(hasattr(self.place, "updated_at"))
        self.assertEqual(type(self.place.updated_at), datetime)

if __name__ == '__main__':
    unittest.main()
