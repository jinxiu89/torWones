#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {18-12-29}.
from tornado.web import url
from handlers.passport.accounts import (
    accountHandlers,
    authHandlers,
)
from handlers.passport import (
    roleHanlders,
    permissionHandlers,
)

passportUrl = [
    # 用户操作相关
    url(r'/passport/account\.html', accountHandlers.IndexHandler, name="account"),
    url(r'/passport/account/user/add/', accountHandlers.AddHandler, name="add_account"),
    url(r'/passport/account/user/edit/(?P<user_id>[0-9]+)', accountHandlers.EditHandler, name="edit_account"),
    url(r'/passport/account/user/set/role/(?P<user_id>[0-9]+)', accountHandlers.SetRoleHandler, name="set_role"),
    url(r'/passport/account/user/set/admin/(?P<user_id>[0-9]+)', accountHandlers.SetAdminHandler, name="set_admin"),

    # 认证相关
    (r'/passport/account/auth', authHandlers.AuthHandler),
    (r'/passport/account/login', authHandlers.LoginHandler),
    (r'/passport/account/signUp', authHandlers.SignUpHandler),
    (r'/passport/account/signOut', authHandlers.SignOutHandler),

    # 角色权限相关
    (r'/passport/roles', roleHanlders.Role),
    (r'/passport/roles/set/permission/(?P<role_id>[0-9]+)', roleHanlders.SetPermission),
    (r'/passport/role/add', roleHanlders.RoleAdd),
    (r'/passport/role/edit/(?P<role_id>[0-9]+)', roleHanlders.RoleEdit),
    (r'/passport/permissions/group', permissionHandlers.PermissionGroup),
    (r'/passport/permissions/group/add', permissionHandlers.AddPermissionGroup),
    (r'/passport/permissions/group/edit/(?P<group_id>[0-9]+)', permissionHandlers.EditPermissionGroup),
    (r'/passport/permissions', permissionHandlers.Permission),
    (r'/passport/permissions/add/(?P<group_id>[0-9]+)', permissionHandlers.AddPermission),
    (r'/passport/permissions/edit/(?P<permission_id>[0-9]+)', permissionHandlers.EditPermission),
]
