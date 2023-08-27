#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay

    Attributes:
        city_id (str): city id.
        user_id (str): user id.
        name (str): place name.
        description (str): place discription.
        number_rooms (int): place rooms number.
        number_bathrooms (int): place bathrooms number.
        max_guest (int): place max number of guests.
        price_by_night (int): place night price.
        latitude (float): place lat.
        longitude (float): place long.
        amenity_ids (list): place amenity ids.
        reviews (object): user review of place.

    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenity_ids = []

    @property
    def reviews(self):
        """Get the list of Review instances
        Return:
            list
        """
        reviews_objs = list(storage.all(Review).values())
        return list(filter(lambda obj: obj.place_id == self.id, reviews_objs))
