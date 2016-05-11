#!/usr/bin/env python
# encoding: utf-8

__author__ = "corazon"

import Queue
import time


class FruitLineSpiderModel(object):
    def __init__(self, config_dict=dict()):
        self.spider_logger = None

        self.start_url = config_dict.get("url") if config_dict.get("url") else ""
        self.start_time = time.time()
        self.end_time = None
        self.time = 24 * 3600
        self.depth = 10
        self.http = "https"
        self.domain = "segmentfault.com"

        self.exit_flag_count = 0
        self.threads = config_dict.get("threads") if config_dict.get("threads") else 10
        self.total_count = 0
        self.count = config_dict.get("count") if config_dict.get("count") else 1000 * 1000
        self.spider_model = config_dict.get("spider_model") if config_dict.get("spider_model") else 0
        self.filter_rule = config_dict.get("filter_rule") if config_dict.get("filter_rule") else ""
        self.refuse_count = 0
        self.crawl_policy = config_dict.get("crawl_policy") if config_dict.get("crawl_policy") else 0

        self.global_url_queue = Queue.Queue()
        self.spider_url_queue = Queue.Queue()
        self.html_content_queue = Queue.Queue()
        self.crawled_url_queue = set()

