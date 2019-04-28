import os
import django
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_blog.settings")
# 工作目录添加执行环境里面
sys.path.append(os.getcwd())
django.setup()

from backend.models.admin import Admin

print('add admin:1 ,edit admin:2')
option = input("choice:")
if option == '1':
    if Admin.objects.all():
        print('Admin exist')
    else:
        name = input("name:").strip()
        password = input("password:").strip()

        def verify(name, password):
            if 4 < len(name) < 6 and 4 < len(password) < 12:
                return True
            print('name or pwd length error')
            return False

        if verify(name, password):
            admin = Admin()
            admin.name = name
            admin.password = password
            admin.save()
elif option == '2':
    admin = Admin.objects.first()
    if not admin:
        print('please add Admin')
    else:
        name = input("name:").strip()
        password = input("password:").strip()
        admin.username = name
        admin.password = password
        admin.save()