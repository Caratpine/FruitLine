#!/usr/bin/env python
# encoding: utf-8

__author__ = "corazon"

import ConfigParser
import sys
from lib.structure.SpiderModel import FruitLineSpiderModel
from lib.server.server import global_server
from lib.common.log import spider_log
import config
from config import celery_app
from tasks import segementfault_task


def spider():
    conf = ConfigParser.ConfigParser()
    conf.read("./config/spider_config.ini")

    conf_dict = dict()
    conf_dict['url'] = conf.get("spider", "url")
    conf_dict['filter_rule'] = conf.get("spider", "filter_rule")

    segementfault_task.delay(conf_dict).get()

    # fruitline_spider_variable = FruitLineSpiderModel(conf_dict)
    # spider_log(fruitline_spider_variable)
    # global_server(fruitline_spider_variable)


if __name__ == "__main__":
    try:
        spider()
    except KeyboardInterrupt, e:
        print "\nExit!"
        sys.exit()