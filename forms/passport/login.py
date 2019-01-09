#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-11-1.
import wtforms
from wtforms.validators import DataRequired
from wtforms_tornado import Form


class LoginForm(Form):
    name = wtforms.StringField(
        label="用户名",
        validators=[DataRequired("请输入用户名")],
        description="用户名",
        render_kw={
            "id": "name",
            "class": "input-text size-L",
            "placeholder": "username"
        }
    )
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
    captcha = wtforms.StringField(
        validators=[DataRequired("请输入验证码")],
        description="验证码",
        render_kw={
            "id": "captcha",
            "class": "input-text size-L",
            "style": "width:140px"

        }
    )
    submit = wtforms.SubmitField(
        render_kw={
            "class": "btn btn-success radius size-L button", "value": "       登      录     ",
            "type": "button"
        })
