#!/usr/bin/env python
#-*-coding:utf-8-*-   
#说明:
from sqlalchemy.orm import session
from tornado import web
from tornado.web import authenticated

from app.models import BusLine, BusNumber


class BusStationHandler(web.RequestHandler):
    def get(self):
        station = self.get_argument('station', '临江大道')
        print("sadsadsd")
        print(station)
        busslines_id = BusLine.query.filter_by(bus_station=station).all()
        for bussline_id in busslines_id:
            print(bussline_id.bus_number_id)
            busline = BusNumber.query.filter_by(id=bussline_id.bus_number_id).all()

            # print(busline.name)
        # # buslines=session.query.filter(BusNumber.id=BusLine.bus_number_id).filter(BusLine.bus_station= "和平大道").all()
        # for busline in buslines:
        #     print(busline.id)

        self.render('index.html', buslines=busline, busstations=None)


class BusLineHandler(web.RequestHandler):
    def get(self):
        bus_number = self.get_argument('bus_number','BUS16')
        bus_number_id = BusNumber.query.filter_by(name=bus_number).first()
        print("wqwqwq")

        print(bus_number_id)
        bus_stations = BusLine.query.filter_by(bus_number_id=bus_number_id.id).all()
        self.render('index.html', busstations=bus_stations, buslines=None)


if __name__ == '__main__':
    test=BusStationHandler()
    test.get()