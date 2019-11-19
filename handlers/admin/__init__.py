#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-12-31.
from tornado.web import url
from handlers.admin.dashboard import (
    dashboardHandlers,
)
from handlers.admin.system import (
    settingsHandlers,
)

adminUrls = [
    url(r'/admin/index', dashboardHandlers.IndexHandler, name="dashboard"),
    url(r'/admin/index/', dashboardHandlers.IndexHandler, name="dashboard"),
    url(r'/admin/system', settingsHandlers.IndexHandler, name="settings"),
]
