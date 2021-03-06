#!/usr/bin/env python
# encoding: utf-8

__author__ = "corazon"

import ConfigParser
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base
from celery import Celery
import celeryconfig

sys.path.append(sys.path[0].split("FruitLine")[0] + "FruitLine/config")

conf = ConfigParser.ConfigParser()
conf.read("./config/config.ini")

user = conf.get("mysql", "user")
pwd = conf.get("mysql", "password")
address = conf.get("mysql", "address")
db = conf.get("mysql", "db")

engine = create_engine("mysql+mysqldb://{0}:{1}@{2}/{3}?charset=utf8".format(user, pwd, address, db), echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

main = conf.get("celery", "main")
broker = conf.get("celery", "broker")
backend = conf.get("celery", "backend")

celery_app = Celery(main,
                    broker=broker,
                    backend=backend,
                    include=['tasks'])

celery_app.config_from_object(celeryconfig)


