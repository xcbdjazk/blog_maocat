# -*- coding:utf8 -*-
from flask import Blueprint, request
from utils.base_utils import tmpl
from config import config
import jieba

bp = Blueprint("blog", __name__, url_prefix="/blog")


@bp.route("")
def index():
    seg = list(jieba.cut("第1111"))
    key = seg if len(seg) <= 2 else [i for i in seg if len(i) != 1]

    return tmpl()


