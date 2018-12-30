#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {18-12-29}.
from config import setting
from tornado import web
from handlers import handlers


class Application(web.Application):
    def __init__(self):
        super(Application, self).__init__(handlers, **setting)
