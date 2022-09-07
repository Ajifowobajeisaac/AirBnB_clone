#!/usr/bin/python3
''' module for City class '''
from .base_model import BaseModel


class City(BaseModel):
    '''A City class

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    '''
    state_id = ''
    name = ''
