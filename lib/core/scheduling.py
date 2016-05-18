#!/usr/bin/env python
# encoding: utf-8

__author__ = "corazon"

import random
import time
import sys
sys.path.append(sys.path[0].split("FruitLine")[0] + "FruitLine/lib")
from structure.UrlModel import UrlModel
from parse import select_url, parse_data


def exit_condition(fruitline_spider_variable):
    if time.time() - fruitline_spider_variable.start_time < fruitline_spider_variable.time:
        if fruitline_spider_variable.exit_flag_count < fruitline_spider_variable.threads:
            if fruitline_spider_variable.total_count < fruitline_spider_variable.count:
                return True
    return False


def depth_first_scheduling(fruitline_spider_variable):
    url_model = UrlModel(fruitline_spider_variable.start_url, "", -1)
    fruitline_spider_variable.global_url_queue.put(url_model)

    while exit_condition(fruitline_spider_variable):
        if fruitline_spider_variable.html_content_queue.qsize() > 0:
            html_content = fruitline_spider_variable.html_content_queue.get()
            url_list = select_url(html_content.url, html_content.html, fruitline_spider_variable)
            parse_data(html_content.html, fruitline_spider_variable)
            for d in url_list:
                url = d['url']
                method = d['method']
                referer = html_content.url
                depth = html_content.depth
                url_model = UrlModel(url, referer, depth, method)

                if url_model.depth <= fruitline_spider_variable.depth:
                    fruitline_spider_variable.global_url_queue.put(url_model)
                else:
                    fruitline_spider_variable.refuse_count += 1


def fifo_scheduling(fruitline_spider_variable):
    url_list = fruitline_spider_variable.get_url_list()
    url_model = UrlModel(url_list.next(), "", -1)
    fruitline_spider_variable.global_url_queue.put(url_model)

    while exit_condition(fruitline_spider_variable):
        if fruitline_spider_variable.html_content_queue.qsize() > 0:
            html_content = fruitline_spider_variable.html_content_queue.get()
            


def global_scheduling(fruitline_spider_variable):
    while True:
        if fruitline_spider_variable.global_url_queue.qsize() > 0:
            url_model = fruitline_spider_variable.global_url_queue.get()
            fruitline_spider_variable.spider_url_queue.put(url_model)



if __name__ == "__main__":
    pass
