from django.conf import settings

# UEDITOR_UPLOAD_PATH = ""


class Config(object):
    UEDITOR_UPLOAD_TO_QINIU = settings.DEBUG
    # UEDITOR_UPLOAD_TO_QINIU = not settings.DEBUG
    UEDITOR_QINIU_ACCESS_KEY = ""
    UEDITOR_QINIU_SECRET_KEY = ""
    # UEDITOR_QINIU_BUCKET_NAME = ""
    # UEDITOR_QINIU_DOMAIN = ""
    # {
    #     'name':'BUCKET_NAME',
    #     'url':'DOMAIN',
    # }
    BUCKET_CONF = {
        'static':{
            'name':'static',
            'url':'http://static.maocatooo.cn/',
        },
        'upload':{
            'name':'blog',
            'url':'http://upload.maocatooo.cn/',
        }
    }