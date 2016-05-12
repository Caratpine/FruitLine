#!/usr/bin/env python
# encoding: utf-8

__author__ = "corazon"

import sys
import logging
from lxml.html import fromstring
from config import session
from model import SegmentFault

reload(sys)
sys.setdefaultencoding('utf-8')

spider_logger = logging.getLogger("FruitLineLogs")


def segmentfault_parse(html_content):
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

    return data
