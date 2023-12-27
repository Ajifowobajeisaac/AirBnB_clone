#!/usr/bin/python3

import unittest
from models import storage
from models.place import Place
from datetime import datetime
from time import sleep

class TestPlace(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

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

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_place_storage(self):
        """
        Test that a Place instance is correctly stored.
        """
        p = Place()
        storage.new(p)
        storage.save()
        stored_places = storage.all(Place)
        self.assertIn(p, stored_places.values())

    def test_two_places_unique_ids(self):
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)

    def test_two_places_different_created_at(self):
        p1 = Place()
        sleep(0.05)
        p2 = Place()
        self.assertLess(p1.created_at, p2.created_at)

    def test_two_places_different_updated_at(self):
        p1 = Place()
        sleep(0.05)
        p2 = Place()
        self.assertLess(p1.updated_at, p2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        p = Place()
        p.id = "123456"
        p.created_at = p.updated_at = dt
        pstr = p.__str__()
        self.assertIn("[Place] (123456)", pstr)
        self.assertIn("'id': '123456'", pstr)
        self.assertIn("'created_at': " + dt_repr, pstr)
        self.assertIn("'updated_at': " + dt_repr, pstr)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        p = Place(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(p.id, "345")
        self.assertEqual(p.created_at, dt)
        self.assertEqual(p.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        p = Place("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(p.id, "345")
        self.assertEqual(p.created_at, dt)
        self.assertEqual(p.updated_at, dt)

    def test_save_method(self):
        p = Place()
        old_updated_at = p.updated_at
        p.save()
        self.assertNotEqual(old_updated_at, p.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("Place." + p.id, f.read())

    def test_to_dict(self):
        p = Place()
        p_dict = p.to_dict()
        self.assertEqual(dict, type(p_dict))
        self.assertIn('__class__', p_dict)
        self.assertEqual('Place', p_dict['__class__'])
        self.assertIn('id', p_dict)
        self.assertEqual(str, type(p_dict['id']))
        self.assertIn('created_at', p_dict)
        self.assertEqual(str, type(p_dict['created_at']))
        self.assertIn('updated_at', p_dict)
        self.assertEqual(str, type(p_dict['updated_at']))

if __name__ == '__main__':
    unittest.main()
