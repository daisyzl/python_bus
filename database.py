#!/usr/bin/env python
#-*-coding:utf-8-*-   
#说明:

# coding:utf-8
import json
from datetime import datetime, date

from decimal import Decimal
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import AppConfig

engine = create_engine(AppConfig.SQLALCHEMY_DATABASE_URI, encoding="utf-8", echo=True, max_overflow=5)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


def to_json(self):
    class CJsonEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(obj, date):
                return obj.strftime("%Y-%m-%d")
            elif isinstance(obj, Decimal):
                return eval(str(obj))
            else:
                return json.JSONEncoder.default(self, obj)

    return json.dumps(self.to_dict(), indent=4, ensure_ascii=False, cls=CJsonEncoder)


Base.to_dict = to_dict
Base.to_json = to_json


def init_db():
    import app.models
    Base.metadata.create_all(engine)
    app.models.BusNumber.insert_bus_number()
    app.models.BusLine.insert_bus_station()
    app.models.BusLine.query_bus_station()




if __name__=='__main__':
    init_db()