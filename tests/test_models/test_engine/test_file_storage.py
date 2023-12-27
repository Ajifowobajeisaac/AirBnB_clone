#!/usr/bin/python3

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def setUp(self):
        """
        Set up for the tests.
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Clean up after the tests.
        """
        del self.storage

    def test_no_args_instantiates(self):
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_new_method(self):
        b = BaseModel()
        self.storage.new(b)
        self.assertIn("BaseModel." + b.id, self.storage.all().keys())

    def test_all_method(self):
        self.assertEqual(dict, type(self.storage.all()))

    def test_save_method(self):
        b = BaseModel()
        self.storage.new(b)
        self.storage.save()
        with open("file.json", "r") as f:
            self.assertIn("BaseModel." + b.id, f.read())

    def test_reload_method(self):
        b = BaseModel()
        self.storage.new(b)
        self.storage.save()
        self.storage.reload()
        self.assertIn("BaseModel." + b.id, self.storage.all().keys())

    def test_file_path_is_private_str(self):
        self.assertEqual(str, type(self.storage._FileStorage__file_path))

    def test_objects_is_private_dict(self):
        self.assertEqual(dict, type(self.storage._FileStorage__objects))

    def test_file_path_attribute(self):
            self.assertEqual(str, type(self.storage._FileStorage__file_path))
            self.assertEqual("file.json", self.storage._FileStorage__file_path)

    def test_objects_attribute(self):
        self.assertEqual(dict, type(self.storage._FileStorage__objects))
        self.assertEqual({}, self.storage._FileStorage__objects)
    
    def test_new_method(self):
        b = BaseModel()
        self.storage.new(b)
        self.assertIn("BaseModel." + b.id, self.storage.all().keys())

    def test_save_method(self):
        b = BaseModel()
        old_updated_at = b.updated_at
        b.save()
        self.assertNotEqual(old_updated_at, b.updated_at)
        with open("file.json", "r") as f:
            self.assertIn("BaseModel." + b.id, f.read())


if __name__ == '__main__':
    unittest.main()
