# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url   = scrapy.Field()
    title = scrapy.Field()
    body  = scrapy.Field()



class Huangye88comItem(scrapy.Item):
    company_url            = scrapy.Field()
    company_name           = scrapy.Field()
    company_location       = scrapy.Field()
    company_bussiness_info = scrapy.Field()
    company_description    = scrapy.Field()
    company_phone          = scrapy.Field()
    contact_name           = scrapy.Field()
    contact_url            = scrapy.Field()
    contact_phone          = scrapy.Field()
    contact_imurl          = scrapy.Field()
    contact_im             = scrapy.Field()
    
