from flask import Flask
from view import main


def current_app():
    app = Flask(__name__)
    app.register_blueprint(main.bp)
    return app