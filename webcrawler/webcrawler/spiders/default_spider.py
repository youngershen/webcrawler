#!/usr/bin/env python
# -*- coding:utf-8 -*-  
# author : younger shen
# email  : younger.x.shen@gmail.com

from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors import LinkExtractor as sle
from webcrawler.items import WebcrawlerItem
import time
import sys
import os
reload(sys)
sys.setdefaultencoding('utf8')

class DefaultSpider(CrawlSpider):
    name = "default"
    allowed_domains = ["58.com"]
    start_urls = ["http://www.58.com/shouji"]
    rules = (
            Rule(sle(allow=('/shouji/.*', )), follow=True, process_request = "add_cookie"),
            Rule(sle(allow=('http://.*\.58.com/shouji/.*\.shtml', )), callback='parse_item', process_request = "add_cookie")
            )

    def parse_item(self, response):
        item = WebcrawlerItem()
        item['title'] = response.xpath("//title").extract()
        item['url']   = response.url
        item['body']  = response.body
        return item

    def add_cookie(self, request):
        request.replace(
                cookies=[
                    {'name': 'id58','value': '05dvZ1RPYxGDmB0SYiNgAg==','domain': '.58.com','path': '/'},
                    {'name': 'myfeet_tooltip', 'value' : 'end', 'domain' : '.58.com', 'path':'/'},
                    {'name': '__utmt_pageTracker', 'value' : '1', 'domain' : '.58.com', 'path':'/'},
                    {'name': 'www58com', 'value' : '"AutoLogin=false&UserID=26310418022407&UserName=tmntp_p2&CityID=0&Email=&AllMsgTotal=0&CommentReadTotal=0&CommentUnReadTotal=0&MsgReadTotal=0&MsgUnReadTotal=0&RequireFriendReadTotal=0&RequireFriendUnReadTotal=0&SystemReadTotal=0&SystemUnReadTotal=0&UserCredit=0&UserScore=0&PurviewID=&IsAgency=false&Agencys=null&SiteKey=2A31A22D9706340594F5D37F0FF3B8E9B1091114D6796754E&Phone=&WltUrl=&UserLoginVer=3FFB2E44A074375AACA31788F08C23D8F&LT=1414490249190"; 58cooper="userid=26310418022407&username=tmntp_p2&cooperkey=a7dee666cee0e92380c5b44819fc50dd"', 'domain' : '.58.com', 'path':'/'},
                    {'name': 'PPU', 'value' : '"UID=26310418022407&PPK=6bb4c724&PPT=250214ca&SK=7A8AA9BF524FE0547756DF8DE262E2A27367F16CE70F13884&LT=1414490249201&UN=tmntp_p2&LV=e5d60885"', 'domain' : '.58.com', 'path':'/'},
                    {'name': 'city', 'value' : 'bj', 'domain' : '.58.com', 'path':'/'},
                    {'name': '__utma', 'value' : '253535702.1132389055.1414488851.1414488851.1414488851.1', 'domain' : '.58.com', 'path':'/'},
                    {'name': '__utmb', 'value' : '253535702.5.9.1414490247538', 'domain' : '.58.com', 'path':'/'},
                    {'name': '__utmc', 'value' : '253535702', 'domain' : '.58.com', 'path':'/'},
                    {'name': '__utmz', 'value' : '253535702.1414488851.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)', 'domain' : '.58.com', 'path':'/'},
                    {'name': 'bangbangid', 'value' : '26310418022407', 'domain' : '.58.com', 'path':'/'},

                    ]
                );

        return request;

