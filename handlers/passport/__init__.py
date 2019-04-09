#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {18-12-29}.
from handlers.passport.accounts import (
    accountHandlers,
    authHandlers,
)
from handlers.passport import (
    roleHanlders,
    permissionHanlders,
)

passportUrl = [
    (r'/passport/account', accountHandlers.IndexHandler),
    (r'/passport/account/', accountHandlers.IndexHandler),
    (r'/passport/account/auth', authHandlers.AuthHandler),
    (r'/passport/account/login', authHandlers.LoginHandler),
    (r'/passport/account/signUp', authHandlers.SignUpHandler),
    (r'/passport/account/signOut', authHandlers.SignOutHandler),
    (r'/passport/roles', roleHanlders.Role),
    (r'/passport/roles/', roleHanlders.Role),
    (r'/passport/add_role', roleHanlders.RoleAdd),
    (r'/passport/add_role/', roleHanlders.RoleAdd),
    (r'/passport/edit_role/(?P<role_id>[0-9]+)', roleHanlders.RoleEdit),
    (r'/passport/permissions_group', permissionHanlders.PermissionGroup),
    (r'/passport/permissions_group/', permissionHanlders.PermissionGroup),
    (r'/passport/permissions/add_group', permissionHanlders.AddPermissionGroup),
    (r'/passport/permissions/edit_group/(?P<group_id>[0-9]+)', permissionHanlders.EditPermissionGroup),

    (r'/passport/permissions', permissionHanlders.Permission),
    (r'/passport/permissions/', permissionHanlders.Permission),
    (r'/passport/add_permission', permissionHanlders.AddPermission),
    (r'/passport/edit_permission', permissionHanlders.Permission),

]
