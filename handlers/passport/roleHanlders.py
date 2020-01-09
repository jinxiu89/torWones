#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {2019/4/6}.
from forms.passport.role import RoleAddForm, RoleEditForm
from handlers.base import BaseHandler
from libs.passport.role import add_role, edit_role, set_permissions
from modules.passport.rolesModules import Role as RoleModel
from modules.permission.permissionModules import PermissionGroup
from tornado.web import authenticated
from libs.decorate import permission
from libs.common import show


class Role(BaseHandler):
    """
    角色控制器，用来展示角色
    """

    def data_received(self, chunk):
        pass

    @authenticated
    # @permission
    def get(self, *args, **kwargs):
        # print("hello")
        # exit()
        data, count = RoleModel.all()
        self.render('passport/role/role_list.html', count=count, data=data)


class RoleAdd(BaseHandler):
    def data_received(self, chunk):
        pass

    # @authenticated
    # @admin_permissionl
    def get(self):
        kwargs = {
            "msg": "新增角色",
            "form": RoleAddForm()
        }
        self.render('passport/role/role_add.html', **kwargs)

    @authenticated
    # @admin_permission
    def post(self, *args, **kwargs):
        data = self.json.loads(self.request.body)
        form = RoleAddForm.from_json(data)
        if form.validate():
            result = add_role(self, data)
            if result['status'] is True:
                return self.write(show(True, result['message'], '/passport/roles'))
            else:
                return self.write(show(False, result['message'], ''))
        else:
            for key in form.errors:
                return self.write(show(False, str(form.errors[key]), ''))


class RoleEdit(BaseHandler):
    def data_received(self, chunk):
        pass

    @authenticated
    # @permission
    def get(self, role_id):
        print(self.request.path)
        role = RoleModel.by_id(role_id)
        form = RoleEditForm()
        self.render('passport/role/role_edit.html', role=role, form=form)

    @authenticated
    # @permission
    def post(self, *args, **kwargs):
        data = self.json.loads(self.request.body)
        form = RoleEditForm.from_json(data)
        if form.validate():
            result = edit_role(self, data)
            if result['status'] is True:
                return self.write(show(True, result['message'], '/passport/roles'))
            else:
                return self.write(show(False, result['message'], ''))
        else:
            for key in form.errors:
                return self.write(show(False, str(form.errors[key]), ''))


class SetPermission(BaseHandler):
    """
    2019-05-01 - 2019-05-04 完成逻辑写作
    """

    def data_received(self, chunk):
        pass

    @authenticated
    def get(self, role_id):
        data, count = PermissionGroup. all()
        print(data)
        role = RoleModel.by_id(role_id)
        permissions = role.permission
        plist = list()
        for i in permissions:
            plist.append(i.id)
        self.render("passport/role/set_permission.html", permissions=data, role=role, plist=plist)

    @authenticated
    # @permission
    def post(self, *args, **kwargs):
        data = self.json.loads(self.request.body)
        result = set_permissions(self, data)
        if result['status'] is True:
            return self.write(show(True, result['message'], '/passport/roles'))
        else:
            return self.write(show(False, result['message'], ''))
