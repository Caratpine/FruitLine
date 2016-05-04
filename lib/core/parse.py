#!/usr/bin/env python
# encoding: utf-8

__author__ = "corazon"

import logging
import sys
import re
from lxml.html import document_fromstring
import urllib2

reload(sys)
sys.setdefaultencoding("utf-8")

spider_logger = logging.getLogger("FruitLineLogs")


def select_url(url, html):
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
        d = dict()
        d['method'] = "get"
        d['url'] = i
        final_links.append(d)
    return final_links


if __name__ == "__main__":
    pass
