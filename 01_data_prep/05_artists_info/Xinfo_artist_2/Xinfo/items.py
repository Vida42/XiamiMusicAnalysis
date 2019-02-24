# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiamiItem(scrapy.Item):
    # 该歌曲的orders
    orders = scrapy.Field()
    # 艺人id
    artist = scrapy.Field()
    # 虾米音乐人id
    ixiami = scrapy.Field()
    # 虾米音乐人
    ixiami_name = scrapy.Field()
    # 风格id
    genre = scrapy.Field()
