# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiamiItem(scrapy.Item):
    # 该歌曲的orders
    orders = scrapy.Field()
    # 专辑id
    album = scrapy.Field()
    # 语种
    lan = scrapy.Field()
    # 时间
    releasetime = scrapy.Field()
    # 风格id
    genre = scrapy.Field()
