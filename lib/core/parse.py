#!/usr/bin/env python
# encoding: utf-8

__author__ = "corazon"

import logging
import sys
import re
import urlparse
from lxml.html import document_fromstring
import urllib2

reload(sys)
sys.setdefaultencoding("utf-8")

spider_logger = logging.getLogger("FruitLineLogs")


def select_url(url, html, fruitline_spider_variable):
    if html < 10:
        return []
    try:
        html_element = document_fromstring(urllib2.unquote(html))
        html_element.make_links_absolute(url)
        links = [i[2] for i in html_element.iterlinks()]
    except Exception, e:
        spider_logger.error("Function: select_url, Info: %s" % str(e))
        return []
    links_unrepeat = set()
    [links_unrepeat.add(i) for i in links]

    final_links = []
    for i in list(links_unrepeat):
        full_url = repair_url(i, fruitline_spider_variable)
        pattern = re.compile(fruitline_spider_variable.filter_rule)
        if re.match(pattern, full_url):
            if full_url not in fruitline_spider_variable.crawled_url_queue:
                d = dict()
                d['method'] = "get"
                d['url'] = full_url
                final_links.append(d)
    return final_links


def repair_url(url, fruitline_spider_variable):
    res = urlparse.urlparse(url)

    if res[0] != "" and res[1] != "":
        return url
    else:
        url = fruitline_spider_variable.http + "://" + fruitline_spider_variable.domain + url
        return url


def parse_data(html_content, fruitline_spider_variable):
    parse_func = fruitline_spider_variable.parse

    try:
        parse_func(html_content)
    except Exception, e:
        spider_logger.error("Function: parse_func is not existed")


if __name__ == "__main__":
    pass
