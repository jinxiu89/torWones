#!/usr/bin/env python
# _*_coding:utf-8_*_
# author:Jinxiu89@163.com
# create by kevin on {18-12-29}.
from libs.dataBase.db import Base
from .passport import (usersModules, rolesModules, localOAuthModules, foreignOauthModules)
from .relationship import relationTableModules
from .permission import permissionModules
from .product import productModules
from .product import productSkuModules
