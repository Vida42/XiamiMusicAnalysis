# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiamiItem(scrapy.Item):

	# 用户id
	userid = scrapy.Field()
	# 综合信息
	cominfo = scrapy.Field()
	# 加入时间
	intime = scrapy.Field()
	# 累计播放
	play_count = scrapy.Field()
	# 等级
	level = scrapy.Field()
	# 访问次数
	v_time = scrapy.Field()
	# 关注
	guanzhu = scrapy.Field()
	# 粉丝
	fensi = scrapy.Field()
	# 分享
	fenxiang = scrapy.Field()