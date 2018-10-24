# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Length
from models.user import Administrators
from flask import request

__all__ = ["LoginForm"]


class LoginForm(FlaskForm):
    mobile = StringField(u'手机', validators=[DataRequired(),
                                            Length(11, message=u'手机号11位')])
    pwd = PasswordField(u'密码', validators=[DataRequired()])
    remember_me = BooleanField(u'下次自动登录')
    submit = SubmitField(u'登录')

    def validate_pwd(self, field):
        user = Administrators.objects(mobile=self.mobile.data).first()
        if user is None:
            raise ValidationError(u'账号或者密码错误')
        elif user.verify_password(field.data) is False:
            raise ValidationError(u'账号或者密码错误')


class PWDForm(FlaskForm):
    pwd = PasswordField(u'密码', validators=[DataRequired()])
    submit = SubmitField(u'修改')


class BlogTagForm(FlaskForm):
    name = StringField(u'添加Tag', validators=[DataRequired()])
    submit = SubmitField(u'添加')


    def __init__(self,*args,**kwargs):
        super(BlogTagForm, self).__init__(*args,**kwargs)
        if request.method == "GET":
            if kwargs:
                self.name.data = kwargs.get("tag").name
