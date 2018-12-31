#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-12-31.
from handlers.base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write("hello admin index")
