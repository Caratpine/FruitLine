#!/usr/bin/env python
# encoding: utf-8

__authoer__ = "corazon"

from sqlalchemy import Column, String, Integer, Float
from .base import Base


class SegmentFault(Base):
    __tablename__ = "segmentfault"
    id = Column(Integer, primary_key=True)
    url = Column(String(1024))
    name = Column(String(1024))

    def __repr__(self):
        return "<SegmentFault(segmentfault='%s')>" % self.name


class DouBanMovie(Base):
    __tablename__ = "douban_movies"

    id = Column(Integer, primary_key=True)
    movie_id = Column(String(64))
    image_url = Column(String(1024))
    name = Column(String(1024))
    tags = Column(String(2048))
    star = Column(Float)

    def __repr__(self):
        return "<DoubanMovie(doubanmovie='%s')>" % self.movie_id

