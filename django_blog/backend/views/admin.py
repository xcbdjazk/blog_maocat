# -*-  coding:utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from ..helps import rest
from django.views.decorators.http import require_http_methods
from ..models.admin import Admin
from utils.login_manage import login_require
import os
import json
import string
import sys
import time
import hashlib
import re
import qiniu
from io import BytesIO

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


UEDITOR_UPLOAD_PATH = ""
UEDITOR_UPLOAD_TO_QINIU = False
UEDITOR_QINIU_ACCESS_KEY = ""
UEDITOR_QINIU_SECRET_KEY = ""
UEDITOR_QINIU_BUCKET_NAME = ""
UEDITOR_QINIU_DOMAIN = ""

def _random_filename(rawfilename):
    random_filename = str(time.time()) + rawfilename
    filename = hashlib.md5(random_filename.encode('utf-8')).hexdigest()
    subffix = os.path.splitext(rawfilename)[-1]
    return filename + subffix


@require_http_methods(["GET", 'POST'])
@login_require
def upload(request):
    action = request.args.get('action')
    result = {}
    if action == 'config':
        config_path = os.path.join(bp.static_folder or app.static_folder, 'ueditor', 'config.json')
        with open(config_path, 'r', encoding='utf-8') as fp:
            result = json.loads(re.sub(r'\/\*.*\*\/', '', fp.read()))

    elif action in ['uploadimage', 'uploadvideo', 'uploadfile']:
        image = request.files.get("upfile")
        filename = image.filename
        save_filename = _random_filename(filename)
        result = {
            'state': '',
            'url': '',
            'title': '',
            'original': ''
        }
        if UEDITOR_UPLOAD_TO_QINIU:
            if not sys.modules.get('qiniu'):
                raise RuntimeError('没有导入qiniu模块！')
            q = qiniu.Auth(UEDITOR_QINIU_ACCESS_KEY, UEDITOR_QINIU_SECRET_KEY)
            token = q.upload_token(UEDITOR_QINIU_BUCKET_NAME)
            buffer = BytesIO()
            image.save(buffer)
            buffer.seek(0)
            ret, info = qiniu.put_data(token, save_filename, buffer.read())
            if info.ok:
                result['state'] = "SUCCESS"
                result['url'] = parse.urljoin(UEDITOR_QINIU_DOMAIN, ret['key'])
                result['title'] = ret['key']
                result['original'] = ret['key']
        else:
            image.save(os.path.join(UEDITOR_UPLOAD_PATH, save_filename))
            result['state'] = "SUCCESS"
            result['url'] = redirect('ueditor.files', filename=save_filename).url
            result['title'] = save_filename,
            result['original'] = image.filename

    elif action == 'uploadscrawl':
        base64data = request.form.get("upfile")
        img = base64.b64decode(base64data)
        filename = _random_filename('xx.png')
        filepath = os.path.join(UEDITOR_UPLOAD_PATH, filename)
        with open(filepath, 'wb') as fp:
            fp.write(img)
        result = {
            "state": "SUCCESS",
            "url": url_for('files', filename=filename),
            "title": filename,
            "original": filename
        }
    return JsonResponse(result)