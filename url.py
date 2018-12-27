#!/usr/bin/env python
#-*-coding:utf-8-*-   
#说明:通过url找到对应的处理函数
from handlers.BusHandler import BusStationHandler, BusLineHandler, BusIndexHandler

handlers = [
    (r"/", BusIndexHandler),
    (r"/busstation", BusStationHandler),
    (r"/busnumber", BusLineHandler),




]