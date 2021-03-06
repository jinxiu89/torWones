#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-11-1.
import wtforms
import wtforms_json
from wtforms.validators import (DataRequired, Length, EqualTo, Email, ValidationError)
from wtforms_tornado import Form
from modules.passport.usersModules import User
from libs.dataBase.redis import redis
from modules.passport.localOAuthModules import LocalOAuth


class LoginForm(Form):
    """
    wtforms_json 是用于Json数据格式的验证引入的。
    1、在有JSON数据的Form 里init()它，即可解决JSON数据无法通过验证的问题
    """
    wtforms_json.init()
    name = wtforms.StringField(
        label="用户名",
        validators=[DataRequired("请输入用户名"), Length(4, 16, message="长度必须在4-16个字符之间")],
        description="用户名",
        render_kw={
            "id": "name",
            "class": "input-text size-L",
            "placeholder": "username"
        }
    )

    @staticmethod
    def validate_name(self, field):
        """
        如果用户已经有了，就不让注册
        :param self:
        :param field:
        :return:
        """
        if User.by_name(field.data) is None:
            raise ValidationError("用户没注册")

    password = wtforms.StringField(
        label="管理员密码",
        validators=[DataRequired("请输入密码")],
        description="密码",
        render_kw={
            "type": "password",
            "class": "input-text size-L",
            "id": "password",
            "autocomplete": "off",
            "placeholder": "密码"
        }
    )

    @staticmethod
    def validate_password(self, password):

        pass

    captcha = wtforms.StringField(
        validators=[DataRequired("请输入验证码")],
        description="验证码",
        render_kw={
            "id": "captcha",
            "class": "input-text size-L",
            "style": "width:140px"

        }
    )

    @staticmethod
    def validate_captcha(self, field):
        """
        通过Form自定义验证，作用是用于验证码校验
        :param self:
        :param field:
        :return:
        """
        captcha = redis.get('captcha')
        if captcha is None:
            raise ValidationError("验证码不合法！")
        elif str(redis.get('captcha'), encoding='utf-8').lower() != field.data.lower():
            raise ValidationError('验证码不正确！')

    submit = wtforms.SubmitField(
        render_kw={
            "class": "btn btn-success radius size-L button", "value": "       登      录     ",
            "type": "button"
        })
