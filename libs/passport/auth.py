#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {19-3-13}.
from modules.passport.usersModules import User
from modules.passport.localOAuthModules import LocalOAuth
from modules.permission.permissionModules import Permission
from libs.common import msg
from datetime import datetime
from sqlalchemy import exc


def sign_in(self, data):
    user = User.by_name(name=data.get('name'))
    password = user.local_oauth
    if user and password.auth_password(other_password=data.get('password')):
        self.session.set('user_name', user.name)
        return msg(True, "登陆成功")
    return msg(False, '用户名和密码不正确')


def sign_up(self, data):
    user = User(name=data.get('name'))
    local_oauth = LocalOAuth()
    local_oauth.password = data.get('password')
    user.local_oauth = local_oauth
    try:
        self.db.add(user)
        self.db.commit()
        return msg(True, "注册成功")
    except exc.IntegrityError as e:
        return msg(False, str(e))


def auth(user):
    roles = user.roles
    rlist = [i.permission for i in roles]
    permissions = list(set(sum(rlist, [])))
    return [i.handler for i in permissions]


def handlers():
    data, count = Permission.all()
    return [i.handler for i in data]
