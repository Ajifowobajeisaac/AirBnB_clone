#!/usr/bin/python3
''' module for Review class '''
from .base_model import BaseModel


class Review(BaseModel):
    '''A Review class 

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    '''
    place_id = ''
    user_id = ''
    text = ''
