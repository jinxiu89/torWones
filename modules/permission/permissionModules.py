#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {2019/3/30}.
from sqlalchemy import (Column, Integer, String, ForeignKey)
from sqlalchemy.orm import relationship, backref
from modules.relationship.relationTableModules import PermissionRole
from libs.dataBase.db import Base, dbSession


class PermissionGroup(Base):
    """权限组，将各种权限分类"""
    __tablename__ = "tb_permission_group"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    description = Column(String(64))
    permissions = relationship("Permission", backref=backref("Permission"))

    @classmethod
    def by_name(cls, name):
        return dbSession.query(cls).filter_by(name=name).first()

    @classmethod
    def by_id(cls, group_id):
        return dbSession.query(cls).filter_by(id=group_id).first()

    @classmethod
    def all(cls):
        query = dbSession.query(cls)
        data = query.all()
        count = query.count()
        return data, count

    @classmethod
    def query(cls):
        return dbSession.query(cls)


class Permission(Base):
    """权限表"""
    __tablename__ = "tb_permission"
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_id = Column(Integer, ForeignKey('tb_permission_group.id'))
    name = Column(String(64), nullable=False)
    description = Column(String(64))
    # 权限和菜单是一对一的关系
    handler = Column(String(64), nullable=False)
    # 和角色是多对多关系
    role = relationship("Role", secondary=PermissionRole.__tablename__)

    @classmethod
    def all(cls):
        """
        查询所有的数据，返回表数据
        :return: 列表
        """
        query = dbSession.query(cls)
        data = query.order_by(cls.group_id).all()
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


class Menu(Base):
    """菜单权限"""
    __tablename__ = "tb_permission_menu"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    pid = Column(Integer, ForeignKey("tb_permission.id"))
    # 权限和菜单是一对一的关系
    permission = relationship("Permission", backref=backref("Menu", uselist=False))

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


class Handler(Base):
    """Handler表"""
    __tablename__ = "tb_permission_handler"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    pid = Column(Integer, ForeignKey("tb_permission.id"))
    # 和菜单一样 也是一对一的关系
    permission = relationship("Permission", backref=backref("Handler", uselist=False))

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
