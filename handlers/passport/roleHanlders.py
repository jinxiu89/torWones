#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {2019/4/6}.
from forms.passport.role import RoleAddForm, RoleEditForm
from handlers.base import BaseHandler
from libs.passport.role import add_role, edit_role
from modules.passport.rolesModules import Role as RoleModel
from tornado.web import authenticated


class Role(BaseHandler):
    """
    角色控制器，用来展示角色
    """

    def data_received(self, chunk):
        pass

    @authenticated
    def get(self, *args, **kwargs):
        data, count = RoleModel.all()
        self.render('passport/role/role_list.html', count=count, data=data)

    def post(self, *args, **kwargs):
        pass


class RoleAdd(BaseHandler):
    def data_received(self, chunk):
        pass

    @authenticated
    def get(self, *args, **kwargs):
        kwargs = {
            "msg": "新增角色",
            "form": RoleAddForm()
        }
        self.render('passport/role/role_add.html', **kwargs)

    @authenticated
    def post(self, *args, **kwargs):
        data = self.json.loads(self.request.body)
        form = RoleAddForm.from_json(data)
        if form.validate():
            result = add_role(self, data)
            if result['status'] is True:
                return self.write({"status": True, "message": result['msg'], "url": "/passport/roles"})
            else:
                return self.write({"status": False, "message": result['msg']})
        else:
            for key in form.errors:
                return self.write({"status": False, "message": str(form.errors[key])})


class RoleEdit(BaseHandler):
    def data_received(self, chunk):
        pass

    @authenticated
    def get(self, role_id):
        role = RoleModel.by_id(role_id)
        form = RoleEditForm()
        self.render('passport/role/role_edit.html', role=role, form=form)

    @authenticated
    def post(self, *args, **kwargs):
        data = self.json.loads(self.request.body)
        form = RoleEditForm.from_json(data)
        if form.validate():
            result = edit_role(self, data)
            if result['status'] is True:
                return self.write({"status": True, "message": result['msg'], "url": "/passport/roles"})
            else:
                return self.write({"status": False, "message": result['msg']})
        else:
            for key in form.errors:
                return self.write({"status": False, "message": str(form.errors[key])})
