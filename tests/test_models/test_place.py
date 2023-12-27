#!/usr/bin/python3

import unittest
from models.place import Place
from models.base_model import BaseModel
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

    def test_inheritance(self):
        """
        Test that Place inherits from BaseModel.
        """
        self.assertTrue(issubclass(Place, BaseModel))


if __name__ == '__main__':
    unittest.main()
