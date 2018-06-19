from flask_api import FlaskAPI

from flask import jsonify

from config import app_config






def create_app(config_name):
    app = FlaskAPI(__name__)
    app.config.from_object(app_config["development"])
    app.config.from_envvar("APP_SETTINGS")

    return app
