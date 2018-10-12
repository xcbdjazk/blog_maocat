from flask import Blueprint, render_template as render
from flask_login import login_user
bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("")
def index():
    return render("backend_home.html")
