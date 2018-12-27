#!/usr/bin/env python
#-*-coding:utf-8-*-   
#说明:
from sqlalchemy.orm import session
from tornado import web

from app.models import BusLine, BusNumber

class BusIndexHandler(web.RequestHandler):
    def get(self):
        self.render('index.html', buslines=None, busstations=None)




class BusStationHandler(web.RequestHandler):
    def get(self):
        station = self.get_argument('station', '和平大道')
        buslines_id = BusLine.query.filter_by(bus_station=station).all()
        data_result=[]
        for bussline_id in buslines_id:
            busline = BusNumber.query.filter_by(id=bussline_id.bus_number_id).first()
            data_result.append(busline.name)

        self.render('index.html', buslines=data_result, busstations=None)

            


class BusLineHandler(web.RequestHandler):
    def get(self):
        bus_number = self.get_argument('number')
        bus_number_id = BusNumber.query.filter_by(name=bus_number).first()
        bus_stations = BusLine.query.filter_by(bus_number_id=bus_number_id.id).all()
        result=[]
        for t in bus_stations:
            result.append(t.bus_station)

        self.render('index.html', busstations=result, buslines=None)


if __name__ == '__main__':
    test=BusStationHandler()
    test.get()