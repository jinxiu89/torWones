#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {2019/4/6}.
from modules.passport.rolesModules import Role
from modules.permission.permissionModules import Permission
from modules.relationship.relationTableModules import PermissionRole
from libs.common import msg
from sqlalchemy import exc


def add_role(self, data):
    role = Role(
        name=data.get("name"),
        description=data.get("description")
    )
    try:
        self.db.add(role)
        self.db.commit()
        return msg(True, "新增成功")
    except exc.IntegrityError as e:
        return msg(False, str(e))


def edit_role(self, data):
    role = Role.by_id(data.get("id"))
    role.name = data.get("name")
    role.description = data.get("description")
    try:
        self.db.add(role)
        self.db.commit()
        return msg(True, "保存成功")
    except exc.IntegrityError as e:
        return msg(False, str(e))


def set_permissions(self, data):
    """
    多对多的数据新增
    1、拿到原来的数据
    2、组装现在的数据
    3、原来的数据集合和现在的数据集合比较得到的差集就是需要删除掉的数据
    4、把现有的数据插入数据库
    5、这里利用的是set的子交并补概念
    date:2019-05-04
    :param self:
    :param data:
    :return:
    """
    role_id = data.get("role_id")
    del data['role_id']
    role = Role.by_id(role_id)
    plist = role.permission
    permissions = list()
    for key, value in data.items():
        permissions.append(Permission.by_id(key))
    delete = list(set(plist).difference(set(permissions)))
    if delete is not None:
        for i in delete:
            role.permission.remove(i)
        self.db.commit()
    role.permission = permissions
    try:
        self.db.add(role)
        self.db.commit()
        return msg(True, "保存成功")
    except exc.IntegrityError as e:
        return msg(False, str(e))
