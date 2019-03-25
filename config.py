#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {18-12-29}.
import os
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)
option = {
    'port': 8000,
    'log_path': os.path.join(BASE_DIR, "logs/log.txt"),
    'log_level': "debug"  # debug|info|warning|error|none
}
setting = {
    "debug": True,
    "static_path": os.path.join(BASE_DIR, "static"),
    "avatar_path": os.path.join(BASE_DIR, 'static/images/user_avatars/'),
    "template_path": os.path.join(BASE_DIR, "templates"),
    "xsrf_cookies": True,
    "cookie_secret": "db7ef65f-3bb0-4d19-9966-d07fafb3cd8a",
    "login_url": "/passport/account/login",
    "ui_methods": {
        "get_flashed_message": ""
    },
    "pycket": {
        "engine": "redis",
        "storage": {
            "host": "localhost",
            "port": 6379,
            "db_sessions": 5,
            "db_notifications": 11,
            "max_connections": 2 ** 31,
        },
        "cookies": {
            "expires_days": 30,
        }
    },
    "image_type": ['png', 'jpeg', 'jpg', 'gif', 'bmp']
}
config = {
    "version": "0.0.1",
    "Copyright": "Copyright © {} {} All Rights Reserved. ".format(datetime.now().strftime("%Y"), "www.motkit.com"),
    "stack": "Tornado",
    "object": "TorWones"
}
db = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Wavlink@163",
    "database": "wones",  # your dataBase
    "port": "3306"
}
