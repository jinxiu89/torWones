#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {18-12-29}.
import tornado.options
from config import option
from tornado import ioloop
from application import Application


def main():
    tornado.options.options.log_file_prefix = option['log_path']
    tornado.options.options.logging = option['log_level']
    tornado.options.parse_command_line()
    app = Application()
    app.listen(option['port'])
    try:
        ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        ioloop.IOLoop.current().stop()
    print("Program exit!")


if __name__ == "__main__":
    main()
