#!/usr/bin/python3

import unittest
from models.state import State
from models import storage
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestState(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

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

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_state_storage(self):
        """
        Test that a State instance is correctly stored.
        """
        s = State()
        storage.new(s)
        storage.save()
        stored_states = storage.all(State)
        self.assertIn(s, stored_states.values())

    def test_two_states_unique_ids(self):
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.id, s2.id)

    def test_two_states_different_created_at(self):
        s1 = State()
        sleep(0.05)
        s2 = State()
        self.assertLess(s1.created_at, s2.created_at)

    def test_two_states_different_updated_at(self):
        s1 = State()
        sleep(0.05)
        s2 = State()
        self.assertLess(s1.updated_at, s2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        s = State()
        s.id = "123456"
        s.created_at = s.updated_at = dt
        sstr = s.__str__()
        self.assertIn("[State] (123456)", sstr)
        self.assertIn("'id': '123456'", sstr)
        self.assertIn("'created_at': " + dt_repr, sstr)
        self.assertIn("'updated_at': " + dt_repr, sstr)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        s = State(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(s.id, "345")
        self.assertEqual(s.created_at, dt)
        self.assertEqual(s.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        s = State("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(s.id, "345")
        self.assertEqual(s.created_at, dt)
        self.assertEqual(s.updated_at, dt)

    def test_inheritance(self):
        """
        Test that State inherits from BaseModel.
        """
        self.assertTrue(issubclass(State, BaseModel))


if __name__ == '__main__':
    unittest.main()
