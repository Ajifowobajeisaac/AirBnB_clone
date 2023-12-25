#!/usr/bin/python3
"""
This module contains the State class, which inherits from the BaseModel class.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class inherits from BaseModel.

    Attributes:
        name (str): The name of the state.
    """

    def __init__(self, name, cities=None):
        super().__init__()
        self.name = name
        self.cities = cities if cities is not None else []

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.name)
