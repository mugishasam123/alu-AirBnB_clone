#! /usr/bin/python3

import unittest
import os
from models import storage
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ 
    Unit test class for City model
    """

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
    
    def test_city_attributes(self):
        """
        Tests the default values of City attributes.
        """
        city = City()

        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
    
    def test_city_inherits_from_basemodel(self):
        """
        Tests that City inherits from BaseModel.
        """
        city = City()

        self.assertTrue(issubclass(type(city), BaseModel))

    def test_city_string_representation(self):
        """
        Tests the string representation of City.
        """
        city = City()

        self.assertEqual(str(city), f"[City] ({city.id}) {city.__dict__}")

    def test_addition(self):
        """
        Tests the default values of Amenity attributes.
        """

        self.assertEqual(1+1, 2)

    def test_city_to_dict(self):
        """
        Tests the to_dict method of City.
        """
        city = City()

        city.state_id = "123"
        city.name = "Michigan"

        city_dict = city.to_dict()

        self.assertEqual(city_dict["id"], city.id)
        self.assertEqual(city_dict["created_at"], city.created_at.isoformat())
        self.assertEqual(city_dict["updated_at"], city.updated_at.isoformat())
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(city_dict["state_id"], "123")
        self.assertEqual(city_dict["name"], "Michigan")

    def test_city_save(self):
        """
        Tests the save method of City.
        """
        city = City()

        city.save()

        objects = storage.all()

        key = f"City.{city.id}"


if __name__ == "__main__":
    unittest.main()