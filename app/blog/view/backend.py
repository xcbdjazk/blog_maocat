# -*- coding:utf8 -*-
from flask import Blueprint, redirect, session, url_for
from flask_login import login_user, current_user, login_required,logout_user
from ..forms.blog import LoginForm, PWDForm, BlogTagForm
from models.user import Administrators
from models.blog.blog import *
from utils.base_utils import tmpl
from config import config as cf
import os
import re
import json
import os
import re
import json

from flask import Flask, request, render_template, url_for, make_response

from utils.uploader import Uploader

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
    return tmpl(form=form, admin=admin)


@bp.route("/detail", methods=["GET"])
@login_required
def backend_detail():
    return tmpl(admin=current_user)


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
    return tmpl(form=form, admin=current_user)


@bp.route("/add/tag", methods=["GET", "POST"])
@login_required
def backend_tag_add():
    form = BlogTagForm()
    if form.validate_on_submit():
        tag = TagBlog()
        tag.name = form.name.data
        tag.save()
        return "添加成功"
    return tmpl("backend/backend_pwd_edit.html",form=form, admin=current_user)


@bp.route("/add/article", methods=["GET", "POST"])
@login_required
def backend_article_add():

    return tmpl(admin=current_user)


@bp.route('/upload', methods=['GET', 'POST', 'OPTIONS'])
def upload():
    """UEditor文件上传接口

    config 配置文件
    result 返回结果
    """
    result = {}
    action = request.args.get('action')
    # 解析JSON格式的配置文件
    with open(os.path.join(cf.base_dir,"app","blog","static", 'ueditor', 'php',
                           'config.json')) as fp:
        try:
            # 删除 `/**/` 之间的注释
            CONFIG = json.loads(re.sub(r'\/\*.*\*\/', '', fp.read()))
        except:
            CONFIG = {}

    if action == 'config':
        # 初始化时，返回配置文件给客户端
        result = CONFIG

    elif action in ('uploadimage', 'uploadfile', 'uploadvideo'):
        # 图片、文件、视频上传
        if action == 'uploadimage':
            fieldName = CONFIG.get('imageFieldName')
            config = {
                "pathFormat": CONFIG['imagePathFormat'],
                "maxSize": CONFIG['imageMaxSize'],
                "allowFiles": CONFIG['imageAllowFiles']
            }
        elif action == 'uploadvideo':
            fieldName = CONFIG.get('videoFieldName')
            config = {
                "pathFormat": CONFIG['videoPathFormat'],
                "maxSize": CONFIG['videoMaxSize'],
                "allowFiles": CONFIG['videoAllowFiles']
            }
        else:
            fieldName = CONFIG.get('fileFieldName')
            config = {
                "pathFormat": CONFIG['filePathFormat'],
                "maxSize": CONFIG['fileMaxSize'],
                "allowFiles": CONFIG['fileAllowFiles']
            }

        if fieldName in request.files:
            field = request.files[fieldName]
            uploader = Uploader(field, config, cf.base_dir+"/website_uploadfile")
            result = uploader.getFileInfo()
        else:
            result['state'] = '上传接口出错'

    elif action in ('uploadscrawl'):
        # 涂鸦上传
        fieldName = CONFIG.get('scrawlFieldName')
        config = {
            "pathFormat": CONFIG.get('scrawlPathFormat'),
            "maxSize": CONFIG.get('scrawlMaxSize'),
            "allowFiles": CONFIG.get('scrawlAllowFiles'),
            "oriName": "scrawl.png"
        }
        if fieldName in request.form:
            field = request.form[fieldName]
            uploader = Uploader(field, config, cf.base_dir+"/app"+"/blog"+"/static")
            result = uploader.getFileInfo()
        else:
            result['state'] = '上传接口出错'

    elif action in ('catchimage'):
        config = {
            "pathFormat": CONFIG['catcherPathFormat'],
            "maxSize": CONFIG['catcherMaxSize'],
            "allowFiles": CONFIG['catcherAllowFiles'],
            "oriName": "remote.png"
        }
        fieldName = CONFIG['catcherFieldName']

        if fieldName in request.form:
            # 这里比较奇怪，远程抓图提交的表单名称不是这个
            source = []
        elif '%s[]' % fieldName in request.form:
            # 而是这个
            source = request.form.getlist('%s[]' % fieldName)

        _list = []
        for imgurl in source:
            uploader = Uploader(imgurl, config, cf.base_dir+"/app"+"/blog"+"/static", 'remote')
            info = uploader.getFileInfo()
            _list.append({
                'state': info['state'],
                'url': info['url'],
                'original': info['original'],
                'source': imgurl,
            })

        result['state'] = 'SUCCESS' if len(_list) > 0 else 'ERROR'
        result['list'] = _list

    else:
        result['state'] = '请求地址出错'

    result = json.dumps(result)

    if 'callback' in request.args:
        callback = request.args.get('callback')
        if re.match(r'^[\w_]+$', callback):
            return '%s(%s)' % (callback, result)
        return json.dumps({'state': 'callback参数不合法'})

    res = make_response(result)
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Headers'] = 'X-Requested-With,X_Requested_With'
    return res







