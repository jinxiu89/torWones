#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {18-12-29}.
from handlers.base import BaseHandler
from modules.passport.usersModules import User as UserModel
from modules.passport.rolesModules import Role as RoleModel
from forms.passport.users import EditForm
from libs.passport.user import edit_user, set_role, set_admin
from libs.common import show
from libs.decorate import permission
from tornado.web import authenticated


class IndexHandler(BaseHandler):
    @authenticated
    # @permission
    def get(self, *args, **kwargs):
        data, count = UserModel.all()
        kwargs = {
            "count": count,
            "data": data
        }
        self.render("passport/accounts/index.html", **kwargs)


class AddHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    @authenticated
    # @permission
    def get(self, *args, **kwargs):
        self.render("passport/accounts/add.html")


class EditHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    @authenticated
    # @permission
    def get(self, user_id):
        kwargs = {
            "form": EditForm(),
            "data": UserModel.by_id(user_id)
        }
        self.render("passport/accounts/edit.html", **kwargs)

    @authenticated
    # @permission
    def post(self, *args, **kwargs):
        data = self.json.loads(self.request.body)
        result = edit_user(self, data)
        if result['status'] is True:
            return self.write(show(True, result['message'], "/passport/account"))
        else:
            return self.write(show(False, result['message'], ''))


class SetRoleHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    @authenticated
    # @permission
    def get(self, user_id):
        data, count = RoleModel.all()
        user = UserModel.by_id(user_id)
        roles = user.roles
        rlist = list()
        for i in roles:
            rlist.append(i.id)
        kwargs = {
            "data": data,
            "user": user,
            "rlist": rlist
        }

        self.render("passport/accounts/set_role.html", **kwargs)

    @authenticated
    # @permission
    def post(self, *args, **kwargs):
        data = self.json.loads(self.request.body)
        result = set_role(self, data)
        if result['status'] is True:
            return self.write(show(True, result['message'], "/passport/account"))
        else:
            return self.write(show(False, result['message'], ''))


class SetAdminHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    @authenticated
    # @permission
    def post(self, user_id):
        result = set_admin(self, user_id)
        if result['status'] is True:
            return self.write(show(True, result['message'], "/passport/account"))
        else:
            return self.write(show(False, result['message'], ''))
