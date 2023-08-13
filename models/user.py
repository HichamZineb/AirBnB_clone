#!/usr/bin/python3
""" Creation of a class User """
from models.base_model import BaseModel

class User(BaseModel):
    """ User class initialization """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
