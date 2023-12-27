#!/usr/bin/python3

import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime
from time import sleep

class TestReview(unittest.TestCase):
    """Unittests for testing instantiation of the Review class."""

    def setUp(self):
        """
        Set up for the tests.
        """
        self.review = Review()

    def tearDown(self):
        """
        Clean up after the tests.
        """
        del self.review

    def test_no_args_instantiates(self):
        self.assertEqual(Review, type(Review()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_two_reviews_unique_ids(self):
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.id, r2.id)

    def test_two_reviews_different_created_at(self):
        r1 = Review()
        sleep(0.05)
        r2 = Review()
        self.assertLess(r1.created_at, r2.created_at)

    def test_two_reviews_different_updated_at(self):
        r1 = Review()
        sleep(0.05)
        r2 = Review()
        self.assertLess(r1.updated_at, r2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        r = Review()
        r.id = "123456"
        r.created_at = r.updated_at = dt
        rstr = r.__str__()
        self.assertIn("[Review] (123456)", rstr)


if __name__ == "__main__":
    unittest.main()
