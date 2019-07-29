    # -*-  coding:utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from ..helps import rest
from django.views.decorators.http import require_http_methods
from ..models.admin import Admin
from ..models.article import Article
from utils.login_manage import login_require
from utils.redis_session import REDIS_CLIENT

@require_http_methods(["GET", 'POST'])
# @login_require
def home(request):
    if request.session.get("user_id") and REDIS_CLIENT.get(request.session.get("user_id")):
        return redirect('index')
    if request.method == 'POST':
        # loggin user
        admin = Admin.objects.filter(username=request.POST.get('username')).order_by('create_time').last()
        if admin and admin.verify_password(request.POST.get('password')):
            request.session['user_id'] = admin.aid
            REDIS_CLIENT.set(request.session['user_id'], request.session['user_id'], ex=10000)
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
    articles = Article.objects.order_by('id').all()
    # for i in articles:
    #     print(i.tag.all())
    content = dict(
        articles=articles,
    )
    return render(request, 'admin/index.html', content)

