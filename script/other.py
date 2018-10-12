# -*- coding:utf8 -*-
from flask_script import Command
from models.user import Administrators
from config import config
import json
import os


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
