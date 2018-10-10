# -*- coding:utf8 -*-


class Config(object):
    DEBUG = True
    SECRET_KEY = "JWKY"

    # 关系数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://dbuser:Changeme_123@postgres/test'

    # mongoDB
    MONGODB_DB = 'blog'
    MONGODB_HOST = 'mongo'
    MONGODB_PORT = 27017

    # redis
    REDIS_HOST = 'redis'
    REDIS_SOCKETIO = 'redis://{0}:6379/{1}'.format(REDIS_HOST, 0)