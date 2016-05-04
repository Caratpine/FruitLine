#!/usr/bin/env python
# encoding: utf-8

__author__ = "corazon"

import logging

def spider_log(fruitline_spider_variable):
    spider_logger = logging.getLogger("FruitLineLogs")
    spider_logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")

    console_handler.setFormatter(formatter)

    spider_logger.addHandler(console_handler)

    fruitline_spider_variable.spider_logger = spider_logger

if __name__ == "__main__":
    pass
