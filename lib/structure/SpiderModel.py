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
        self.depth = config_dict.get("depth") if config_dict.get("depth") else 10
        self.http = config_dict.get("http") if config_dict.get("http") else "http"
        self.domain = config_dict.get("domain") if config_dict.get("domain") else ""
        try:
            exec "from parse.parse_html import " + config_dict.get("parse")
            self.parse = eval(config_dict.get("parse"))
        except:
            self.parse = ""
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

    def get_url_list(self):
        if self.spider_model == 1:
            with open('./config/url_list.txt', 'r') as f:
                res = f.readlines()
                for u in res:
                    yield u[:-1]


