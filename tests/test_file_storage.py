#! /usr/bin/python3

import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """
    This class contains the test cases for the FileStorage class.
    """
    def setUp(self):
        """
        This method Sets up the testing dependencies before each test case
        """
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.storage.new(self.obj)

    def tearDown(self):
        """
        This method cleans up the testing dependencies after each test case
        """
        del self.storage
        del self.obj
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_class_attributes(self):
        """
        Test the class attributes of FileStorage.
        """
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)


    def test_all(self):
        """
        Test the 'all' method of the FileStorage class.
        """
       
        all_objects = self.storage.all()
        self.assertIn('BaseModel.' + self.obj.id, all_objects)
        self.assertEqual(all_objects['BaseModel.' + self.obj.id], self.obj)

    def test_new(self):
        """
        Test the 'new' method of the FileStorage class.
        """
        obj2 = BaseModel()
        self.storage.new(obj2)
        all_objects = self.storage.all()
        self.assertIn('BaseModel.' + obj2.id, all_objects)
        self.assertEqual(all_objects['BaseModel.' + obj2.id], obj2)

    def test_save(self):
        """
        Test the 'save' method of the FileStorage class.
        """
        self.storage.save()

        self.assertTrue(os.path.exists('file.json'))
        with open('file.json', 'r') as f:
            obj_dict = json.load(f)

        self.assertIn('BaseModel.' + self.obj.id, obj_dict)

        self.assertEqual(obj_dict['BaseModel.' + self.obj.id]['id'], self.obj.id)

    def test_reload(self):
        """
        Test the 'reload' method of the FileStorage class.
        """
        self.storage.save()

        self.storage.reset()

        self.storage.reload()

        all_objects = self.storage.all()

        self.assertIn('BaseModel.' + self.obj.id, all_objects)

        self.assertEqual(all_objects['BaseModel.' + self.obj.id].id, self.obj.id)


if __name__ == '__main__':
    unittest.main()
    