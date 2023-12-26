#!/usr/bin/python3

import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime

class TestState(unittest.TestCase):

    def setUp(self):
        """
        Set up for the tests.
        """
        self.state = State()

    def tearDown(self):
        """
        Clean up after the tests.
        """
        del self.state

    def test_instance_type(self):
        """
        Test that the created instance is of type State.
        """
        self.assertTrue(isinstance(self.state, State))

    def test_inheritance(self):
        """
        Test that State inherits from BaseModel.
        """
        self.assertTrue(issubclass(State, BaseModel))

    def test_id(self):
        """
        Test that the state has an id.
        """
        self.assertEqual(type(self.state.id), str)

    def test_created_at(self):
        """
        Test that the state has a created_at attribute.
        """
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertEqual(type(self.state.created_at), datetime)

    def test_updated_at(self):
        """
        Test that the state has an updated_at attribute.
        """
        self.assertTrue(hasattr(self.state, "updated_at"))
        self.assertEqual(type(self.state.updated_at), datetime)

if __name__ == '__main__':
    unittest.main()
