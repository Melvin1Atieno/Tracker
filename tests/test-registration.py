import unittest
import os
import json
from app import create_app


class UserRegistrationTestCase(unittest.TestCase):
    """Test cases for user registration"""

    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.data = {
            "username": "melvin",
            "email": "email@gmail.com",
            "password": "12345"
        }

    def test_new_user_registeration(self):
        """Test that a user can register if they provide details"""
        register = self.client.post("api/v1/users", data=json.dumps(dict(username="newuser", email="newuser@gmail.com", password="1234")),
                                    content_type=("application/json"))
        self.assertEqual(register.status_code, 201)
        response = json.loads(register.data.decode())
        self.assertEqual(response["message"], "Registration Successful")
                                     

    def test_user_registration_without_username(self):
        """Test for appropriate response message for registration without username"""
        register = self.client.post("api/v1/users", data=json.dumps(dict(email="person@gmail", password="12345")),
                                    content_type=("application/json")
                                    )
        response = json.loads(register.data.decode())
        self.assertEqual(response["message"], "Username not provided")
        self.assertEqual(register.status_code, 400)

    def test_user_registration_with_empty_string_username(self):
        """Test for appropriate response message for registration with empty string username"""
        register = self.client.post("api/v1/users", data=json.dumps(dict(username=" ", email="example@gmail", password="1234")),
                                    content_type=("application/json"))
        response = json.loads(register.data.decode())
        self.assertEqual(response["message"], "Username field cannot be empty")
        self.assertEqual(register.status_code,400)

    def test_user_registration_without_email(self):
        """Test reponse message for user registration without email"""
        register = self.client.post("api/v1/users", data=json.dumps(dict(username="example", password="1234")),
                                    content_type=("application/json"))
        response = json.loads(register.data.decode())
        self.assertEqual(response["message"], "Email not provided")
        self.assertEqual(register.status_code, 400)

    def test_user_registration_with_empty_string_email(self):
        """Test for appropriate response message for empty string email registration"""
        register = self.client.post("api/v1/users", data=json.dumps(dict(username="example", email=" ", password="12345")),
                                    content_type=("application/json"))
        response = json.loads(register.data.decode())
        self.assertEqual(response["message"], "Email field cannot be empty")

    def test_user_registration_without_password(self):
        """Test for appropriate response message for registration without password"""
        register = self.client.post("api/v1/users", data=json.dumps(dict(username="another", email="another@gmail")),
                                    content_type=("application/json"))
        response = json.loads(register.data.decode())
        self.assertEqual(response["message"], "Password not provided")
        self.assertEqual(register.status_code, 400)

    def test_user_registration_with_empty_string_password(self):
        """Test for approprate response for user registration with empty string password"""
        register = self.client.post("api/v1/users", data=json.dumps(dict(username="example", email="example@gmail", password=" ")),
                                    content_type=("application/json"))
        response = json.loads(register.data.decode())
        self.assertEqual(response["message"], "Password field cannot be empty")
        self.assertEqual(register.status_code, 400)

    def test_user_registration_with_existing_username(self):
        """Test for user registration with already existing username"""
        register = self.client.post("api/v1/users", data=json.dumps(self.data),
                                    content_type=("application/json"))
        register_two = self.client.post("api/v1/users", data=json.dumps(dict(username="melvin", email="differnt@gmail.com", password="1234")),
                                        content_type=("application/json"))
        response = json.loads(register_two.data.decode())
        self.assertEqual(response["message"], "Username already taken")
        self.assertEqual(register_two.status_code, 400)

    def test_user_registration_with_existing_email(self):
        """Test response message for registration with already existing email"""
        register = self.client.post("api/v1/users", data=json.dumps(dict(username="name", email="email@gmail.com", password="1234")),
                                    content_type=("application/json"))
        register_two = self.client.post("api/v1/users", data=json.dumps(dict(username="different name", email="email@gmail.com", password="1234")),
                                        content_type=("application/json"))
        response = json.loads(register_two.data.decode())
        self.assertEqual(response["message"],
                         "Email already registered to a user")
        self.assertEqual(register_two.status_code, 400)

    def test_user_registration_with_invalid_email(self):
        """test response message for registration with invalid email"""
        register = self.client.post("api/v1/users", data=json.dumps(dict(username="name", email="email", password="1234")),
                                    content_type=("application/json"))
        response = json.loads(register.data.decode())
        self.assertEqual(response["message"], "Invalid email")
        self.assertEqual(register.status_code, 400)

        if __name__ == "__main__":
            unittest.main()
