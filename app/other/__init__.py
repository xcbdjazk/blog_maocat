from flask import Flask
from view import main
from config import *
from flask_mongoengine import MongoEngineSessionInterface


def current_app():
    app = Flask(__name__)
    app.config.from_object(config)
    mongo.init_app(app)
    app.register_blueprint(main.bp)
    app.session_interface = MongoEngineSessionInterface(
        mongo, collection='other_session')
    return app