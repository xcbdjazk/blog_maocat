# -*- coding:utf8 -*-
from flask import Blueprint, send_from_directory,redirect, url_for
from utils.base_utils import tmpl
from config import config
import os
bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("")
def index():

    return redirect(url_for('blog.index'))


@bp.route('/website_uploadfile/<path:filename>')
def send_html(filename):
    # logger.debug("download file, path is %s" % filename)
    return send_from_directory(config.base_dir+'/website_uploadfile', filename, as_attachment=True)




