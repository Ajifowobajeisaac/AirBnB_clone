#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime

class TestCity(unittest.TestCase):

    def setUp(self):
        """
        Set up for the tests.
        """
        self.city = City()

    def tearDown(self):
        """
        Clean up after the tests.
        """
        del self.city

    def test_instance_type(self):
        """
        Test that the created instance is of type City.
        """
        self.assertTrue(isinstance(self.city, City))

    def test_inheritance(self):
        """
        Test that City inherits from BaseModel.
        """
        self.assertTrue(issubclass(City, BaseModel))

    def test_id(self):
        """
        Test that the city has an id.
        """
        self.assertEqual(type(self.city.id), str)

    def test_created_at(self):
        """
        Test that the city has a created_at attribute.
        """
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertEqual(type(self.city.created_at), datetime)

    def test_updated_at(self):
        """
        Test that the city has an updated_at attribute.
        """
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertEqual(type(self.city.updated_at), datetime)


if __name__ == '__main__':
    unittest.main()
