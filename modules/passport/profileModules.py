#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {19-3-11}.
from uuid import uuid4
from datetime import datetime
import pbkdf2
from sqlalchemy import (Column, Integer, String, Boolean, DateTime)
from libs.dataBase.db import Base, dbSession
from utils.validate import validate
from string import printable


class Profile(Base):
    __tablename__ = "tb_profile"
    id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(String(64), nullable=False)
