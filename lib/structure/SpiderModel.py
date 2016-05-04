#!/usr/bin/env python
# encoding: utf-8

__author__ = "corazon"

import Queue
import time


class FruitLineSpiderModel(object):
    def __init__(self):
        self.spider_logger = None

        self.start_url = ""
        self.start_time = time.time()
        self.end_time = None

        self.exit_flag_count = 0
        self.threads = 10
        self.total_count = 0
        self.count = 1000

        self.refuse_count = 0




        self.global_url_queue = Queue.Queue()
        self.spider_url_queue = Queue.Queue()
        self.html_content_queue = Queue.Queue()

