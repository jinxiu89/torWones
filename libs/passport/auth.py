#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {19-3-13}.
from modules.passport.usersModules import User
# from modules.passport.localOAuthModules import LocalOAuth
from datetime import datetime


def sign_in(self, data):
    user = User.by_name(name=data.get('name'))
    password = user.local_oauth
    if user and password.auth_password(other_password=data.get('password')):
        self.session.set('user_name', user.name)
        return {"status": True, "msg": "登陆成功"}
    return {"status": False, "msg": "用户名和密码不正确"}


def sign_up(self, data):
    user = User(name=data.get('name'))
    local_oauth = LocalOAuth()
    local_oauth.password = data.get('password')
    user.local_oauth = local_oauth
    self.db.add(user)
    self.db.commit()
    return {"status": True, "msg": "注册成功"}
