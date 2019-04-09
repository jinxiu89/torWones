#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {2019/4/1}.
from forms.passport.permission import EditPermissionGroupForm, AddPermissionGroupForm
from handlers.base import BaseHandler
from libs.passport.permission import add_group, edit_group
from modules.permission.permissionModules import PermissionGroup as PermissionGroupModel


class PermissionGroup(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        data, count = PermissionGroupModel.all()

        self.render("passport/permission/group_list.html", data=data, count=count)

    def post(self, *args, **kwargs):
        pass


class AddPermissionGroup(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        form = AddPermissionGroupForm()
        self.render("passport/permission/add_group.html", form=form)

    def post(self, *args, **kwargs):
        data = self.json.loads(self.request.body)
        form = AddPermissionGroupForm.from_json(data)
        if form.validate():
            result = add_group(self, data)
            if result['status'] is True:
                return self.write({"status": True, "message": result['msg'], "url": "/passport/permissions_group"})
            else:
                return self.write({"status": False, "message": result['msg']})
        else:
            for key in form.errors:
                return self.write({"status": False, "message": str(form.errors[key])})


class EditPermissionGroup(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, group_id):
        form = EditPermissionGroupForm()
        data = PermissionGroupModel.by_id(group_id)
        self.render("passport/permission/edit_group.html", form=form, data=data)

    def post(self, *args, **kwargs):
        data = self.json.loads(self.request.body)
        form = EditPermissionGroupForm.from_json(data)
        if form.validate():
            result = edit_group(self, data)
            if result['status'] is True:
                return self.write({"status": True, "message": result['msg'], "url": "/passport/permissions_group"})
            else:
                return self.write({"status": False, "message": result['msg']})
        else:
            for key in form.errors:
                return self.write({"status": False, "message": str(form.errors[key])})


class Permission(BaseHandler):
    """
    权限列表，根角色一样有
    """

    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.render("passport/permission/permission_list.html")

    def post(self, *args, **kwargs):
        pass


class AddPermission(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.render("passport/permission/add_permission.html")

    def post(self, *args, **kwargs):
        pass


class EditPermission(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass
