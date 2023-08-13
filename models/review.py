#!/usr/bin/python3
""" Creation of a class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class initialization """
    place_id = ""
    user_id = ""
    text = ""
