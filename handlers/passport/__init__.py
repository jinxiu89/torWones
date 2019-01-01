#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {18-12-29}.
from handlers.passport.accounts import (
    accountHandlers,
    authHandlers,
)

passportUrl = [
    (r'/passport/account', accountHandlers.IndexHandler),
    (r'/passport/account/', accountHandlers.IndexHandler),
    (r'/passport/account/auth', authHandlers.AuthHandler),
    (r'/passport/account/login', authHandlers.LoginHandler),
]
