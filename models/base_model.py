#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """init method"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now().isoformat()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now().isoformat()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()
            storage.new(self)


    def __str__(self):
        """str method"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """save method"""
        self.updated_at = datetime.now().isoformat()
        storage.save()

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
