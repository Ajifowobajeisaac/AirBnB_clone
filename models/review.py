#!/usr/bin/python3
"""
This module contains the Review class, which inherits from the BaseModel class.
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review class inherits from BaseModel.

    Attributes:
        place_id (str): The id of the place the review belongs to.
        user_id (str): The id of the user who wrote the review.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
