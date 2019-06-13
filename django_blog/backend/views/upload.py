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
    result ={}
    image = request.FILES.get('editormd-image-file')
    filename = image.name
    save_filename = _random_filename(filename)
    if Config.UEDITOR_UPLOAD_TO_QINIU:
        q = qiniu.Auth(Config.UEDITOR_QINIU_ACCESS_KEY, Config.UEDITOR_QINIU_SECRET_KEY)
        token = q.upload_token(Config.BUCKET_CONF['upload']['name'])
        ret, info = qiniu.put_data(token, save_filename, image.read())
        if info.ok:
            result['success'] = 1
            result['url'] = parse.urljoin(Config.BUCKET_CONF['upload']['url'], ret['key'])
            result['message'] = 'ok',
    else:
        img_path = default_storage.save(os.path.join(settings.BASE_DIR, 'backend', 'static', 'ueditor_image', save_filename), image)
        result['success'] = 1
        result['url'] = 'http://' + request.get_host() + '/static/ueditor_image/' + save_filename
        result['message'] = 'ok',
    return JsonResponse(result)