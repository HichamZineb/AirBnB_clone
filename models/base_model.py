#!/usr/bin/python3
""" Creation of a class BaseModel """

import uuid
from datetime import datetime
import models


class BaseModel:
    """ BaseModel class initialization """

    def __init__(self, *args, **kwargs):
        """ Initialization """

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        models.storage.new(self)

    def __str__(self):
        """ Return a string representation """

        class_name = self.__class__.__name__
        return "[{}] ({}) <{}>".format(class_name, self.id, self.__dict__)

    def save(self):
        """ Save method """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return a dictionnary """

        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()

        return data
