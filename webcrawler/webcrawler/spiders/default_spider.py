#!/usr/bin/env python
# -*- coding:utf-8 -*-  

# author : younger shen
# email  : younger.x.shen@gmail.com

import scrapy
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors import LinkExtractor as sle
from webcrawler.items import WebcrawlerItem
import time
import sys
reload(sys)
import os
sys.setdefaultencoding('utf8')

class DefaultSpider(CrawlSpider):
    name = "default"
    allowed_domains = ["58.com"]
    start_urls = ["http://bj.58.com/shouji"]
    rules = ( Rule(sle(allow=('/.*', )), callback='parse_item', follow=True),)

    def parse_item(self, response):
        item = WebcrawlerItem()
        item['title'] = response.xpath("//title").extract()
        item['url']   = response.url
        item['body']  = response.body
        return item
