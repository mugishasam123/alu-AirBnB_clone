#! /usr/bin/python3

import unittest
import os

from models import storage
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Unit test class for Place
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
    
    def test_place_attributes(self):
        """
        Tests the default values of Place attributes.
        """
        place = Place()

        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])
    
    def test_place_inherits_from_basemodel(self):
        """
        Tests that Place inherits from BaseModel.
        """
        place = Place()

        self.assertTrue(issubclass(type(place), BaseModel))
    
    def test_place_to_dict(self):
        """
        Tests the to_dict method of Place.
        """
        place = Place()
        place.city_id = "123"
        place.user_id = "456"
        place.name = "Far away from home"
        place.description = "No tenant needed"
        place.number_rooms = 1
        place.number_bathrooms = 1
        place.max_guest = 1
        place.price_by_night = 1
        place.latitude = 1.0
        place.longitude = 1.0
        place.amenity_ids = ["amenity_id1"]

        place_dict = place.to_dict()

        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["id"], place.id)
        self.assertEqual(place_dict["created_at"], place.created_at.isoformat())
        self.assertEqual(place_dict["updated_at"], place.updated_at.isoformat())
        self.assertEqual(place_dict["city_id"], place.city_id)
        self.assertEqual(place_dict["user_id"], place.user_id)
        self.assertEqual(place_dict["name"], place.name)
        self.assertEqual(place_dict["description"], place.description)
        self.assertEqual(place_dict["number_rooms"], place.number_rooms)
        self.assertEqual(place_dict["number_bathrooms"], place.number_bathrooms)
        self.assertEqual(place_dict["max_guest"], place.max_guest)
        self.assertEqual(place_dict["price_by_night"], place.price_by_night)
        self.assertEqual(place_dict["latitude"], place.latitude)
        self.assertEqual(place_dict["longitude"], place.longitude)
        self.assertEqual(place_dict["amenity_ids"], place.amenity_ids)
    
    def test_place_string_representation(self):
        """
        Tests the string representation of Place.
        """
        place = Place()

        place_str = str(place)

        self.assertEqual(place_str, f"[Place] ({place.id}) {place.__dict__}")
    
    def test_place_save(self):
        """
        Tests the save method of Place.
        """
        place = Place()

        place.save()

        self.assertIn(f"Place.{place.id}", storage.all())


if __name__ == "__main__":
    unittest.main()