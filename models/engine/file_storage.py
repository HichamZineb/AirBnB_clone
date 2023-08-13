#!/usr/binb/python3
""" Creation of class FileStorage
    For serialization and deserialization
"""

import json
import os
import uuid
from datetime import datetime
from models.base_model import BaseModel


class FileStorage:
    """ FileStorage class construct """

    __file_path = 'file.json'
    __objects = {}

    class_map = {
        "BaseModel": BaseModel,
    }

    def all(self):
        """ all method return dictionnary __objects """

        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """

        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """

        temp_dict = {}

        for key, value in FileStorage.__objects.items():
            temp_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(temp_dict, file)

    def reload(self):
        """ Deserializes the JSON file to __objects (if file exists) """

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name in FileStorage.class_map:
                        obj_class = FileStorage.class_map[class_name]
                        new_obj = obj_class(**value)
                        FileStorage.__objects[key] = new_obj
                    else:
                        pass
