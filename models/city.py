#!/usr/bin/python3
"""
This module contains the BaseModel class, which serves as the base class for
all your models. It contains common elements such as id, created_at, and
updated_at attributes, and save() and to_dict() methods.
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    City class inherits from BaseModel.

    Attributes:
        name (str): The name of the city.
        state_id (str): The id of the state the city belongs to.
    """
    def __init__(self, name, state_id):
        super().__init__()
        self.name = name
        self.state_id = state_id

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.name)
