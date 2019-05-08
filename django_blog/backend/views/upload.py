from django.http import JsonResponse
from django.shortcuts import redirect
from django.core.files.storage import default_storage
from django.views.decorators.http import require_http_methods
import os
import json
import sys
import time
import hashlib
import base64
import re
import qiniu
from io import BytesIO
from utils.login_manage import login_require
from urllib import parse
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt
from utils.qiniu_conf import Config
from utils.redis_session import session


def _random_filename(rawfilename):
    random_filename = str(time.time()) + rawfilename
    filename = hashlib.md5(random_filename.encode('utf-8')).hexdigest()
    subffix = os.path.splitext(rawfilename)[-1]
    return filename + subffix


@require_http_methods(["GET", 'POST'])
@csrf_exempt
@login_require
def upload(request):
    action = request.GET.get('action')
    result = {}
    if action == 'config':
        config_path = os.path.join(settings.BASE_DIR, 'backend', 'static', 'ueditor', 'config.json')
        result = session.get("ueditor_conf")
        if not result:
            with open(config_path, 'r', encoding='utf-8') as fp:
                result = json.loads(re.sub(r'\/\*.*\*\/', '', fp.read()))
                session.set('ueditor_conf', json.dumps(result))
        else:
            result = json.loads(str(result, encoding='utf-8'))
    elif action in ['uploadimage', 'uploadvideo', 'uploadfile']:
        image = request.FILES.get("upfile")
        filename = image.name
        save_filename = _random_filename(filename)
        if Config.UEDITOR_UPLOAD_TO_QINIU:
            q = qiniu.Auth(Config.UEDITOR_QINIU_ACCESS_KEY, Config.UEDITOR_QINIU_SECRET_KEY)
            token = q.upload_token(Config.BUCKET_CONF['upload']['name'])
            ret, info = qiniu.put_data(token, save_filename, image.read())
            if info.ok:
                result['state'] = "SUCCESS"
                result['url'] = parse.urljoin(Config.BUCKET_CONF['upload']['url'], ret['key'])
                result['title'] = ret['key']
                result['original'] = ret['key']
        else:
            img_path = default_storage.save(os.path.join(settings.BASE_DIR, 'backend', 'static', 'ueditor_image', save_filename), image)
            result['state'] = "SUCCESS"
            result['url'] = '/static/ueditor_image/' + save_filename
            result['title'] = save_filename,
            result['original'] = image.name

    elif action == 'uploadscrawl':
        base64data = request.POST.get("upfile")
        img = base64.b64decode(base64data)
        filename = _random_filename('xx.png')
        filepath = os.path.join(settings.BASE_DIR, 'backend', 'static', 'ueditor_image', filename)
        with open(filepath, 'wb') as fp:
            fp.write(img)
        result = {
            "state": "SUCCESS",
            "url": '/static/ueditor_image/' + filename,
            "title": filename,
            "original": filename
        }
    return JsonResponse(result)