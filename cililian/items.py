# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CililianItem(scrapy.Item):
    # define the fields for your item here like:
    keyword = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    size = scrapy.Field()
    pass
