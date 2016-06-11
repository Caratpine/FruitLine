#!/usr/bin/env python
# encoding: utf-8

__author__ = "corazon"

import sys
import logging
import re
from lxml.html import fromstring
from config import session
from model import SegmentFault, DouBanMovie

reload(sys)
sys.setdefaultencoding('utf-8')

spider_logger = logging.getLogger("FruitLineLogs")


def segmentfault_parse(html_content):
    try:
        dom = fromstring(html_content)
    except Exception, e:
        spider_logger.error("Function: parse_data, INFO: %s" % str(e))
        return ""
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


def douban_movie_parse(html_content):
    if html_content == '':
        return ""
    else:
        try:
            dom = fromstring(html_content)
        except Exception, e:
            spider_logger.error("Function: parse_data, INFO: %s" % str(e))
            return ""

        try:
            mod_movie_list = dom.xpath("//div[@class='']//table")
        except:
            return ""

        for tb in mod_movie_list:
            movie = dict()

            try:
                movie['name'] = tb.xpath(".//a[@class='']/text()")[0].strip()
            except Exception, e:
                movie['name'] = 'NULL'

            try:
                title_url = tb.xpath(".//a[@class='']/@href")[0].strip()
                movie['movie_id'] = filter(str.isdigit, title_url)
            except Exception, e:
                spider_logger.error("%s" % str(e))
                movie['movie_id'] = 'NULL'

            try:
                movie['tags'] = tb.xpath(".//p[@class='pl']/text()")[0].strip()
            except Exception, e:
                movie['tags'] = 'NULL'

            try:
                movie['star'] = float("{0:.2f}".format(float(tb.xpath('.//span[@class="rating_nums"]/text()')[0].strip())))
            except Exception, e:
                movie['star'] = -1.0

            try:
                movie['image_url'] = tb.xpath('.//img/@src')[0].strip()
            except Exception, e:
                movie['image_url'] = 'NULL'

            try:
                db = DouBanMovie(**movie)
                session.add(db)
                session.commit()
                spider_logger.info("Data: INSERT SUCCESS")
            except Exception, e:
                spider_logger.error("Data: INSERT ERROR: %s" % str(e))

            return movie


def douban_parse(html_content):
    if html_content == '':
        return ''
    else:
        try:
            pattern = re.compile(r'<div class="mod movie-list">(.*)</div>.*?<div class="paginator">', re.S)
            content = pattern.findall(html_content)[0]
            mod_movie_list = fromstring(content.decode('utf-8'))
        except Exception, e:
            spider_logger.error("Function: parse_data, INFO: %s" % str(e))
            return ''

        for dl in mod_movie_list:
            movie = dict()

            try:
                movie['name'] = dl.xpath('.//a[@class="title"]/text()')[0].strip()
            except Exception, e:
                movie['name'] = 'NULL'

            try:
                title_url = dl.xpath('.//a[@class="title"]/@href')[0].strip()
                movie['movie_id'] = filter(str.isdigit, title_url)
            except Exception, e:
                movie['movie_id'] = 'NULL'

            try:
                movie['tags'] = dl.xpath('.//div[@class="desc"]/text()')[0].strip()
            except Exception, e:
                movie['tags'] = 'NULL'

            try:
                movie['star'] = float(dl.xpath('.//span[@class="rating_nums"]/text()')[0].strip())
            except Exception, e:
                movie['star'] = -1

            try:
                movie['image_url'] = dl.xpath('.//img/@src')[0].strip()
            except Exception, e:
                movie['image_url'] = 'NULL'

            try:
                db = DouBanMovie(**movie)
                session.add(db)
                session.commit()
                spider_logger.info("Data: INSERT SUCCESS")
            except Exception, e:
                spider_logger.info("Data: INSERT ERROR: %s" % str(e))
        return
