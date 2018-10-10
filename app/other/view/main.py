from flask import Blueprint, render_template as render

bp = Blueprint("main", __name__, url_prefix="/other")

@bp.route("")
def index():
    return render("index.html")
