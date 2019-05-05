from functools import wraps
from django.http import HttpResponse


def login_require(func):

    @wraps(func)
    def decorator(request, *args, **kwargs):
        if request.session.get('user_id'):
            return func(request, *args, **kwargs)
        else:
            return HttpResponse('Unauthorized', status=401)
    return decorator

