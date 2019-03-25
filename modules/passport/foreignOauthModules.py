#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {19-3-22}.
from sqlalchemy import (Column, Integer, String, Boolean, DateTime, ForeignKey)
from libs.dataBase.db import Base, dbSession
from utils.validate import validate
from string import printable
from sqlalchemy.orm import relationship, backref
from modules.passport.usersModules import User


class ForeignOAuth(Base):
    __tablename__ = "tb_foreign_oauth"
    id = Column(Integer, primary_key=True, autoincrement=True)
    uid = Column(Integer, ForeignKey("tb_users.id"))
    user = relationship('User', backref=backref('ForeignOAuth', uselist=False))
    oauth_name = Column(String(32))
    oauth_id = Column(Integer)
    access_token = Column(String(64))
    oauth_expires = Column(Integer)
