#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-12-31.
import wtforms_json
from handlers.base import BaseHandler
from libs.captcha.capthca import auth_captcha
from libs.passport.auth import sign_in, sign_up
from forms.passport import (login, signup)


class AuthHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write("hello Auth Handler")


class LoginHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        next = self.get_argument('next', '/')
        kwargs = {
            "msg": "用户登陆",
            "form": login.LoginForm(),
            "next": next
        }
        self.render('passport/accounts/auth/login.html', **kwargs)

    def post(self, *args, **kwargs):
        """
        加入Form验证工具，科学的应对一亿只草泥马的问题。
        这里的form = login.LoginForm.from_json(data)是为了解决ajax提交过来的json数据而引入的，这个 from_json 在Form里初始化
        后续的注释将不写此段
        :param args:
        :param kwargs:
        :return:
        """
        data = self.json.loads(self.request.body)
        form = login.LoginForm.from_json(data)
        if form.validate():
            result = sign_in(self, data)
            if result['status'] is False:
                return self.write({"status": False, "message": result['msg']})
            else:
                return self.write({"status": True, "message": result['msg'], "url": self.get_argument('next', '/')})
        else:
            for key in form.errors:
                return self.write({"status": False, "message": str(form.errors[key])})


class SignUpHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        kwargs = {
            "msg": "用户注册",
            "form": signup.SignUpForm()
        }
        self.render("passport/accounts/auth/SignUp.html", **kwargs)

    def post(self, *args, **kwargs):
        data = self.json.loads(self.request.body)
        form = signup.SignUpForm.from_json(data)
        if form.validate():
            result = sign_up(self, data)
            if result['status'] is False:
                return self.write({"status": False, "message": "auth 注册程序有问题", "url": self.request.url})
            else:
                return self.write({"status": True, "message": result['msg'], "url": "/passport/account/login"})
        else:
            for key in form.errors:
                return self.write({"status": False, "message": str(form.errors[key])})
