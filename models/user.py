from config import mongo
from flask_login import UserMixin
from mongoengine import *
from werkzeug.security import generate_password_hash, check_password_hash
import datetime


class Administrators(UserMixin, mongo.DynamicDocument):
    meta = {"collection":"administrators"}
    username = StringField(requeired=True)
    mobile = StringField(max_length=11,min_length=11)
    alias_id = SequenceField()
    password_hash = StringField(requeired=True)
    create_time = DateTimeField(default=datetime.datetime.now())
    update_time = DateTimeField(default=datetime.datetime.now())
    is_super = BooleanField(default=False)

    @property
    def password(self):
        return AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):

        return check_password_hash(self.password_hash, password)

    def edit_update_time(self):
        self.update_time = datetime.datetime.now()
        self.save()


