from django import template


register=template.Library() #对象名必须为register
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
        now = datetime.datetime.now()
        return self.format_string


def funcname(parse, token):  # parse解析器对象，token被解析的对象，包含标签的名字和格式化的格式
    try:
        tag_name, format_string = token.split_contents()
        print(tag_name)
        print(format_string)
    except:
        raise template.TemplateSyntaxError('syntax')
    return CurrentNode(format_string[1:-1])  # 传入模板中的节点类

register.tag('funcname', funcname)


def percent_decimal(value):
    value = float(str(value))
    value = round(value, 3)
    value = value * 100

    return str(value) + '%'


register.filter('percent_decimal', percent_decimal)