#!/usr/bin/env python
# encoding: utf-8

__author__ = "corazon"


class UrlModel(object):
    def __init__(self, url, referer="", depth, method="get", data=""):
        self.url = url
        self.referer = referer
        self.method = method
        self.depth = int(depth) + 1
        self.data = data


if __name__ == "__main__":
    pass
