#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-12-31.
from uuid import uuid4
from datetime import datetime
import pbkdf2
from sqlalchemy import (Column, Integer, String, Boolean, DateTime)
from sqlalchemy.orm import relationship, backref
from modules.passport.localOAuthModules import LocalOAuth
from libs.dataBase.db import Base, dbSession
from utils.validate import validate
from string import printable
from config import setting


class User(Base):
    """
    用户表
    """
    __tablename__ = "tb_users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    gid = Column(Integer)
    uuid = Column(String(36), unique=True, nullable=False, default=lambda: str(uuid4()))
    name = Column(String(64), nullable=False)
    nickname = Column(String(64))
    create_time = Column(DateTime, default=datetime.now())
    phone = Column(String(64))
    email = Column(String(64))
    mobile = Column(String(11))
    num = Column(String(11), unique=True)
    qq = Column(String(13))
    _locked = Column(Boolean, default=False, nullable=False)
    _is_delete = Column(Boolean, default=False, nullable=False)
    _avatar = Column(String(128))
    local_oauth = relationship('LocalOAuth', uselist=False)

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
            if ext in setting['image_type'] and not self.is_xss_image(image_data):
                if self._avatar and os.path.exists(setting['avatar_path'] + self._avatar):
                    os.unlink(setting['avatar_path'] + self._avatar)
                file_path = str(setting['avatar_path'] + self.uuid + '.' + ext)
                with open(file_path, 'wb') as f:
                    f.write(image_data)
                self._avatar = self.uuid + '.' + ext
            else:
                raise validate.ValidateError("only is png jpeg jpg gif and bmp")
        else:
            raise validate.ValidateError("容量必须在1M以下，64KB以上")
