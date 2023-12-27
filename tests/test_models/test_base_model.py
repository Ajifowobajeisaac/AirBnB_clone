#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestBaseModel(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def setUp(self):
        """
        Set up for the tests.
        """
        self.base = BaseModel()

    def tearDown(self):
        """
        Clean up after the tests.
        """
        del self.base

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_bases_unique_ids(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_two_bases_different_created_at(self):
        b1 = BaseModel()
        sleep(0.05)
        b2 = BaseModel()
        self.assertLess(b1.created_at, b2.created_at)

    def test_two_bases_different_updated_at(self):
        b1 = BaseModel()
        sleep(0.05)
        b2 = BaseModel()
        self.assertLess(b1.updated_at, b2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        b = BaseModel()
        b.id = "123456"
        b.created_at = b.updated_at = dt
        bstr = b.__str__()
        self.assertIn("[BaseModel] (123456)", bstr)
        self.assertIn("'id': '123456'", bstr)
        self.assertIn("'created_at': " + dt_repr, bstr)
        self.assertIn("'updated_at': " + dt_repr, bstr)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        b = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(b.id, "345")
        self.assertEqual(b.created_at, dt)
        self.assertEqual(b.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        b = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(b.id, "345")
        self.assertEqual(b.created_at, dt)
        self.assertEqual(b.updated_at, dt)


if __name__ == '__main__':
    unittest.main()
