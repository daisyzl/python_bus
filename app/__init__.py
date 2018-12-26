#!/usr/bin/env python
#-*-coding:utf-8-*-   
#说明:
import tornado

from config import AppConfig
from database import db_session
from url import handlers


def create_app():
    class Application(tornado.web.Application):
        def __init__(self):
            settings = dict(
                template_path=AppConfig.TEMPLATE_PATH,
                static_path=AppConfig.STATIC_PATH,
                debug=AppConfig.DEBUG,
            )
            tornado.web.Application.__init__(self, handlers=handlers, **settings)
            self.session = db_session

    return Application()