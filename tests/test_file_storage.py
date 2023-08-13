#!/usr/bin/python3
""" unittest tests for file_storage """

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test suite for the FileStorage class"""

    def setUp(self):
        """Set up before each test case"""
        # Initialize a new FileStorage instance for testing
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after each test case"""
        # Reset the storage instance
        self.storage = None

    # ... Other test methods ...

    def test_save_and_reload_with_base_model(self):
        """Test saving and reloading BaseModels in the storage"""
        # Create a new BaseModel instance
        base_model = BaseModel()
        base_model.name = "TestModel"
        base_model.save()

        # Save the storage and reload a new instance
        new_storage = FileStorage()
        new_storage.reload()

        # Retrieve the reloaded object
        reloaded_obj = new_storage.all().get(f"BaseModel.{base_model.id}")

        # Check if the reloaded object is an instance of BaseModel
        self.assertIsInstance(reloaded_obj, BaseModel)

        # Check if the reloaded object has the correct attributes
        self.assertEqual(reloaded_obj.name, "TestModel")

    def test_save_and_reload_multiple_models(self):
        """Test saving and reloading multiple model instances in the storage"""
        # Create multiple BaseModel instances
        model1 = BaseModel()
        model1.name = "Model1"
        model1.save()

        model2 = BaseModel()
        model2.name = "Model2"
        model2.save()

        # Save the storage and reload a new instance
        new_storage = FileStorage()
        new_storage.reload()

        # Retrieve the reloaded objects
        reloaded_model1 = new_storage.all().get(f"BaseModel.{model1.id}")
        reloaded_model2 = new_storage.all().get(f"BaseModel.{model2.id}")

        # Check if the reloaded objects are instances of BaseModel
        self.assertIsInstance(reloaded_model1, BaseModel)
        self.assertIsInstance(reloaded_model2, BaseModel)

        # Check if the reloaded objects have the correct attributes
        self.assertEqual(reloaded_model1.name, "Model1")
        self.assertEqual(reloaded_model2.name, "Model2")


if __name__ == '__main__':
    unittest.main()
