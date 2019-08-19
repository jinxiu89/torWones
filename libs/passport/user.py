#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {2019/5/5}.
from modules.passport.usersModules import User as UserModel
from modules.passport.rolesModules import Role as RoleModel
from sqlalchemy import exc
from libs.common import msg


def edit_user(self, data):
    user = UserModel.by_id(data.get("id"))
    user.name = data.get("name")
    user.nickname = data.get("nickname")
    user.email = data.get("email")
    user.mobile = data.get("mobile")
    user.qq = data.get("qq")
    try:
        self.db.add(user)
        self.db.commit()
        return msg(True, "保存成功")
    except exc.IntegrityError as e:
        return msg(False, str(e))


def set_role(self, data):
    user_id = data.get("user_id")
    del data["user_id"]
    user = UserModel.by_id(user_id)
    rlist = user.roles
    roles = list()
    for key, value in data.items():
        roles.append(RoleModel.by_id(key))
    delete = list(set(rlist).difference(set(roles)))
    if delete is not None:
        for i in delete:
            user.roles.remove(i)
        self.db.commit()
    user.roles = roles
    try:
        self.db.add(user)
        self.db.commit()
        return msg(True, "保存成功")
    except exc.IntegrityError as e:
        return msg(False, str(e))


def set_admin(self, user_id):
    user = UserModel.by_id(user_id)
    user.is_admin = 1
    try:
        self.db.add(user)
        self.db.commit()
        return msg(True, "设置成功")
    except exc.IntegrityError as e:
        return msg(False, str(e))
