#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {2019/4/7}.
from modules.permission.permissionModules import PermissionGroup
from sqlalchemy import exc


def add_group(self, data):
    group = PermissionGroup(
        name=data.get("name"),
        description=data.get("description")
    )
    try:
        self.db.add(group)
        self.db.commit()
        return {"status": True, "msg": "新增成功"}
    except exc.IntegrityError as e:
        return {"status": False, "msg": str(e)}


def edit_group(self, data):
    group = PermissionGroup.by_id(data.get("id"))
    group.name = data.get("name")
    group.description = data.get("description")
    try:
        self.db.add(group)
        self.db.commit()
        return {"status": True, "msg": "保存成功"}
    except exc.IntegrityError as e:
        return {"status": False, "msg": str(e)}
