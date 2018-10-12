# -*- coding:utf8 -*-
from flask import Blueprint, redirect, session, url_for
from flask_login import login_user, current_user, login_required,logout_user
from ..forms.blog import LoginForm,PWDForm
from models.user import Administrators
from utils.base_utils import tmpl

bp = Blueprint("backend", __name__, url_prefix="/backend")


@bp.route("", methods=["GET", "POST"])
def backend_home():
    if current_user.is_authenticated:
        return redirect(url_for("backend.backend_detail"))
    form = LoginForm()
    admin = Administrators.objects(mobile=form.mobile.data).first()
    if form.validate_on_submit():
        login_user(admin, form.remember_me.data)
        return redirect(url_for("backend.backend_detail"))
    return tmpl(form=form)


@bp.route("/detail", methods=["GET"])
@login_required
def backend_detail():
    return tmpl()



@bp.route("/logout", methods=["GET"])
@login_required
def backend_logout():
    logout_user()
    return redirect(url_for("backend.backend_home"))


@bp.route("/pwd/edit", methods=["GET", "POST"])
@login_required
def backend_pwd_edit():
    form = PWDForm()
    if form.validate_on_submit():
        admin = Administrators.objects.get(id=current_user.id)
        admin.password = form.pwd.data
        admin.save()
        return "修改成功"
    return tmpl(form=form)


