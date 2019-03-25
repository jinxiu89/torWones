#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {19-3-13}.
from libs.dataBase.db import dbSession
from modules.passport.usersModules import User


def create_user():
    user = User()
    user.name = "admin"
    user.password = "Wavlink@163"
    dbSession.add(user)
    dbSession.commit()


if __name__ == "__main__":
    create_user()
