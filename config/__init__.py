#!/usr/bin/env python
# encoding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base

engine = create_engine("mysql+mysqldb://root:@localhost/test", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

