#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {2019/5/7}.


def show(status, message, url):
    """
    本方法用于handler返回到前端的消息返回
    :param status:
    :param message:
    :param args:
    :return:
    """
    return {"status": status, "message": message, "url": url}


def msg(status, message):
    """
    本方法用于向handler传递操作消息
    :param status:
    :param message:
    :return:
    """
    return {"status": status, "message": message}
