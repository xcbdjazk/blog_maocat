# -*-  coding:utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from ..helps import rest
from django.views.decorators.http import require_http_methods
from ..models.admin import Admin
from utils.login_manage import login_require


@require_http_methods(["GET", 'POST'])
# @login_require
def home(request):
    if request.session.get("user_id"):
        return redirect('index')
    if request.method == 'POST':
        # loggin user
        admin = Admin.objects.filter(username=request.POST.get('username')).order_by('create_time').last()
        if admin and admin.verify_password(request.POST.get('password')):
            request.session['user_id'] = admin.aid
            return rest.success("登录成功", data={
                "url": redirect('index').url
            })
        return rest.params_error('帐号密码错误')
    # request.session['1']= 123
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
    # admin = Admin.objects.order_by('create_time').last()
    # print(admin.verify_password('123'))
    return render(request, 'admin/home.html')


@require_http_methods(["GET", 'POST'])
@login_require
def index(request):

    return render(request, 'admin/index.html')

