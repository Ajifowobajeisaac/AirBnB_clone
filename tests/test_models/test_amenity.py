import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime

class TestAmenity(unittest.TestCase):
    
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
    
        def test_instance_type(self):
            """
            Test that the created instance is of type Amenity.
            """
            self.assertTrue(isinstance(self.amenity, Amenity))
    
        def test_inheritance(self):
            """
            Test that Amenity inherits from BaseModel.
            """
            self.assertTrue(issubclass(Amenity, BaseModel))
    
        def test_id(self):
            """
            Test that the amenity has an id.
            """
            self.assertEqual(type(self.amenity.id), str)
    
        def test_created_at(self):
            """
            Test that the amenity has a created_at attribute.
            """
            self.assertTrue(hasattr(self.amenity, "created_at"))
            self.assertEqual(type(self.amenity.created_at), datetime)
    
        def test_updated_at(self):
            """
            Test that the amenity has an updated_at attribute.
            """
            self.assertTrue(hasattr(self.amenity, "updated_at"))
            self.assertEqual(type(self.amenity.updated_at), datetime)


if __name__ == '__main__':
    unittest.main()
