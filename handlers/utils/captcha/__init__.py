#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-12-31.
from handlers.base import BaseHandler
from libs.captcha import capthca


class CaptchaHandler(BaseHandler):
    def get(self, code):
        img = capthca.create_captcha(self)
        self.set_header('Content-Type', 'image/jpg')
        self.write(img)
