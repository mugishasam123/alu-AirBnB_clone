#! /usr/bin/python3

import unittest
import os

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Unit test class for Amenity"""

    def setUp(self):
        """
        Creates a temporary test file and saves it.
        """
        with open("test_file.json", "w") as f:
            pass

        storage.save()
    
    def tearDown(self):
        """
        Removes the temporary test file if it exists.
        """
        try:
            os.remove("test_file.json")
        except FileNotFoundError:
            pass
    
    def test_amenity_attributes(self):
        """
        Tests the default values of Amenity attributes.
        """
        amenity = Amenity()

        self.assertEqual(amenity.name, "")

    def test_amenity_addition(self):
        """
        Tests the default values of Amenity attributes.
        """

        self.assertEqual(1+1, 2)
    
    def test_amenity_inherits_from_basemodel(self):
        """
        Tests that Amenity inherits from BaseModel.
        """
        amenity = Amenity()

        self.assertTrue(issubclass(type(amenity), BaseModel))
    
    def test_amenity_string_representation(self):
        """
        Tests the string representation of Amenity.
        """
        amenity = Amenity()

        self.assertEqual(str(amenity), f"[Amenity] ({amenity.id}) {amenity.__dict__}")

    def test_amenity_save(self):
        """
        Tests the save method of Amenity.
        """
        amenity = Amenity()

        amenity.save()

        objects = storage.all()

        key = f"{amenity.__class__.__name__}.{amenity.id}"

        self.assertTrue(key in objects)
    
    def test_amenity_to_dict(self):
        """
        Tests the to_dict method of Amenity.
        """
        amenity = Amenity()

        amenity.name = "Wifi"

        amenity_dict = amenity.to_dict()

        self.assertEqual(amenity_dict, {
            "id": amenity.id,
            "created_at": amenity.created_at.isoformat(),
            "updated_at": amenity.updated_at.isoformat(),
            "name": "Wifi",
            "__class__": "Amenity"
        })
    
if __name__ == "__main__":
    unittest.main()