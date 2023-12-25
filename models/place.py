#!/usr/bin/python3
"""
This module contains the Place class, which inherits from the BaseModel class.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class inherits from BaseModel.

    Attributes:
        name (str): The name of the place.
        city_id (str): The id of the city the place belongs to.
        user_id (str): The id of the user who owns the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests the place can
          accommodate.
        price_by_night (int): The price per night to stay at the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list of str): A list of amenity ids associated with the
          place.
    """

    def __init__(self, name, description, city_id, user_id):
        super().__init__()
        self.name = name
        self.description = description
        self.city_id = city_id
        self.user_id = user_id

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.name)
