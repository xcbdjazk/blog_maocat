from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
import re
from django.shortcuts import redirect
from ..helps import rest
from django.views.decorators.http import require_http_methods
from ..models.admin import Admin
from ..models.article import Article
from utils.login_manage import login_require
from ..models.article import Tag


@require_http_methods(["GET", 'POST'])
@login_require
def edit_user(request):
    user = request.user
    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.title = request.POST.get('title')
        user.desc = request.POST.get('desc')
        user.save()
        return rest.success('修改成功')
    content = dict(
        user=user
    )
    return render(request, 'user/edit_user.html', content)