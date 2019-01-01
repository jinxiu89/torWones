#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {18-12-29}.
import json
from tornado.web import RequestHandler
from libs.dataBase  import db, redis
from config import config


class BaseHandler(RequestHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.db = db.dbSession
        self.redis = redis.redis
        self.flashes = None
        self.json = json
        self.config = config

    def data_received(self, chunk):
        pass

    # def get_current_user(self):
    #     user_name = self.session.get("user_name")
    #     user = None
    #     if user_name:
    #         pass

    def on_finish(self):
        self.db.close()


class NotFoundHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.render("base/404.html")
        self.set_status(404, "error page is not found")
