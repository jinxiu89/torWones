#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-12-31.
from handlers.base import BaseHandler
from forms.passport import login

class AuthHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write("hello Auth Handler")


class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        kwargs={
            "msg":"用户登陆",
            "form":login.LoginForm()
        }
        self.render('passport/accounts/auth/login.html', **kwargs)

    def post(self, *args, **kwargs):
        pass


class SignUpHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write("hello SignUp Handler")

    def post(self, *args, **kwargs):
        pass
