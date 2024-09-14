#! /usr/bin/python3

import unittest
import os

from models import storage
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    """
    Unit test class for Review
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
    
    def test_review_attributes(self):
        """
        Tests the default values of Review attributes.
        """
        review = Review()

        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
    
    def test_review_inherits_from_basemodel(self):
        """
        Tests that Review inherits from BaseModel.
        """
        review = Review()

        self.assertTrue(issubclass(type(review), BaseModel))
    
    def test_review_string_representation(self):
        """
        Tests the string representation of Review.
        """
        review = Review()

        self.assertEqual(str(review), f"[Review] ({review.id}) {review.__dict__}")
    
    def test_review_to_dict(self):
        """
        Tests the to_dict method of Review.
        """
        review = Review()
        review.place_id = "123"
        review.user_id = "456"
        review.text = "This place is great!"

        review_dict = review.to_dict()

        self.assertEqual(type(review_dict), dict)
        self.assertEqual(review_dict["place_id"], "123")
        self.assertEqual(review_dict["user_id"], "456")
        self.assertEqual(review_dict["text"], "This place is great!")

    def test_review_save(self):
        """
        Tests the save method of Review.
        """
        review = Review()

        review.save()

        all_objects = storage.all()

        self.assertIn(review, all_objects.values())


if __name__ == "__main__":
    unittest.main()