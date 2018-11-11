from flask import request, render_template
import random


def tmpl(*name_or_list, **context):
    if name_or_list:
        template = name_or_list[0]
    else:
        endpoint = request.endpoint.split(".")
        template = [
            '/'.join(endpoint[x:]) + '.html' for x in range(len(endpoint))
            ]
    return render_template(template, **context)


def set_6_number():
    return str(random.randrange(0, 1000000)).zfill(6)

