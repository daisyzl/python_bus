#!/usr/bin/env python
#-*-coding:utf-8-*-   
#说明:

from sqlalchemy import Column, Integer, String, text, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app.constants import BUS_NUMBER, BUS_STATION1, BUS_STATION2
from database import Base, db_session


class BusNumber(Base):
    __tablename__ = 'bus_numbers'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    bus_line = relationship('BusLine', backref='bus_number')

    @staticmethod  # 装饰器给类用的,不用设置类对象
    def insert_bus_number():
        """插入公交名称"""
        bus_numbers = BUS_NUMBER
        for t in bus_numbers:
            bus_number = BusNumber.query.filter_by(name=t).first()
            print(bus_number)
            if bus_number is None:
                bus_number = BusNumber(name=t)
                #添加表结构的对象
                db_session.add(bus_number)
            db_session.commit()
            db_session.remove()
#id自增无法输入

class BusLine(Base):
    __tablename__ = 'bus_lines'
    id = Column(Integer, primary_key=True)
    bus_station = Column(String(32))
    bus_number_id = Column(Integer, ForeignKey('bus_numbers.id'))

    @staticmethod  # 装饰器给类用的,不用设置类对象
    def insert_bus_station():
        """插入公交站点1 16路"""
        bus_stations = BUS_STATION1
        for t in bus_stations:
            bus_station = BusLine.query.filter_by(bus_station=t).first()
            print(bus_station)
            if bus_station is None:
                bus_station = BusLine(bus_station=t, bus_number_id=1)
                # 添加表结构的对象
                db_session.add(bus_station)
            db_session.commit()
            db_session.remove()

        """插入公交站点2 76路"""
        bus_stations = BUS_STATION2
        for t in bus_stations:
            bus_station = BusLine.query.filter_by(bus_station=t).first()
            print(bus_station)
            if bus_station is None:
                bus_station = BusLine(bus_station=t, bus_number_id=2)
                # 添加表结构的对象
                db_session.add(bus_station)
            db_session.commit()
            db_session.remove()
        # id自增无法输入


    @staticmethod
    def query_bus_station():
        bus_line = BusLine.query.filter_by(id=1).first()
        print(bus_line)










