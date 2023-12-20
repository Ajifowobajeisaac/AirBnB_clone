#!/usr/bin/python3
from base_model import BaseModel

from base_model import BaseModel

class User(BaseModel):
    """User class that inherits from BaseModel"""
    def __init__(self, name, email):
        super().__init__()
        self.name = name
        self.email = email
