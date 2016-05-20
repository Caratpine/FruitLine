#!/usr/bin/env python
# encoding: utf-8

__author__ = "corazon"

import time
import random
import requests
import sys
sys.path.append(sys.path[0].split("FruitLine")[0] + "FruitLine/lib")
from structure.HtmlModel import HtmlModel
from common.common import timestamp
import logging

spider_logger = logging.getLogger("FruitLineLogs")


def spider(fruitline_spider_variable):
    while True:
        if fruitline_spider_variable.spider_url_queue.qsize() > 0:
            url_model = fruitline_spider_variable.spider_url_queue.get()
            html_content = req(url_model.url, fruitline_spider_variable.spider_model)
            fruitline_spider_variable.crawled_url_queue.add(url_model.url)

            if len(html_content) < 10:
                continue
            html_model = HtmlModel(url_model.url, html_content, timestamp(), url_model.depth)
            fruitline_spider_variable.html_content_queue.put(html_model)
            fruitline_spider_variable.total_count += 1
            msg = "[Url] %s  Depth: %s  Found: %s Remaining: %s  Html: %s" % \
                  (url_model.url, str(url_model.depth), str(fruitline_spider_variable.total_count), \
                   str(fruitline_spider_variable.spider_url_queue.qsize()), str(len(html_content)))
            spider_logger.info(msg)
        else:
            time.sleep(5)
    fruitline_spider_variable.exit_flag_count += 1


def req(url, spider_model=0, fetch_time_interval=1, set_referer=True, set_cookies=False):
    headers = dict()

    if set_referer:
        headers['Referer'] = set_referer
    if set_cookies:
        headers['Cookie'] = set_cookies
    headers['User-Agent'] = random_http_headers()

    html_content = ""

    if spider_model == 0:
        try:
            response = requests.get(url, timeout=6, headers=headers, allow_redirects=False)
            if response.status_code == 200:
                html_content = response.content
                spider_logger.info("[URL] %s Status Code: %s" % (str(url), str(response.status_code)))
            else:
                spider_logger.error("[URL] %s Status Code: %s" % (str(url), str(response.status_code)))
                return ""
        except Exception, e:
            spider_logger.error("Function: req, Info: %s", str(e))
            return ""
    else:
        return ""

    time.sleep(fetch_time_interval)
    return html_content


def random_http_headers():
    user_agents = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) \ "
        "Chrome/50.0.2661.86 ",
        "Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)",
    ]

    return random.choice(user_agents)