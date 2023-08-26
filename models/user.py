#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel):
    """This class defines a user by various attributes
    Attributes:
        email(str): the user's email
        password(str): the user's password
        first_name(str): the user's first name
        last_name(str): the user's last name
    """
    __tablename__ = "users"
    email = Colomn(String(128), nullable=False)
    password = Colomn(String(128), nullable=False)
    first_name = Colomn(String(128))
    last_name = Colomn(String(128))
