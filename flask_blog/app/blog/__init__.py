# -*- coding:utf8 -*-
from flask import Flask
from view import main
from view import backend
from view import blog
from config import *
from flask_mongoengine import MongoEngineSessionInterface
from models.user import Administrators
from utils.register_admin_autoinit import register_endpoint


def current_app():
    app = Flask(__name__)
    app.config.from_object(config)

    mongo.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)

    @login_manager.user_loader
    def load_user(userid):
        return Administrators.objects.get(id=userid)

    login_manager.init_app(app)
    app.register_blueprint(main.bp)
    app.register_blueprint(blog.bp)
    app.register_blueprint(backend.bp)
    register_endpoint(app)
    app.session_interface = MongoEngineSessionInterface(
        mongo, collection='blog_session')
    return app