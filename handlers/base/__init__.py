#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {18-12-29}.
import json

from pycket.session import SessionMixin
from tornado.web import RequestHandler
from modules.passport.usersModules import User
from config import config
from libs.dataBase import db, redis


class BaseHandler(RequestHandler, SessionMixin):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.db = db.dbSession
        self.redis = redis.redis
        self.flashes = None
        self.json = json
        self.config = config

    def data_received(self, chunk):
        pass

    def get_current_user(self):
        user_name = self.session.get("user_name")
        user = None
        if user_name:
            user = User.by_name(name=user_name)
        return user if user else None

    def on_finish(self):
        self.db.close()


class NotFoundHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.render("base/404.html")
        self.set_status(404, "error page is not found")


class InternalErrorHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("base/500.html")
        self.set_status(500, "Internal error")
