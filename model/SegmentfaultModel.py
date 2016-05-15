#!/usr/bin/env python
# encoding: utf-8

__authoer__ = "corazon"

from sqlalchemy import Column, String, Integer
from .base import Base


class SegmentFault(Base):
    __tablename__ = "segmentfault"
    id = Column(Integer, primary_key=True)
    url = Column(String(1024))
    name = Column(String(1024))

    def __repr__(self):
        return "<SegmentFault(segmentfault='%s')>" % self.name