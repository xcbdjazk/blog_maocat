# -*- coding:utf8 -*-
from flask import Blueprint, render_template as render, session,request
from utils.base_utils import tmpl

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("")
def index():
    return tmpl()




