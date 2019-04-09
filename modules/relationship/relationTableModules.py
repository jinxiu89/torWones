#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {2019/3/29}.
from sqlalchemy import Column, Integer, ForeignKey

from libs.dataBase.db import Base


class UserRole(Base):
    """用户角色中间表"""
    __tablename__ = "tb_user_role"
    user_id = Column(Integer, ForeignKey("tb_users.id"), primary_key=True)
    role_id = Column(Integer, ForeignKey("tb_role.id"), primary_key=True)


class PermissionRole(Base):
    """权限角色中间表"""
    __tablename__ = "tb_permission_role"
    permission_id = Column(Integer, ForeignKey("tb_permission.id"), primary_key=True)
    role_id = Column(Integer, ForeignKey("tb_role.id"), primary_key=True)
