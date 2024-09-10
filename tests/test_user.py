import unittest
import os

from models import storage
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Unit test class for User model"""

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

    def test_user_attributes(self):
        """
        Tests the default values of User attributes.
        """
        user = User()

        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_inherits_from_basemodel(self):
        """
        Tests that User inherits from BaseModel.
        """
        user = User()

        self.assertTrue(issubclass(type(user), BaseModel))

    def test_user_string_representation(self):
        """
        Tests the string representation of User.
        """
        user = User()

        user_str = str(user)

        self.assertEqual(user_str, f"[User] ({user.id}) {user.__dict__}")

    def test_user_to_dict(self):
        """
        Tests the to_dict method of User.
        """
        user = User()

        user.email = "example@testing.com"
        user.first_name = "John"
        user.last_name = "Doe"
        user.password = "password"
        user.save()

        user_dict = user.to_dict()

        self.assertEqual(user_dict["__class__"], "User")

        self.assertEqual(user_dict["id"], user.id)
        self.assertEqual(user_dict["created_at"], user.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"], user.updated_at.isoformat())
        self.assertEqual(user_dict["email"], user.email)
        self.assertEqual(user_dict["password"], user.password)
        self.assertEqual(user_dict["first_name"], user.first_name)
        self.assertEqual(user_dict["last_name"], user.last_name)


if __name__ == "__main__":
    unittest.main()