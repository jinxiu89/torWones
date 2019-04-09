#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {2019/4/6}.
import wtforms
import wtforms_json
from wtforms.validators import (DataRequired, Length, ValidationError)
from wtforms_tornado import Form
from modules.permission.permissionModules import PermissionGroup


class AddPermissionGroupForm(Form):
    """
        wtforms_json 是用于Json数据格式的验证引入的。
        1、在有JSON数据的Form 里init()它，即可解决JSON数据无法通过验证的问题
        """
    wtforms_json.init()
    name = wtforms.StringField(
        label="组名",
        validators=[DataRequired("组名"), Length(4, 16, message="长度必须在4-16个字符之间")],
        description="权限名称",
        render_kw={
            "id": "name",
            "class": "input-text size-L",
            "placeholder": "Role name"
        }
    )

    @staticmethod
    def validate_name(self, field):
        """
        如果名称已经有了，就不让重新加组
        :param field:
        :return:
        """
        if PermissionGroup.by_name(field.data) is not None:
            raise ValidationError("以存在同名权限组，不必重复添加")

    description = wtforms.StringField(
        label="组描述",
        validators=[DataRequired("请输入描述"), Length(12, 64, message="长度必须在12-64个字符之间")],
        description="角色描述",
        render_kw={
            "id": "description",
            "class": "input-text size-L",
            "placeholder": "该组是负责搞什么的呢？"
        }
    )

    submit = wtforms.SubmitField(
        render_kw={
            "class": "btn btn-success radius size-L button", "value": "       提      交     ",
            "type": "button"
        })


class EditPermissionGroupForm(Form):
    """
        wtforms_json 是用于Json数据格式的验证引入的。
        1、在有JSON数据的Form 里init()它，即可解决JSON数据无法通过验证的问题
        """
    wtforms_json.init()
    id = wtforms.IntegerField(render_kw={
        "type": "hidden"
    })

    name = wtforms.StringField(
        label="角色名",
        validators=[DataRequired("请输入角色名"), Length(4, 16, message="长度必须在4-16个字符之间")],
        description="角色名",
        render_kw={
            "id": "name",
            "class": "input-text size-L",
            "placeholder": "Role name"
        }
    )

    description = wtforms.StringField(
        label="组描述",
        validators=[DataRequired("请输入描述"), Length(12, 64, message="长度必须在12-64个字符之间")],
        description="组描述",
        render_kw={
            "id": "description",
            "class": "input-text size-L",
            "placeholder": "该组是负责搞什么的呢？"
        }
    )
    submit = wtforms.SubmitField(
        render_kw={
            "class": "btn btn-success radius size-L button", "value": "       提      交     ",
            "type": "button"
        })
