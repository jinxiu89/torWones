#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {2019/3/28}.
from sqlalchemy import (Column, Integer, String)
from sqlalchemy.orm import relationship, backref
from libs.dataBase.db import Base, dbSession
from modules.relationship.relationTableModules import UserRole, PermissionRole


class Role(Base):
    """角色表"""
    __tablename__ = "tb_role"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), nullable=False)
    description = Column(String(64))
    # 1角色和用户属于多对多的关系；
    users = relationship("User", secondary=UserRole.__tablename__)
    # 2、权限和角色是多对多的关系
    permission = relationship("Permission", secondary=PermissionRole.__tablename__, backref=backref("Role"))

    @classmethod
    def all(cls):
        """
        查询所有的数据，返回表数据
        :return: 列表
        """
        query = dbSession.query(cls)
        data = query.all()
        count = query.count()
        return data, count

    @classmethod
    def by_id(cls, id):
        """
        根据ID 查询单条数据
        :param id:
        :return:
        """
        return dbSession.query(cls).filter_by(id=id).first()

    @classmethod
    def by_name(cls, name):
        """
        根据name查询数据
        :param name:
        :return:
        """
        return dbSession.query(cls).filter_by(name=name).first()
