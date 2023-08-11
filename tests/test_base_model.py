#!/usr/bin/python3
""" unittest tests for base_model """


import unittest
from models.base_model import BaseModel

class Test_base_model(unittest.TestCase):
    """ Tests for base_model """

    def test_init(self):
        """ Test creating a new instance of BaseModel """

        new_instance = BaseModel()
        self.assertIsInstance(new_instance, BaseModel)

if __name__ == '__main__':
    unittest.main()
