from flask import Blueprint, render_template as render, session,request,send_from_directory
from utils.base_utils import tmpl
from config import config

bp = Blueprint("blog", __name__, url_prefix="/blog")


@bp.route("")
def index():
    return tmpl()


