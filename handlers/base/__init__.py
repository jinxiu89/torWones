#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {18-12-29}.
from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    # super().__init__(self)

    def data_received(self, chunk):
        pass

    # def get_current_user(self):
    #     pass
    #
    # def on_finish(self):
    #     pass


class NotFoundHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.render("base/404.html")
        self.set_status(404, "error page is not found")
