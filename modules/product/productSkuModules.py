#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {2019/8/19}.
from uuid import uuid4
from datetime import datetime
import pbkdf2
from sqlalchemy import (Column, Integer, String, Boolean, DateTime, SmallInteger, Float, DECIMAL, CheckConstraint)
from libs.dataBase.db import Base, dbSession
from utils.validate import validate
from string import printable


class ProductSku(Base):
    __tablename__ = "tb_product_sku"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, comment="产品关联键")
    name = Column(String(128), comment="SKU名称")
    description = Column(String(128), comment="SKU描述")
    price = Column(DECIMAL(10, 2), comment="SKU价格")
    stock = Column(Integer, comment="SKU库存")
    __table_args__ = ((CheckConstraint(stock >= 0)),)
