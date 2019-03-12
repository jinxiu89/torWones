#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-12-31.
from uuid import uuid4
from datetime import datetime
import pbkdf2
from sqlalchemy import (Column, Integer, String, Boolean, DateTime)
from libs.dataBase.db import Base, dbSession
from utils.validate import validate
from string import printable


class User(Base):
    """
    用户表
    """
    __tablename__ = "tb_users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid4()))
    name = Column(String(64), nullable=False)
    _password = Column("password", String(64), nullable=False)
    create_time = Column(DateTime, default=datetime.now())
    update_time = Column(DateTime)
    last_login = Column(DateTime)
    login_num = Column(Integer, default=0)
    _locked = Column(Boolean, default=False, nullable=False)
    _avatar = Column(String(128))
    _is_delete = Column(Boolean, default=False, nullable=False)
    email = Column(String(64))
    mobile = Column(String(11))
    num = Column(String(11), unique=True)
    qq = Column(String(13))

    @classmethod
    def all(cls):
        """
        查询所有的数据，返回表数据
        :return: 列表
        """
        return dbSession.query(cls).all()

    @classmethod
    def by_id(cls, id):
        """
        根据ID 查询单条数据
        :param id:
        :return:
        """
        return dbSession.query(cls).filter_by(id=id).first()

    @classmethod
    def by_uuid(cls, uuid):
        """
        根据UUID查询单条数据
        :param uuid:
        :return:
        """
        return dbSession.query(cls).filter_by(uuid=uuid).first()

    @classmethod
    def by_name(cls, name):
        """
        根据name查询数据
        :param name:
        :return:
        """
        return dbSession.query(cls).filter_by(name=name).first()

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

    @property
    def avatar(self):
        """

        :return:
        """
        return self._avatar if self._avatar else "default.jpeg"

    @avatar.setter
    def avatar(self, image_data):
        if 64 < len(image_data) < 1024 * 1024:
            import imghdr
            import os
            ext = imghdr.what("", h=image_data)
            print(ext)
            print(self.uuid)
            if ext in ['png', 'jpeg', 'jpg', 'gif', 'bmp'] and not self.is_xss_image(image_data):
                if self._avatar and os.path.exists("static/images/user_avatars" + self._avatar):
                    os.unlink("static/images/user_avatars" + self._avatar)
                file_path = str("static/images/user_avatars/" + self.uuid + '.' + ext)
                with open(file_path, 'wb') as f:
                    f.write(image_data)
                self._avatar = self.uuid + '.' + ext
            else:
                raise validate.ValidateError("only is png jpeg jpg gif and bmp")
        else:
            raise validate.ValidateError("容量必须在1M以下，64KB以上")

    @staticmethod
    def is_xss_image(data):
        return all([char in printable for char in data[:16]])

    @property
    def locked(self):
        return self._locked

    @locked.setter
    def locked(self, value):
        assert isinstance(value, bool)
        self._locked = value

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'last_login': self.last_login
        }
