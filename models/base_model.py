#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import getenv

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models

    Attributes:
        id (str): object unique id.
        created_at (datetime): object creation timestamp.
        updated_at (datetime): object last modification timestamp.

    """

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if getenv("HBNB_TYPE_STORAGE") != 'db':
                if 'updated_at' in kwargs.keys():
                    kwargs['updated_at'] = datetime.strptime(
                            kwargs['updated_at'],
                            '%Y-%m-%dT%H:%M:%S.%f'
                                                         )
                else:
                    self.updated_at = datetime.now()
                if 'created_at' in kwargs.keys():
                    kwargs['created_at'] = datetime.strptime(
                            kwargs['created_at'],
                            '%Y-%m-%dT%H:%M:%S.%f'
                                                         )
                else:
                    self.created_at = datetime.now()
                if '__class__' in kwargs.keys():
                    del kwargs['__class__']
                self.id = kwargs.get('id', str(uuid.uuid4()))
            else:
                self.id = str(uuid.uuid4())
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Delete the current instance from the storage"""
        storage.delete(self)
