from django import template
from django.templatetags import static
from django.conf import settings
from utils.qiniu_conf import Config
from urllib import parse
import time

register = template.Library()  # 对象名必须为register
# @register.tag(name='funcname')
# def funcname(a1,a2):
#     return a1+a2


# 解析器

import datetime


class CurrentNode(template.Node):
    def __init__(self, format):
        self.format_string = str(format)

    # 把当前时间格式化后返回
    def render(self, context):
        if settings.DEBUG:
            return static.static(self.format_string)
        else:
            url = '{}{}{}?v={}'.format(Config.BUCKET_CONF['static']['url'], Config.BUCKET_CONF['static']['key_prefix'],
                                       self.format_string, int(time.time()))
            return url


def url_for(parse, token):  # parse解析器对象，token被解析的对象，包含标签的名字和格式化的格式
    try:
        tag_name, format_string = token.split_contents()
    except:
        raise template.TemplateSyntaxError('syntax')
    return CurrentNode(format_string[1:-1])  # 传入模板中的节点类


register.tag('url_for', url_for)


# 过滤器
def percent_decimal(value):
    value = float(str(value))
    value = round(value, 3)
    value = value * 100

    return str(value) + '%'


register.filter('percent_decimal', percent_decimal)
