#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {2019/4/1}.
from tornado.web import authenticated
from libs.decorate import permission
from forms.passport.permission import EditPermissionGroupForm, AddPermissionGroupForm, AddPermissionForm, \
    EditPermissionForm
from handlers.base import BaseHandler
from libs.passport.permission import add_group, edit_group, add_permission, edit_permission
from libs.common import show
from modules.permission.permissionModules import PermissionGroup as PermissionGroupModel
from modules.permission.permissionModules import Permission as PermissionModel


class PermissionGroup(BaseHandler):
    def data_received(self, chunk):
        pass

    @authenticated
    @permission('permissionHandlers.PermissionGroup')
    async def get(self, *args, **kwargs):
        data, count = PermissionGroupModel.all()

        self.render("passport/permission/group_list.html", data=data, count=count)

    @authenticated
    # @permission
    async def post(self, *args, **kwargs):
        pass


class AddPermissionGroup(BaseHandler):
    def data_received(self, chunk):
        pass

    @authenticated
    @permission('permissionHandlers.AddPermissionGroup')
    async def get(self, *args, **kwargs):
        form = AddPermissionGroupForm()
        self.render("passport/permission/add_group.html", form=form)

    @authenticated
    @permission('permissionHandlers.AddPermissionGroup')
    async def post(self, *args, **kwargs):
        data = self.json.loads(self.request.body)
        form = AddPermissionGroupForm.from_json(data)
        if form.validate():
            result = add_group(self, data)
            if result['status'] is True:
                return self.write(show(True, result['message'], '/passport/permissions/group'))
            else:
                return self.write(show(False, result['message'], ''))
        else:
            for key in form.errors:
                return self.write(show(False, str(form.errors[key]), ''))


class EditPermissionGroup(BaseHandler):
    def data_received(self, chunk):
        pass

    @authenticated
    @permission('permissionHandlers.EditPermissionGroup')
    async def get(self, group_id):
        form = EditPermissionGroupForm()
        data = PermissionGroupModel.by_id(group_id)
        self.render("passport/permission/edit_group.html", form=form, data=data)

    @authenticated
    # @permission
    async def post(self, *args, **kwargs):
        data = self.json.loads(self.request.body)
        form = EditPermissionGroupForm.from_json(data)
        if form.validate():
            result = edit_group(self, data)
            if result['status'] is True:
                return self.write(show(True, result['message'], '/passport/permissions/group'))
            else:
                return self.write(show(False, result['message'], ''))
        else:
            for key in form.errors:
                return self.write(show(False, str(form.errors[key]), ''))


class Permission(BaseHandler):
    """
    这里
    权限列表，根角色一样有
    """

    def data_received(self, chunk):
        pass

    @authenticated
    @permission('permissionHandlers.EditPermissionGroup')
    async def get(self, *args, **kwargs):
        def get_group(group_id):
            group = PermissionGroupModel.by_id(group_id)
            return group.name

        data, count = PermissionModel.all()

        self.render("passport/permission/permission_list.html", data=data, count=count, get_group=get_group)


class AddPermission(BaseHandler):
    def data_received(self, chunk):
        pass

    @authenticated
    # @permission
    async def get(self, group_id):
        kwargs = {
            "group_id": group_id,
            "msg": "fu quan xian dao zu",
            "form": AddPermissionForm(),
        }
        self.render("passport/permission/add_permission.html", **kwargs)

    @authenticated
    # @permission
    async def post(self, *args, **kwargs):
        data = self.json.loads(self.request.body)
        form = AddPermissionForm.from_json(data)
        if form.validate():
            result = add_permission(self, data)
            if result['status'] is True:
                return self.write(show(True, result['message'], '/passport/permissions/group'))
            else:
                return self.write(show(False, result['message'], ''))
        else:
            for key in form.errors:
                return self.write(show(False, str(form.errors[key]), ''))


class EditPermission(BaseHandler):
    def data_received(self, chunk):
        pass

    @authenticated
    # @permission
    async def get(self, permission_id):
        kwargs = {
            "msg": "编辑权限",
            "form": EditPermissionForm(),
            "data": PermissionModel.by_id(permission_id)
        }
        self.render("passport/permission/edit_permission.html", **kwargs)

    @authenticated
    # @permission
    async def post(self, *args, **kwargs):
        data = self.json.loads(self.request.body)
        form = EditPermissionForm.from_json(data)
        if form.validate():
            result = edit_permission(self, data)
            if result['status'] is True:
                return self.write(show(True, result['message'], '/passport/permissions'))
            else:
                return self.write(show(False, result['message'], ''))
        else:
            for key in form.errors:
                return self.write(show(False, str(form.errors[key]), ''))
