#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """class to inherit from BaseModel
    Attributes:
        name (str): amenity name.
        place_amenities (object): relationship.
    """
    name = Column(String(128), nullable=False)
    __tablename__ = 'amenities'
