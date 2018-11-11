# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField, RadioField
from wtforms.validators import ValidationError, DataRequired, Length,Email
from models.user import Administrators
from flask import request

__all__ = ["LoginForm", "PWDForm", "BlogTagForm"]


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


class EmailForm(FlaskForm):
    email = StringField(u'E-mail', validators=[DataRequired(),
                                           Email(message=u'邮箱格式不正确')])
    code = PasswordField(u'验证码', validators=[DataRequired()])
    remember_me = BooleanField(u'下次自动登录')
    submit = SubmitField(u'登录')

    def validate_code(self, field):
        user = Administrators.objects(email=self.email.data).first()
        if user is None:
            raise ValidationError(u'账号或者密码错误')
        elif user.verify_code(field.data) is False:
            raise ValidationError(u'验证码错误')


class MobileForm(FlaskForm):
    mobile = StringField(u'mobile', validators=[DataRequired(),
                                           Email(message=u'邮箱格式不正确')])
    code = PasswordField(u'验证码', validators=[DataRequired()])
    remember_me = BooleanField(u'下次自动登录')
    submit = SubmitField(u'登录')

    def validate_code(self, field):
        user = Administrators.objects(mobile=self.mobile.data).first()
        if user is None:
            raise ValidationError(u'账号或者密码错误')
        elif user.verify_code(field.data) is False:
            raise ValidationError(u'验证码错误')



class PWDForm(FlaskForm):
    pwd = PasswordField(u'密码')
    radio = RadioField(u'登录方式')
    submit = SubmitField(u'添加')

    def __init__(self, *args, **kwargs):
        super(PWDForm, self).__init__(*args, **kwargs)
        if kwargs:
            self.radio.choices = [(0, "password"), (1, "e-mail"), (2, "mobile")]
            if request.method =="GET":
                self.radio.data = str(kwargs.get("login_pattern").login_pattern)


#
# class LoginPatternForm(FlaskForm):
#     radio = RadioField(u'密码', choices=[(0, "password"), (1, "e-mail"), (2, "mobile")])
#     submit = SubmitField(u'修改')
#
#     def __init__(self, *args, **kwargs):
#         super(LoginPatternForm, self).__init__(*args, **kwargs)
#         if request.method == "GET":
#             if kwargs:
#                 self.radio.data = 0

class BlogTagForm(FlaskForm):
    name = StringField(u'添加Tag', validators=[DataRequired()])
    submit = SubmitField(u'添加')

    def __init__(self, *args, **kwargs):
        super(BlogTagForm, self).__init__(*args, **kwargs)
        if request.method == "GET":
            if kwargs:
                self.name.data = kwargs.get("tag").name
