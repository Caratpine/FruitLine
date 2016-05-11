#!/usr/bin/env python
# encoding: utf-8

__author__ = "corazon"

from config import celery_app
from lib.structure.SpiderModel import FruitLineSpiderModel
from lib.server.server import global_server
from lib.common.log import spider_log


@celery_app.task
def segementfault_task(conf_dict):
    fruitline_spider_variable = FruitLineSpiderModel(conf_dict)
    spider_log(fruitline_spider_variable)
    global_server(fruitline_spider_variable)