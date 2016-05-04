#!/usr/bin/env python
# encoding: utf-8

__author__ = "corazon"


class HtmlModel(object):
    def __init__(self, url, html, time, depth):
        self.url = url
        self.html = html
        self.time = time
        self.depth = depth
