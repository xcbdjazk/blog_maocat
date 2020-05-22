from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
import re
from django.shortcuts import redirect
from ..helps import rest
from django.views.decorators.http import require_http_methods
from ..models.article import ImagesModel
from utils.login_manage import login_require
from ..models.article import Tag
from django.views.decorators.csrf import csrf_exempt
from utils.qiniu_conf import Config
import time
import hashlib
import qiniu
import os
from urllib import parse
from django.conf import settings
from django.core.files.storage import default_storage


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


def _random_filename(rawfilename):
    random_filename = str(time.time()) + rawfilename
    filename = hashlib.md5(random_filename.encode('utf-8')).hexdigest()
    subffix = os.path.splitext(rawfilename)[-1]
    return filename + subffix


@require_http_methods(["GET", 'POST'])
@login_require
@csrf_exempt
def add_images(request):
    if request.method == 'POST':
        result = {}

        images = request.FILES.getlist('file')
        urls = []
        for image in images:
            filename = image.name
            save_filename = _random_filename(filename)
            if Config.UEDITOR_UPLOAD_TO_QINIU:
                q = qiniu.Auth(Config.UEDITOR_QINIU_ACCESS_KEY, Config.UEDITOR_QINIU_SECRET_KEY)
                token = q.upload_token(Config.BUCKET_CONF['upload']['name'])
                ret, info = qiniu.put_data(token, save_filename, image.read())
                if info.ok:
                    url = parse.urljoin(Config.BUCKET_CONF['upload']['url'], ret['key'])
                    urls.append(url)
                    img = ImagesModel()
                    img.url = url
                    img.save()
            else:
                img_path = default_storage.save(
                    os.path.join(settings.BASE_DIR, 'backend', 'static', 'ueditor_image', save_filename), image)
                url = 'http://' + request.get_host() + '/static/ueditor_image/' + save_filename
                urls.append(url)
                img = ImagesModel()
                img.url = url
                img.save()
        return rest.success('添加成功', data={"urls": urls})

    images = ImagesModel.objects.all()
    content = dict(
        images=images
    )

    return render(request, 'user/add_images.html', content)
