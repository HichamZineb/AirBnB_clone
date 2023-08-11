#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        date_format = "%Y-%m-%dT%H:%M:%S.%f"
                        value = datetime.strptime(value, date_format)
                        setattr(self, key, value)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):

        class_name = self.__class__.__name__
        return "[{}] ({}) <{}>".format(class_name, self.id, self.__dict__)

    def save(self):

        self.updated_at = datetime.now()

    def to_dict(self):

        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()

        return data
