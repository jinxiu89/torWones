#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-12-31.
from handlers.base import BaseHandler
from tornado.web import authenticated


class IndexHandler(BaseHandler):
    @authenticated
    def get(self, *args, **kwargs):
        self.render('admin/dashboard/index.html')
