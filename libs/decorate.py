#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {2019/5/8}.
from config import setting
from libs.passport.auth import auth


def permission(handler):
    """权限装饰器
    在用户角色里查询权限，然后返回给用户，在每一个操作之前都调用一次这个装饰器，用于检查权限"""

    def func(method):
        def wrapper(self, *args, **kwargs):
            handlers = auth(self.current_user)
            if handler not in handlers:
                self.render(setting.get('template_path') + "/base/nopermission.html")
            else:
                return method(self, *args, **kwargs)

        return wrapper

    return func
