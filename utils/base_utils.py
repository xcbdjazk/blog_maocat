from flask import request,render_template


def tmpl(*name_or_list, **context):
    if name_or_list:
        template = name_or_list[0]
    else:
        endpoint = request.endpoint.split(".")
        template = [
            '/'.join(endpoint[x:]) + '.html' for x in range(len(endpoint))
            ]
    return render_template(template, **context)