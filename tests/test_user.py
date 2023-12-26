#!/usr/bin/python3

import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime

class TestUser(unittest.TestCase):

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

    def test_instance_type(self):
        """
        Test that the created instance is of type User.
        """
        self.assertTrue(isinstance(self.user, User))

    def test_inheritance(self):
        """
        Test that User inherits from BaseModel.
        """
        self.assertTrue(issubclass(User, BaseModel))

    def test_id(self):
        """
        Test that the user has an id.
        """
        self.assertEqual(type(self.user.id), str)

    def test_created_at(self):
        """
        Test that the user has a created_at attribute.
        """
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertEqual(type(self.user.created_at), datetime)

    def test_updated_at(self):
        """
        Test that the user has an updated_at attribute.
        """
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertEqual(type(self.user.updated_at), datetime)

if __name__ == '__main__':
    unittest.main()
