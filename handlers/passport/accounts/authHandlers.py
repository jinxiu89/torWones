#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-12-31.
from handlers.base import BaseHandler
from libs.captcha.capthca import auth_captcha
from forms.passport import login


class AuthHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write("hello Auth Handler")


class LoginHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        kwargs = {
            "msg": "用户登陆",
            "form": login.LoginForm()
        }
        self.render('passport/accounts/auth/login.html', **kwargs)

    def post(self, *args, **kwargs):
        data = self.json.loads(self.request.body)
        result = auth_captcha(self, data['captcha'])
        if result['status'] is False:
            return self.write({"status": False, "message": result['msg']})
        elif result['status'] is True:
            if result['status'] is False:
                return self.write({"status": False, "message": result['msg']})
            else:
                return self.write({"status": True, "message": result['msg']})


class SignUpHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write("hello SignUp Handler")

    def post(self, *args, **kwargs):
        pass
