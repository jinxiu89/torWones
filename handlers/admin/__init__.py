#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-12-31.
from handlers.admin.dashboard import (
    dashboardHandlers,
)
from handlers.admin.system import (
    settingsHandlers,
)

adminUrls = [
    (r'/admin/index', dashboardHandlers.IndexHandler),
    (r'/admin/index/', dashboardHandlers.IndexHandler),
    (r'/admin/system', settingsHandlers.IndexHandler),
]
