import unittest
import os
import json
from app import create_app


class UserLoginTestcase(unittest.TestCase):
    """test user login"""
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.register_user = self.client.post("api/v1/users", data=json.dumps(dict(username="mary",
                                              email="mary@gmail.com", password="1234")),
                                               content_type=("application/json"))
                                
    def test_user_login(self):
        """test user can successfully login"""
        login = self.client.post("api/v1/users/auth", data=json.dumps(dict(username="mary",
                                                       password="1234")), content_type=("application/json"))
        response = json.loads(login.data.decode())
        self.assertEqual(response["message"], "login successful")
        self.assertEqual(login.status_code, 200)
    
    def test_user_login_with_invalid_username(self):
        """test user cannot login with wrong username"""
        login = self.client.post("api/v1/users/auth", data=json.dumps(dict(username="noname",
                                    password="1234")),content_type=("application/json"))
        response = json.loads(login.data.decode())
        self.assertEqual(response["message"], "Invalid username")
        self.assertEqual(login.status_code, 401)
    
    def test_user_registration_with_invalid_password(self):
        """test user cannot login with wrong password"""
        login = self.client.post("api/v1/users/auth", data=json.dumps(dict(username="mary",
                                    password="wrongpasswor")), content_type=("application/json"))
        response = json.loads(login.data.decode())
        self.assertEqual(response["message"], "Incorrect password")
        self.assertEqual(login.status_code, 401)

