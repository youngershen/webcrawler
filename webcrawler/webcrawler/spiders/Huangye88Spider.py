#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector

from webcrawler.items import Huangye88comItem


class Huangye88spiderSpider(CrawlSpider):
    name = 'huangye88'
    allowed_domains = ['huangye88.com']
    start_urls = ['http://b2b.huangye88.com/guangdong/']

    rules = (
            Rule(LinkExtractor(allow=r'http://b2b.huangye88.com/qiye[0-9]+/$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = Huangye88comItem()
        item['main_url']     = response.url
        item['company_name'] = response.xpath('//div[@class="Main"]/div[@class="Content"]/div[@class="Contact"]/table[@class="tablelist"][1]/tbody/tr[1]/td/a[1]/@title[1]')[0].extract()
        item['company_url']  = response.xpath('//div[@class="Main"]/div[@class="Content"]/div[@class="Contact"]/table[@class="tablelist"][1]/tbody/tr[1]/td/a[1]/@href[1]')[0].extract()
        item['company_location'] = response.xpath('//div[@class="Main"]/div[@class="Content"]/div[@class="Contact"]/table[@class="tablelist"][1]/tbody/tr[2]/td/a[1]/text()')[0].extract()
        item['company_bussiness_info'] = response.xpath('//div[@class="Main"]/div[@class="Content"]/div[@class="Contact"]/table[@class="tablelist"][1]/tbody/tr[4]/td/strong/text()').extract()
        item['company_description'] = response.xpath('//div[@class="introduct"]/p/text()').extract()
        item['company_phone'] = response.xpath('//div[@class="Main"]/div[@class="Content"]/div[@class="Contact"]/table[@class="tablelist"][1]/tbody/tr[3]/td/text()').extract()
        item['contact_name'] =  response.xpath('//div[@class="Main"]/div[@class="Content"]/div[@class="Contact"]/table[@class="tablelist"][2]/tbody/tr[1]/td/a[1]/span/text()').extract()
        item['contact_url']  = response.xpath('//div[@class="Main"]/div[@class="Content"]/div[@class="Contact"]/table[@class="tablelist"][2]/tbody/tr[1]/td/a[1]/@href').extract()
        item['contact_phone'] = response.xpath('//div[@class="Main"]/div[@class="Content"]/div[@class="Contact"]/table[@class="tablelist"][2]/tbody/tr[2]/td/span/text()').extract()
        item['contact_imurl'] = response.xpath('//div[@class="Main"]/div[@class="Content"]/div[@class="Contact"]/table[@class="tablelist"][2]/tbody/tr[3]/td/span/a[1]/@href').extract()
        item['contact_im'] = response.xpath('//div[@class="Main"]/div[@class="Content"]/div[@class="Contact"]/table[@class="tablelist"][2]/tbody/tr[3]/td/span/text()').extract()
        return  item
