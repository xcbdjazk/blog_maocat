# -*- coding:utf8 -*-
import os


class Config(object):
    DEBUG = True
    SECRET_KEY = "JWKY"
    base_dir = os.path.dirname(os.path.dirname(__file__))
    # 关系数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://dbuser:Changeme_123@postgres/blog'

    # mongoDB
    MONGODB_DB = 'blog'
    MONGODB_HOST = 'mongo'
    MONGODB_PORT = 27017

    # redis
    REDIS_HOST = 'redis'
    REDIS_SOCKETIO = 'redis://{0}:6379/{1}'.format(REDIS_HOST, 0)

    # endprint
    endpoint = ["bootstrap", "static"]

    # 电子邮件服务器的主机名或IP地址
    MAIL_SERVER = "smtp.163.com"
    # 电子邮件服务器的端口
    MAIL_PORT = "465"
    # 启用传输层安全协议
    # MAIL_USE_TLS = ""
    # 启用安全套接层协议(不同协议端口不一样)
    MAIL_USE_SSL = True
    # 邮件账户的用户名
    MAIL_USERNAME = "zk246422@163.com"
    # 邮件账户的密码
    MAIL_PASSWORD = ""



