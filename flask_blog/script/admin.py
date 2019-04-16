# -*- coding:utf8 -*-
from flask_script import Command
from flask_script import Manager
from models.user import Administrators
from config import config
import json
import os
import re
from config.ext import sub_null_manager

admin_manager = Manager(sub_null_manager)


class CreateAdministrators(Command):
    def run(self):
        admin = Administrators.objects(username="admin", mobile="17802927387").first()
        if admin:
            print("----  superuser is exist  -----")
        else:
            admin = Administrators(username="admin", mobile="17802927387")
            admin.is_super = True
            with open(os.path.join(config.base_dir, "utils", "my.json"), "r", ) as f:
                pwd = json.load(f)[0]
                print("----pwd:", pwd, "-----")
                admin.password = pwd
            admin.save()


@admin_manager.option("-u", "--username", dest="username")
@admin_manager.option("-m", "--mobile", dest="mobile")
@admin_manager.option("-p", "--password", dest="password")
@admin_manager.option("-e", "--email", dest="email")
def admin(username, mobile, password, email):
    pattern = "^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$"
    if not re.match(pattern, email, flags=0):
        print("email : pattern error")
    if len(username) < 5 or len(mobile) != 11 or len(password) < 6:
        print "error :you param  wrong;"
        print "username : len gte 5"
        print "mobile : len is 11"
        print "password : len gte 6"

    else:
        admin = Administrators.objects(username=username, mobile=mobile, email=email).first()
        if admin:
            admin.password = password
            message = u"update admin password Success \nusername:{}\nmobile:{}".format(username, mobile)
        else:
            admin_username = Administrators.objects(username=username).first()
            message = u""
            if admin_username:
                message += u"username: admin exist  \n"
            admin_mobile = Administrators.objects(mobile=mobile).first()
            if admin_mobile:
                message += u"mobile: admin exist  \n"
            admin_email = Administrators.objects(email=email).first()
            if admin_email:
                message += u"mobile: email exist  \n"
            if message:
                return message
            admin = Administrators(username=username, mobile=mobile, password=password,email=email)
            message = u"create admin Success \nusername:{}\nmobile:{}\nmobile:{}".format(username, mobile,email)

        admin.save()
        print message
