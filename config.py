#!/usr/bin/env python
#-*-coding:utf-8-*-   
#说明:

# coding:utf-8
import getpass
import logging
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig:
    STATIC_PATH = os.path.join(BASE_DIR, 'static')
    TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123@localhost:3306/test"




class AppConfig(BaseConfig):
    pass



