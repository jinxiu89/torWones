#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {19-3-20}.
import wtforms
import wtforms_json
from wtforms.validators import (DataRequired, Length, EqualTo, Email, ValidationError)
from wtforms_tornado import Form
from libs.dataBase.redis import redis
from modules.passport.usersModules import User


class SignUpForm(Form):
    wtforms_json.init()
    name = wtforms.StringField(
        label="用户名",
        validators=[DataRequired("请输入用户名"), ],
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
        if User.by_name(field.data) is not None:
            raise ValidationError("该用户已经有人注册")

    password = wtforms.StringField(
        label="密码",
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
    confirmation = wtforms.StringField(
        label="确认密码",
        validators=[DataRequired("请重输密码"), EqualTo("password", message="两次密码输入不一致")],
        description="重复输入密码",
        render_kw={
            "type": "password",
            "class": "input-text size-L",
            "id": "password",
            "autocomplete": "off",
            "placeholder": "密码"
        }
    )
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
    def validate_captcha(field):
        """
        通过Form自定义验证，作用是用于验证码校验
        :param field:
        :return:
        """
        captcha = redis.get('captcha')
        if captcha is None:
            raise ValidationError("验证码不合法！")
        elif str(redis.get('captcha'), encoding='utf-8').lower() != field.data.lower():
            raise ValidationError('验证码不正确！')
