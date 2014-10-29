#!/usr/bin/env python
# -*- coding:utf-8 -*-  

# author : younger shen
# email  : younger.x.shen@gmail.com
import json
import redis
from config import PAGE_SIZE
from config import REDIS_HOST
from config import REDIS_PORT
from config import REDIS_DB
from config import HUANGYE88_KEY

def get_redis():
    return redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

def find_page(page):
    redis_cli= get_redis()
    item_count = redis_cli.llen(HUANGYE88_KEY)
    page = Pager(PAGE_SIZE, item_count, page).page(page)
    ret = redis_cli.lrange(HUANGYE88_KEY, page[0], page[1])
    return ret, page[2]

def json_decode(list):
    ret = []
    for i,e in enumerate(list):
        ret.append(json.loads(e))
    return ret


class Pager(object):
    def __init__(self, page_size, item_count, current_page = 1):
        self.page_size = page_size
        self.item_count = item_count
        self.current_page = current_page

    def page(self, page):
        self.current_page = page
        page_start = self.page_size * (page - 1)
        page_end = page_start + self.page_size - 1
        return page_start, page_end, self.page_count()

    def next_page(self):
        self.current_page += 1
        return self.page(self.current_page)

    def perv_page(self):
        self.current_page -= 1
        return self.page(self.current_page)

    def page_count(self):
        
        if self.item_count % self.page_size  == 0:
            return self.item_count / self.page_size
        else:
            return self.item_count / self.page_size + 1
   
