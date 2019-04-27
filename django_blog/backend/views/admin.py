from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from ..models.admin import Admin
from django.core import serializers
import requests
import json


@require_http_methods(["GET"])
def home(request):
    response = {"a":1}
    # 1 第1种方式 插入数据
    # admin = Admin.objects
    # admin.name='zk'
    # admin.password = "123"
    # admin.create()
    # 2 第二种方式
    # admin = Admin()
    # admin.name = 'zk'
    # admin.password = "123"
    # admin.save()
    admin = Admin.objects.order_by('create_time').last()
    print(admin.verify_password('123'))
    return JsonResponse(response)