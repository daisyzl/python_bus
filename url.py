#!/usr/bin/env python
#-*-coding:utf-8-*-   
#说明:
from handlers.BusHandler import BusStationHandler, BusLineHandler


handlers = [
    (r"/busstation", BusStationHandler),
    (r"/busnumber", BusLineHandler)




]