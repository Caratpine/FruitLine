#!/usr/bin/env python
# encoding: utf-8

__author__ = "corazon"

import time


def timestamp():
    return str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))