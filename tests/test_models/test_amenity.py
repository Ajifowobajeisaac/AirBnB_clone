#!/ust/bin/python3

import unittest
from models.amenity import Amenity
from datetime import datetime
from time import sleep

class TestAmenity(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def setUp(self):
        """
        Set up for the tests.
        """
        self.amenity = Amenity()

    def tearDown(self):
        """
        Clean up after the tests.
        """
        del self.amenity

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_two_amenities_unique_ids(self):
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.id, a2.id)

    def test_two_amenities_different_created_at(self):
        a1 = Amenity()
        sleep(0.05)
        a2 = Amenity()
        self.assertLess(a1.created_at, a2.created_at)

    def test_two_amenities_different_updated_at(self):
        a1 = Amenity()
        sleep(0.05)
        a2 = Amenity()
        self.assertLess(a1.updated_at, a2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        a = Amenity()
        a.id = "123456"
        a.created_at = a.updated_at = dt
        astr = a.__str__()
        self.assertIn("[Amenity] (123456)", astr)
        self.assertIn("'id': '123456'", astr)
        self.assertIn("'created_at': " + dt_repr, astr)
        self.assertIn("'updated_at': " + dt_repr, astr)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        a = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(a.id, "345")
        self.assertEqual(a.created_at, dt)
        self.assertEqual(a.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        a = Amenity("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(a.id, "345")
        self.assertEqual(a.created_at, dt)
        self.assertEqual(a.updated_at, dt)

    def test_save_method(self):
        a = Amenity()
        old_updated_at = a.updated_at
        a.save()
        self.assertNotEqual(old_updated_at, a.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("Amenity." + a.id, f.read())

    def test_to_dict(self):
        a = Amenity()
        a_dict = a.to_dict()
        self.assertEqual(dict, type(a_dict))
        self.assertIn('__class__', a_dict)
        self.assertEqual('Amenity', a_dict['__class__'])
        self.assertIn('id', a_dict)
        self.assertEqual(str, type(a_dict['id']))
        self.assertIn('created_at', a_dict)
        self.assertEqual(str, type(a_dict['created_at']))
        self.assertIn('updated_at', a_dict)
        self.assertEqual(str, type(a_dict['updated_at']))

if __name__ == '__main__':
    unittest.main()
