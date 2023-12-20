#!/usr/bin/python3
from models.base_model import BaseModel

class City(BaseModel):
    """City class that inherits from BaseModel"""
    def __init__(self, name, state_id):
        super().__init__()
        self.name = name
        self.state_id = state_id

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.name)
