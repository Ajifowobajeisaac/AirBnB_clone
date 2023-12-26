#!/usr/bin/python3
"""
This module contains the BaseModel class, which serves as the base class for
all models. It contains common elements such as id, created_at, and
updated_at attributes, and save() and to_dict() methods.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class

    Attributes:
        id (str): The unique id of the BaseModel instance.
        created_at (datetime): The time the BaseModel instance was created.
        updated_at (datetime): The time the BaseModel instance was last
          updated.

    Methods:
        __init__(*args, **kwargs): Initializes a new BaseModel instance.
        __str__(): Returns a string representation of the BaseModel instance.
        save(): Updates the updated_at attribute and saves the BaseModel
          instance.
        to_dict(): Returns a dictionary representation of the BaseModel
          instance.
    """
    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance
        Args:
            *args: unused
            **kwargs: Arbitrary keyword arguments.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    if not isinstance(value, datetime):
                        value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """str method -
        Returns:
            str: A string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """save method -
        Updates the updated_at attribute and saves the BaseModel instance.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the
          instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__

        if isinstance(self.created_at, datetime):
            new_dict["created_at"] = self.created_at.isoformat()
        if isinstance(self.updated_at, datetime):
            new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
