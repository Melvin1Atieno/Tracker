from flask_api import FlaskAPI

from flask import jsonify, request, make_response

from config import app_config

from werkzeug.security import generate_password_hash, check_password_hash

from models import User



users_catalog = [
    {
        "username": "melvin",
        "email": "mel@example.com",
        "password":"12345"
    },
    {
        "username": "mel",
        "email": "me@example.com",
        "password": "123"
    }
]



def create_app(config_name):
    app = FlaskAPI(__name__)
    app.config.from_object(app_config["development"])
    app.config.from_envvar("APP_SETTINGS")



        # import pdb; pdb.set_trace()
    @app.route("/api/v1/users", methods=["POST"])
    def create_user():
        data = request.get_json()
        hashed_password = generate_password_hash(data.get("password"), method="sha256")


        if not data.get("username"):
            return make_response(jsonify({"message": "Username not provided"}),400)
        if not data.get("email"):
            return make_response(jsonify({"message": "Email not provided"}),400)
        if not data.get("password"):
            return make_response(jsonify({"message": "Password not provided"}),400)
        if data.get("username") == " ":
            return make_response(jsonify({"message": "Username field cannot be empty"}),400)
        if data.get("email") == " ":
            return make_response(jsonify({"message": "Email field cannot be empty"}),400)
        if data.get("password") == " ":
            return make_response(jsonify({"message": "Password field cannot be empty"}),400)
        if "@" and ".com" not in data.get("email"):
            return make_response(jsonify({"message":"Invalid email"}),400)


        username = data.get("username")
        email = data.get("email")
        password = hashed_password
        for user in users_catalog:
            if user["username"] == username:
                return make_response(jsonify({"message": "Username already taken"}),400)
            if user["email"] == email:
                return make_response(jsonify({"message": "Email already registered to a user"}),400)
        
        new_user = User(username,email,password)
        users_catalog.append({"username":new_user.username,"email":new_user.email,"password":new_user.password})
        return make_response(jsonify({"message": "Registration Successful"}),201)
        
        
    return app
