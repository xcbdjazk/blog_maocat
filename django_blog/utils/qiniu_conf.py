from django.conf import settings


# UEDITOR_UPLOAD_PATH = ""


class Config(object):
    # UEDITOR_UPLOAD_TO_QINIU = settings.DEBUG
    UEDITOR_UPLOAD_TO_QINIU = not settings.DEBUG
    UEDITOR_QINIU_ACCESS_KEY = ""
    UEDITOR_QINIU_SECRET_KEY = ""

    # {
    #     'name':'BUCKET_NAME',
    #     'url':'DOMAIN',
    # }
    # qshell doc:--- > https://github.com/qiniu/qshell/blob/master/docs/qupload.md
    BUCKET_CONF = {
        'static': {
            'name': 'static',
            'access_key': UEDITOR_QINIU_ACCESS_KEY,
            'secret_key': UEDITOR_QINIU_SECRET_KEY,
            'key_prefix': 'backend/',
            'src_dir': 'backend/static',
            'url': 'http://static.maocatooo.cn/',
        },
        'upload': {
            'name': 'blog',
            'key_prefix': 'upload/',
            # 'src_dir': 'upload/',
            'url': 'http://upload.maocatooo.cn/',
        }
    }
