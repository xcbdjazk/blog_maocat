# -*-  coding:utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from ..helps import rest
from django.views.decorators.http import require_http_methods
from ..models.admin import Admin
from utils.login_manage import login_require
@require_http_methods(["GET", 'POST'])
@login_require
def index(request):

    return render(request, 'article/index.html')
