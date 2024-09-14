#! /usr/bin/python3
import unittest
import os

from models import storage
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Unit test class for State models
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
    
    def test_state_attributes(self):
        """
        Tests the default values of State attributes.
        """
        state = State()

        self.assertEqual(state.name, "")

    def test_state_inherits_from_basemodel(self):
        """
        Tests that State inherits from BaseModel.
        """
        state = State()

        self.assertTrue(issubclass(type(state), BaseModel))

    def test_state_string_representation(self):
        """
        Tests the string representation of State.
        """
        state = State()

        state.name = "Michigan"

        self.assertEqual(str(state), f"[State] ({state.id}) {state.__dict__}")

    def test_state_to_dict(self):
        """
        Tests the to_dict method of State.
        """
        state = State()

        state.name = "Michigan"

        state_dict = state.to_dict()

        self.assertEqual(state_dict["__class__"], "State")

        self.assertEqual(state_dict["id"], state.id)
        self.assertEqual(state_dict["created_at"], state.created_at.isoformat())
        self.assertEqual(state_dict["updated_at"], state.updated_at.isoformat())
        self.assertEqual(state_dict["name"], state.name)


if __name__ == "__main__":
    unittest.main()
