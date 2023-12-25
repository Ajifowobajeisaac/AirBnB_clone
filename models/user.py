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
    email = ""
    password = ""
    first_name = ""
    last_name = ""
