#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.review import Review
from datetime import datetime
import os
import json

class TestReview(unittest.TestCase):
    """Test the Review class"""

    def setUp(self):
        """Sets up test methods."""
        self.review = Review()
        self.review.save()

    def tearDown(self):
        """Tears down test methods."""
        try:
            os.remove("file.json")
        except:
            pass

    def test_docstring(self):
        """Check for docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_attributes(self):
        """Check if instance of BaseModel successfully made"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_subclass(self):
        """Check if instance of BaseModel successfully made"""
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    def test_attribute_type(self):
        """Check attribute type"""
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(type(self.review.text), str)

    def test_save(self):
        """Check save method"""
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    def test_to_dict(self):
        """Check to_dict method"""
        self.assertEqual("to_dict" in dir(self.review), True)

    
if __name__ == "__main__":
    unittest.main()
