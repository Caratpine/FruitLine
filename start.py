#!/usr/bin/env python
# encoding: utf-8

__author__ = "corazon"

import ConfigParser
import sys
import urlparse
from lib.structure.SpiderModel import FruitLineSpiderModel
from lib.server.server import global_server
from lib.common.log import spider_log
import config
from config import celery_app
from tasks import segementfault_task
from parse.parse_html import segmentfault_parse


def spider():
    conf = ConfigParser.ConfigParser()
    conf.read("./config/spider_config.ini")

    conf_dict = dict()
    conf_dict['url'] = conf.get("spider", "url")
    conf_dict['filter_rule'] = conf.get("spider", "filter_rule")
    conf_dict['parse'] = segmentfault_parse

    url_parse = urlparse.urlparse(conf_dict['url'])
    conf_dict['http'] = url_parse[0]
    conf_dict['domain'] = url_parse[1]

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