#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-12-31.

class ValidateError(Exception):
    def __init__(self, message):
        super(ValidateError, self).__init__(message)
