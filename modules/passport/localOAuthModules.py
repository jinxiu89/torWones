#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {19-3-22}.
from datetime import datetime
import pbkdf2
from sqlalchemy import (Column, Integer, String, Boolean, DateTime, ForeignKey)
from libs.dataBase.db import Base, dbSession
from utils.validate import validate
from string import printable
from sqlalchemy.orm import relationship, backref


class LocalOAuth(Base):
    __tablename__ = "tb_local_oauth"
    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, ForeignKey("tb_users.id"))
    _password = Column("password", String(64), nullable=False)
    user = relationship('User', backref=backref('LocalOAuth', uselist=False))

    @staticmethod
    def _hash_password(password):
        """
        将用户输入的密码 加盐
        :param password:
        :return:
        """
        return pbkdf2.crypt(password, iterations=0X2537)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = self._hash_password(password)

    def auth_password(self, other_password):
        """
        传进来的密码 加密比对 如果能想等 就代表通过，不想等就表示密码不正确
        :param other_password:
        :return:
        """
        if self._password is not None:
            return self.password == pbkdf2.crypt(other_password, self.password)
        else:
            return False
