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

    name = ""
