from config import mongo
from flask_login import UserMixin
from mongoengine import *
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from utils.base_utils import set_6_number

class LoginPattern(mongo.DynamicDocument):
    meta = {"collection": "login_pattern"}

    class TYPE:
        password = 0
        email = 1
        mobile = 2

    login_pattern = IntField(default=TYPE.password)



class Administrators(UserMixin, mongo.DynamicDocument):
    meta = {"collection":"administrators"}

    username = StringField(requeired=True)
    mobile = StringField(max_length=11,min_length=11)
    email = StringField()
    alias_id = SequenceField()
    password_hash = StringField(requeired=True)
    create_time = DateTimeField(default=datetime.datetime.now())
    update_time = DateTimeField(default=datetime.datetime.now())
    code = StringField()
    code_over_time = DateTimeField()
    is_super = BooleanField(default=False)

    @property
    def password(self):
        return AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):

        return check_password_hash(self.password_hash, password)

    def verify_code(self, code):
        if self.code_over_time < datetime.datetime.now()-datetime.timedelta(minutes=5):
            return False
        return code == self.code

    def set_code(self):
        self.code = set_6_number()
        self.code_over_time =datetime.datetime.now()
        self.save()
        return self.code

    def edit_update_time(self):
        self.update_time = datetime.datetime.now()
        self.save()


