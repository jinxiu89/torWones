#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-12-8.
import wtforms
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
