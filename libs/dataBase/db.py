#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-12-31.
from config import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URI = "mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8" % (
    db['user'],
    db['password'],
    db['host'],
    db['port'],
    db['database']
)
engine = create_engine(DB_URI, echo=False)
Base = declarative_base(engine)
Session = sessionmaker(engine)
dbSession = Session()
