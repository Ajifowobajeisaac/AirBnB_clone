#!/usr/bin/python3
"""
This module contains the User class, which inherits from the BaseModel class.
"""

from .base_model import BaseModel


class User(BaseModel):
    """
    User class inherits from BaseModel.

    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    def __init__(self, email="", password="", first_name="", last_name=""):
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__)
