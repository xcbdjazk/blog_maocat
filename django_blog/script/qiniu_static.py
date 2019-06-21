import os
import django
import sys
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_blog.settings")
# 工作目录添加执行环境里面
sys.path.append(os.getcwd())
django.setup()
from django.conf import settings
from utils.qiniu_conf import Config

# static_dict = {}
set_ak_sk = 'qshell account ' + Config.UEDITOR_QINIU_ACCESS_KEY + " " + Config.UEDITOR_QINIU_SECRET_KEY + ' '+ '111'
os.system(set_ak_sk)
for k, v in Config.BUCKET_CONF.items():
    static_dict = v
    path = static_dict['src_dir'] = os.path.join(settings.BASE_DIR, static_dict['src_dir'])
    static_dict['bucket'] = static_dict['name']
    path_json = os.path.join(os.path.dirname(__file__), "{}.json".format(k))

    with open(path_json, 'w') as f:
        f.write(json.dumps(static_dict, indent=4))
    os.system('qshell qupload ' + path_json)