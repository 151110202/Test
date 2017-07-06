# coding=utf-8
"""
系统路由设置
"""
import re

from handlers.index import IndexHandler
from handlers.login import LoginHandler
from handlers.manage import ManageHandler, InputHandler
from handlers.system import SystemHandler

urls = [
    (r'/login', LoginHandler),
    (r'/', IndexHandler),
    (r'/input', InputHandler),
    (r'/(?P<direction>.*)/systems/', SystemHandler),
    (r'/manage', ManageHandler)
]
