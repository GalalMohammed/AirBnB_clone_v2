#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from urllib.parse import quote_plus
from sqlalchemy import MetaData
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models"""
    __engine = None
    __session = None
    classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
          }

    def __init__(self):
        """Instatntiates a new storage manager"""
        self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}/{}".format(
                    getenv("HBNB_MYSQL_USER"),
                    quote_plus(getenv("HBNB_MYSQL_PWD")),
                    getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB")),
                pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            m = MetaData()
            m.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage
        Args:
        cls(obj): class to filter the returned objects.
        Return:
            dict.
        """
        dict_objs = {}
        if cls:
            list_objs = self.__session.query(cls).all()
            for obj in list_objs:
                dict_objs[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for cls_name, c in DBStorage.classes.items():
                list_cls_obj = self.__session.query(c).all()
                for obj in list_cls_objs:
                    dict_objs[obj.__class__.__name__ + '.' + obj.id] = obj
        return dict_objs

    def new(self, obj):
        """Adds new object to db
        Args:
            obj (object): object to be added."""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj
        Args:
            obj (object): object to be deleted."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database
        and the current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
