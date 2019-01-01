#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {18-12-29}.
from handlers.passport import passportUrl
from handlers.admin import adminUrls
from handlers.utils import utilsUrl

handlers = []
handlers += passportUrl
handlers += adminUrls
handlers += utilsUrl
