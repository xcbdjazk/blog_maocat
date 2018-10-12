# -*- coding:utf-8 -*-
from flask_mongoengine import MongoEngine
from conf import Config
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
config = Config
mongo = MongoEngine()
bootstrap = Bootstrap()
login_manager = LoginManager()

