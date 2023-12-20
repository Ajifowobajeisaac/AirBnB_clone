#!/usr/bin/python3
from models.base_model import BaseModel

class Place(BaseModel):
    """Place class that inherits from BaseModel"""
    def __init__(self, name, description, city_id, user_id):
        super().__init__()
        self.name = name
        self.description = description
        self.city_id = city_id
        self.user_id = user_id

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.name)
