# -*- coding:utf8 -*-

from config import mail
from flask_mail import Message
from config import config


def send_mail(email, body="",title="邮箱登陆验证码"):
    message = Message(title, sender=config.MAIL_USERNAME, recipients=email)
    message.body = body
    mail.send(message)
