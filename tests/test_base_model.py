#!/usr/bin/python3
""" unittest tests for base_model """


import unittest
from models.base_model import BaseModel


class Test_base_model(unittest.TestCase):
    """ Tests for base_model """

    def test_init(self):
        """ Test for creating a new instance of BaseModel """

        new_instance = BaseModel()
        self.assertIsInstance(new_instance, BaseModel)

    def test_to_dict(self):
        """ Test for to_dict method """

        new_instance = BaseModel()
        new_instance_dict = new_instance.to_dict()
        self.assertIsInstance(new_instance_dict, dict)
        self.assertEqual(new_instance_dict['__class__'], 'BaseModel')
        self.assertIn('id', new_instance_dict)
        self.assertIn('created_at', new_instance_dict)
        self.assertIn('updated_at', new_instance_dict)

    def test_from_dict(self):
        """ Test for creating an instance from a dictionary """

        data = {
            '__class__': 'BaseModel',
            'id': '123',
            'created_at': '2023-08-09T12:34:56.789012',
            'updated_at': '2023-08-09T12:34:56.789012'
        }
        dict_instance = BaseModel(**data)
        self.assertIsInstance(dict_instance, BaseModel)
        self.assertEqual(dict_instance.id, '123')
        self.assertEqual(dict_instance.created_at.year, 2023)
        self.assertEqual(dict_instance.updated_at.year, 2023)

    def test_str(self):
        """ Test for the __str__ method """

        inst = BaseModel()
        inst_str = str(inst)
        class_name = inst.__class__.__name__
        self.assertEqual(
            inst_str,
            "[{}] ({}) <{}>".format(class_name, inst.id, inst.__dict__))

    def test_save(self):
        """ Test for the save method """

        new_instance = BaseModel()
        prev_updated_at = new_instance.updated_at
        new_instance.save()
        self.assertNotEqual(new_instance.updated_at, prev_updated_at)


if __name__ == '__main__':
    unittest.main()
