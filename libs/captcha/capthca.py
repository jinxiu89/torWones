#!/usr/bin/env python
# _*_ coding:utf-8_*_
# author:jinxiu89@163.com
# create by thomas on 18-11-1.
from utils.captcha import captcha
from time import time

timestamp = ''


def create_captcha(self):
    """
    在函数体内 global 声明 后的timestamp 变成了全局变量，可以修改 timestamp的值
    从而达到第一次运行是pre_code 为空的效果，当被执行第一遍时 便可以赋值
    在执行第二遍时就可以确认上一次的值时多少
    :param self:
    :return:
    1541317263
    1541317263446
    """
    global timestamp
    result = int(time())
    pre_code = timestamp
    timestamp = result
    if pre_code is not None:
        self.redis.delete("captcha")
    text, img = captcha.create_captcha()
    self.redis.setex("captcha", text, 600)
    return img



def auth_captcha(self, captcha_code):
    """
    验证redis中的验证码和用户输入的验证码是否一致，redis中存储的value 取出来时byte类型的，所以用
    str(self.redis.get('captcha'),encoding='utf-8').lower()来转成str类型来使用
    :param self:
    :param captcha_code:
    :return:
    """

    if captcha_code == '':
        return {'status': False, 'msg': '请输入验证码'}
    elif self.redis.get('captcha') is None:
        return {'status': False, 'msg': '验证码等待的时间太长了，过期了'}
    elif str(self.redis.get('captcha'), encoding='utf-8').lower() != captcha_code.lower():
        return {'status': False, 'msg': '验证码不正确'}
    return {"status": True, 'msg': '正确'}
