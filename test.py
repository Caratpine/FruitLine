#!/usr/bin/env python
# encoding: utf-8

__author__ = "corazon"


class TestClass(object):
    def __init__(self, func):
        self.func = func


def test(a, b):
    return a + b

if __name__ == "__main__":
    obj = TestClass(test)
    func = obj.func
    res = func(1, 2)
    print res
