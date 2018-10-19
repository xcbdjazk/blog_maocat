# -*- coding:utf8 -*-
from flask import Blueprint, render_template as render, session,request,send_from_directory
from utils.base_utils import tmpl
from config import config

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("")
def index():
    return tmpl()


@bp.route('/website_uploadfile/<path:filename>')
def send_html(filename):
    # logger.debug("download file, path is %s" % filename)
    print(filename)
    print(config.base_dir)
    return send_from_directory(config.base_dir+'/website_uploadfile', filename, as_attachment=True)




