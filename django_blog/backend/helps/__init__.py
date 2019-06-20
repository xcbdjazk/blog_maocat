from utils.qiniu_conf import Config
def global_params(request):
    return {
        'qiniu_url': Config.BUCKET_CONF.get('static').get('url')+Config.BUCKET_CONF.get('static').get('key_prefix'),
        'ad_list': 2,
        'archive_list': 3
    }