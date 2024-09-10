#! /usr/bin/python3

import unittest
from datetime import datetime

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""

    def setUp(self):
        """Set up BaseModel instance for testing"""
        self.base_model_instance = BaseModel()

    def tearDown(self):
        del self.base_model_instance

    def test_init(self):
        """Test BaseModel instance initialization"""

        self.assertIsNotNone(self.base_model_instance.id)
        self.assertIsNotNone(self.base_model_instance.created_at)
        self.assertIsNotNone(self.base_model_instance.updated_at)


        self.assertIsInstance(self.base_model_instance.id, str)

        self.assertIsInstance(self.base_model_instance.created_at, datetime)
        self.assertIsInstance(self.base_model_instance.updated_at, datetime)

    def test_save(self):
        """Test if save method updates the updated_at attribute"""

        updated_at = self.base_model_instance.save()

        self.assertEqual(updated_at, self.base_model_instance.updated_at) 

    def test_to_dict(self):
        """Test if the to_dict method returns the correct dictionary version of the instance"""

        model_inst_dict = self.base_model_instance.to_dict()


        self.assertIn("__class__", model_inst_dict)

        self.assertEqual(model_inst_dict["__class__"], self.base_model_instance.__class__.__name__)

        self.assertEqual(model_inst_dict["created_at"], self.base_model_instance.created_at.isoformat())
        self.assertEqual(model_inst_dict["updated_at"], self.base_model_instance.updated_at.isoformat())

    def test_str(self):
        """Test if the __str__ method returns the correct string representation of the instance"""
        expected_str = f"[{self.base_model_instance.__class__.__name__}] ({self.base_model_instance.id}) {self.base_model_instance.__dict__}"
        self.assertEqual(str(self.base_model_instance), expected_str)


if __name__ == "__main__":
    unittest.main()