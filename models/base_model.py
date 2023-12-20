#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    """BaseModel class"""
    def __init__(self):
        """init method"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def __str__(self):
        """str method"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """save method"""
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """to_dict method"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at
        new_dict['updated_at'] = self.updated_at
        return new_dict
    
    @classmethod
    def from_dict(cls, data):
        """Create an instance from a dictionary"""
        obj = cls()
        obj.__dict__.update(data)
        obj.created_at = datetime.datetime.fromisoformat(data['created_at'])
        obj.updated_at = datetime.datetime.fromisoformat(data['updated_at'])
        return obj
