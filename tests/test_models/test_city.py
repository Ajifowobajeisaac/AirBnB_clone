#!/usr/bin/python3

import unittest
import os
from models import storage
from models.city import City
from datetime import datetime
from time import sleep


class TestCity(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

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

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_city_storage(self):
        city = City()
        storage.new(city)
        storage.save()
        stored_cities = storage.all(City)
        self.assertIn(city, stored_cities.values())

    def test_two_cities_unique_ids(self):
        c1 = City()
        c2 = City()
        self.assertNotEqual(c1.id, c2.id)

    def test_two_cities_different_created_at(self):
        c1 = City()
        sleep(0.05)
        c2 = City()
        self.assertLess(c1.created_at, c2.created_at)

    def test_two_cities_different_updated_at(self):
        c1 = City()
        sleep(0.05)
        c2 = City()
        self.assertLess(c1.updated_at, c2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        c = City()
        c.id = "123456"
        c.created_at = c.updated_at = dt
        cstr = c.__str__()
        self.assertIn("[City] (123456)", cstr)
        self.assertIn("'id': '123456'", cstr)
        self.assertIn("'created_at': " + dt_repr, cstr)
        self.assertIn("'updated_at': " + dt_repr, cstr)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        c = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(c.id, "345")
        self.assertEqual(c.created_at, dt)
        self.assertEqual(c.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        c = City("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(c.id, "345")
        self.assertEqual(c.created_at, dt)
        self.assertEqual(c.updated_at, dt)

    def test_save_method(self):
        c = City()
        old_updated_at = c.updated_at
        c.save()
        self.assertNotEqual(old_updated_at, c.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("City." + c.id, f.read())

    def test_to_dict(self):
        c = City()
        c_dict = c.to_dict()
        self.assertEqual(dict, type(c_dict))
        self.assertIn('__class__', c_dict)
        self.assertEqual('City', c_dict['__class__'])
        self.assertIn('id', c_dict)
        self.assertEqual(str, type(c_dict['id']))
        self.assertIn('created_at', c_dict)
        self.assertEqual(str, type(c_dict['created_at']))
        self.assertIn('updated_at', c_dict)
        self.assertEqual(str, type(c_dict['updated_at']))


if __name__ == '__main__':
    unittest.main()
