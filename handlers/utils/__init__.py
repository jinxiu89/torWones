#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-12-31.
from handlers.utils import captcha

utilsUrl = [
    (r'/utils/captcha', captcha.CaptchaHandler),
    (r'/utils/captcha/', captcha.CaptchaHandler)
]
