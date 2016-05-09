#!/usr/bin/env python
# encoding: utf-8

__author__ = "corazon"

import logging
import sys
import re
import urlparse
from lxml.html import document_fromstring
from lxml.html import fromstring
import urllib2
from config import session
from model import SegmentFault

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
            d = dict()
            d['method'] = "get"
            d['url'] = full_url
            final_links.append(d)
        else:
            spider_logger.info("URL is not match")
    return final_links


def repair_url(url, fruitline_spider_variable):
    res = urlparse.urlparse(url)

    if res[0] != "" and res[1] != "":
        return url
    else:
        url = fruitline_spider_variable.http + "://" + fruitline_spider_variable.domain + url
        return url


def parse_data(html_content):
    try:
        dom = fromstring(html_content)
    except Exception, e:
        spider_logger.error("Function: parse_data, INFO: %s" % str(e))
        return
    ul = dom.xpath("//ul[@class='widget-links list-unstyled']")[0]

    data = dict()

    for li in ul:
        try:
            data['name'] = li.xpath(".//a/text()")[0].strip()
        except Exception, e:
            data['name'] = ""

        try:
            data['url'] = li.xpath(".//a/@href")[0].strip()
        except Exception, e:
            data['url'] = ""
        try:
            sg = SegmentFault(**data)
            session.add(sg)
            session.commit()
            spider_logger.info("Data: INSERT SUCCESS")
        except Exception, e:
            spider_logger.error("Data: INSERT ERROR: %s" % str(e))

if __name__ == "__main__":
    pass
