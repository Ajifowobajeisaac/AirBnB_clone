#!/usr/bin/python3
from models.base_model import BaseModel

class State(BaseModel):
    """State class that inherits from BaseModel"""
    def __init__(self, name, cities=None):
        super().__init__()
        self.name = name
        self.cities = cities if cities is not None else []

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.name)
