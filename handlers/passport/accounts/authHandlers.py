#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-12-31.
import wtforms_json
from handlers.base import BaseHandler
from libs.captcha.capthca import auth_captcha
from libs.passport.auth import sign_in, sign_up
from libs.common import show
from forms.passport import (login, signup)
from tornado.web import authenticated
from config import setting


class AuthHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write("hello Auth Handler")


class LoginHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        next_url = self.get_argument('next', '/admin/index')
        if self.get_current_user():
            return self.redirect("/admin/index")
        else:
            kwargs = {
                "msg": "用户登陆",
                "form": login.LoginForm(),
                "next_url": next_url
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
                return self.write(show(False, result['message'], ''))
            else:
                return self.write(show(True, result['message'], self.get_argument('next', '/admin/index')))
        else:
            for key in form.errors:
                return self.write(show(False, str(form.errors[key]), ''))


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
                return self.write(show(False, result['message'], ''))
            else:
                return self.write(show(True, result['message'], "/passport/account/login"))
        else:
            for key in form.errors:
                return self.write(show(False, str(form.errors[key]), ''))


class SignOutHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    @authenticated
    def get(self, *args, **kwargs):
        self.session.delete('user_name')
        self.redirect(setting['login_url'])
