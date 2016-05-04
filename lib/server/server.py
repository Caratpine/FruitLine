#!/usr/bin/env python
# encoding: utf-8

__author__ = "corazon"

import time
import sys
sys.path.append(sys.path[0].split("FruitLine")[0] + "FruitLine")
import threading
import logging
from lib.core.scheduling import depth_first_scheduling
from lib.core.scheduling import global_scheduling

spider_logger = logging.getLogger("FruitLineLogs")


def global_server(fruitline_spider_variable):
    threads_list = []
    spider_threads = []

    threads_list.append(threading.Thread(target=depth_first_scheduling, args=(fruitline_spider_variable, )))
    threads_list.append(threading.Thread(target=global_scheduling, args=(fruitline_spider_variable, )))

    for t in threads_list:
        t.setDaemon(True)
        t.start()

    for i in xrange(fruitline_spider_variable.threads):
        spider_threads.append(threading.Thread(target=, args=()))

    for t in spider_threads:
        t.setDaemon(True)
        t.start()

    time.sleep(120)

    while True:
        if fruitline_spider_variable.spider_url_queue.qsize() == 0:
            spider_logger.critical("Spider wait to exit!")
            time.sleep(120)

            if fruitline_spider_variable.spider_url_queue.qsize() == 0:
                pass
            else:
                continue
            spider_logger.critical("Spider exit!")
            sys.exit(0)
        else:
            time.sleep(10)

