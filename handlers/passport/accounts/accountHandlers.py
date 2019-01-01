#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {18-12-29}.
from handlers.base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write("hello account Handlers")


class AddHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        pass
