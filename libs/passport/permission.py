#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {2019/4/7}.
from modules.permission.permissionModules import PermissionGroup, Permission
from sqlalchemy import exc
from libs.common import msg


def add_group(self, data):
    group = PermissionGroup(
        name=data.get("name"),
        description=data.get("description")
    )
    try:
        self.db.add(group)
        self.db.commit()
        return msg(True, '新增成功')
    except exc.IntegrityError as e:
        return msg(False, str(e))


def edit_group(self, data):
    group = PermissionGroup.by_id(data.get("id"))
    group.name = data.get("name")
    group.description = data.get("description")
    try:
        self.db.add(group)
        self.db.commit()
        return msg(True, "保存成功")
    except exc.IntegrityError as e:
        return msg(False, str(e))


def add_permission(self, data):
    group = PermissionGroup.by_id(data.get('group_id'))
    permission = Permission(
        name=data.get('name'),
        handler=data.get('handler'),
        description=data.get("description")
    )
    group.permissions.append(permission)
    try:
        self.db.add(group)
        self.db.commit()
        return msg(True, "保存成功")
    except exc.IntegrityError as e:
        return msg(False, str(e))


def edit_permission(self, data):
    permission = Permission.by_id(data.get("id"))
    permission.name = data.get("name")
    permission.handler = data.get("handler")
    permission.description = data.get("description")
    try:
        self.db.add(permission)
        self.db.commit()
        return msg(True, "保存成功")
    except exc.IntegrityError as e:
        return msg(False, str(e))
