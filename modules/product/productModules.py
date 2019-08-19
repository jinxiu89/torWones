#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {19-3-12}.
from uuid import uuid4
from datetime import datetime
import pbkdf2
from sqlalchemy import (Column, Integer, String, Boolean, DateTime, SmallInteger, Float, DECIMAL)
from libs.dataBase.db import Base, dbSession
from utils.validate import validate
from string import printable


class Product(Base):
    __tablename__ = "tb_product"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), comment="产品标题")
    title = Column(String(64), nullable=False, comment="url_标题")
    keywords = Column(String(128), comment="关键词")
    description = Column(String(128), comment="SKU描述")
    thumbnail = Column(String(255), comment="缩略图")
    status = Column(SmallInteger, comment="是否在售")
    rating = Column(Float(2), comment="商品评分")
    sales_volume = Column(Integer, comment="销售量", default=100)
    review_count = Column(Integer, comment="评论数量")
    price = Column(DECIMAL(10, 2), comment="商品最低价格,保留2位小数")
