#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {2019/4/6}.
from modules.passport.rolesModules import Role
from sqlalchemy import exc


def add_role(self, data):
    role = Role(
        name=data.get("name"),
        description=data.get("description")
    )
    try:
        self.db.add(role)
        self.db.commit()
        return {"status": True, "msg": "新增成功"}
    except exc.IntegrityError as e:
        return {"status": False, "msg": str(e)}


def edit_role(self, data):
    role = Role.by_id(data.get("id"))
    role.name = data.get("name")
    role.description = data.get("description")
    try:
        self.db.add(role)
        self.db.commit()
        return {"status": True, "msg": "保存成功"}
    except exc.IntegrityError as e:
        return {"status": False, "msg": str(e)}
