#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-12-8.
import wtforms
import wtforms_json
from wtforms.validators import DataRequired
from wtforms_tornado import Form


class UsersForm(Form):
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


class EditForm(Form):
    wtforms_json.init()
    name = wtforms.StringField(
        label="用户名",
        validators=[DataRequired("请输入用户名")],
        description="用户名",
        render_kw={
            "id": "name",
            "class": "input-text size-L",
            "placeholder": "name"
        }
    )
    nickname = wtforms.StringField(
        label="昵称",
        validators=[DataRequired("请输入昵称")],
        description="昵称",
        render_kw={
            "id": "nickname",
            "class": "input-text size-L",
            "placeholder": "nickname"
        }
    )
    email = wtforms.StringField(
        label="email",
        validators=[],
        description="email",
        render_kw={
            "id": "email",
            "class": "input-text size-L",
            "placeholder": "email"
        }
    )
    mobile = wtforms.StringField(
        label="电话",
        validators=[],
        description="电话",
        render_kw={
            "id": "phone",
            "class": "input-text size-L",
            "placeholder": "phone"
        }
    )
    qq = wtforms.StringField(
        label="QQ",
        validators=[],
        description="qq",
        render_kw={
            "id": "qq",
            "class": "input-text size-L",
            "placeholder": "2447376396"
        }
    )
    submit = wtforms.SubmitField(
        render_kw={
            "class": "btn btn-success radius size-L button", "value": "       提      交     ",
            "type": "button"
        })
