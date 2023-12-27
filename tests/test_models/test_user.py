#!/usr/bin/python3
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestUser(unittest.TestCase):
    """Unittests for testing instantiation of the User class."""

    def setUp(self):
        """
        Set up for the tests.
        """
        self.user = User()

    def tearDown(self):
        """
        Clean up after the tests.
        """
        del self.user

    def test_no_args_instantiates(self):
        self.assertEqual(User, type(User()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_two_users_unique_ids(self):
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)

    def test_two_users_different_created_at(self):
        u1 = User()
        sleep(0.05)
        u2 = User()
        self.assertLess(u1.created_at, u2.created_at)

    def test_two_users_different_updated_at(self):
        u1 = User()
        sleep(0.05)
        u2 = User()
        self.assertLess(u1.updated_at, u2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        u = User()
        u.id = "123456"
        u.created_at = u.updated_at = dt
        ustr = u.__str__()
        self.assertIn("[User] (123456)", ustr)
        self.assertIn("'id': '123456'", ustr)
        self.assertIn("'created_at': " + dt_repr, ustr)
        self.assertIn("'updated_at': " + dt_repr, ustr)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        u = User(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(u.id, "345")
        self.assertEqual(u.created_at, dt)
        self.assertEqual(u.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        u = User("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(u.id, "345")
        self.assertEqual(u.created_at, dt)
        self.assertEqual(u.updated_at, dt)

    def test_inheritance(self):
        """
        Test that User inherits from BaseModel.
        """
        self.assertTrue(issubclass(User, BaseModel))


if __name__ == '__main__':
    unittest.main()
