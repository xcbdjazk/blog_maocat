# -*- coding:utf8 -*-
from flask_script import Command
from flask_script import Manager
from models.user import Administrators
from config import config
import json
import os
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
            with open(os.path.join(config.base_dir, "utils", "my.json"), "r",) as f:
                pwd = json.load(f)[0]
                print("----pwd:", pwd, "-----")
                admin.password = pwd
            admin.save()


@admin_manager.option("-u","--username",dest="username")
@admin_manager.option("-m","--mobile",dest="mobile")
@admin_manager.option("-p","--password",dest="password")
def admin(username,mobile,password):
    if len(username) <5 or len(mobile) !=11 or len(password)<6:
        print "error :you param  wrong;"
        print "username : len gt 5"
        print "mobile : len is 11"
        print "password : len gt 6"

    else:
        admin = Administrators.objects(username=username, mobile=mobile).first()
        if admin:
            admin.password = password
        else:
            admin = Administrators(username=username, mobile=mobile,password = password)

        admin.save()
        print "create admin Success"
