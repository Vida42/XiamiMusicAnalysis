# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiamiItem(scrapy.Item):
    # 用户id
    userid = scrapy.Field()
    # 歌曲id
    musicid = scrapy.Field()
    # 歌曲名
    musicname = scrapy.Field()
