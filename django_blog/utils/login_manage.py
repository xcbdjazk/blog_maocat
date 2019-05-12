# -*-  coding:utf-8 -*-
from functools import wraps
from django.http import HttpResponse
from .redis_session import REDIS_CLIENT


def login_require(func):

    @wraps(func)
    def decorator(request, *args, **kwargs):
        if request.session.get('user_id') and REDIS_CLIENT.get(request.session.get('user_id')):
            # 每次訪問激活用戶的session
            REDIS_CLIENT.set(request.session['user_id'], request.session['user_id'], ex=10000)
            return func(request, *args, **kwargs)
        else:
            return HttpResponse('Unauthorized', status=401)
    return decorator

