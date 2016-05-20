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
import logging
from config import celery_app
from tasks import segementfault_task, douban_task
from parse.parse_html import segmentfault_parse

spider_logger = logging.getLogger("FruitLineLogs")


def get_config():
    conf = ConfigParser.ConfigParser()
    conf.read("./config/spider_config.ini")

    sections = conf.sections()
    conf_dicts = dict()

    for sec in sections:
        conf_dict = dict()
        try:
            conf_dict['url'] = conf.get(sec, "url")
        except Exception, e:
            spider_logger.error("CONFIG: cannot get url, INFO: %s" % str(e))
            return
        try:
            conf_dict['filter_rule'] = conf.get(sec, "filter_rule")
        except Exception, e:
            pass
        try:
            conf_dict['parse'] = conf.get(sec, "parse")
        except Exception, e:
            pass
        try:
            conf_dict['depth'] = conf.get(sec, "depth")
        except Exception, e:
            pass
        try:
            conf_dict['crawl_policy'] = conf.get(sec, 'crawl_policy')
        except Exception, e:
            pass
        try:
            conf_dict['spider_model'] = conf.get(sec, 'spider_model')
        except Exception, e:
            pass
        try:
            conf_dict['threads'] = conf.get(sec, 'threads')
        except Exception, e:
            pass
        try:
            conf_dict['count'] = conf.get(sec, 'count')
        except Exception, e:
            pass

        url_parse = urlparse.urlparse(conf_dict['url'])
        conf_dict['http'] = url_parse[0]
        conf_dict['domain'] = url_parse[1]

        conf_dicts[sec] = conf_dict

    return conf_dicts


def spider(conf_dicts):
    # segementfault_task.delay(conf_dicts['spider']).get()
    fruitline_spider_variable = FruitLineSpiderModel(conf_dicts['douban'])
    spider_log(fruitline_spider_variable)
    global_server(fruitline_spider_variable)
    # segementfault_task.apply_async(args=[conf_dicts['spider']], queue='machine1', routing_key='machine1').get()
    # douban_task.apply_async(args=[conf_dicts['douban']], queue='machine1', routing_key='machine1').get()


if __name__ == "__main__":
    try:
        conf_dicts = get_config()
        if conf_dicts is not None:
            spider(conf_dicts)
    except KeyboardInterrupt, e:
        print "\nExit!"
        sys.exit()