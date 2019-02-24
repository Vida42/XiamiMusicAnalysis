# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html




from scrapy import signals

class XiamiPipeline(object):
	def process_item(self, item, spider):
		# 从内存以追加的方式打开文件，并写入对应的数据
		with open('user' + '.txt', 'a', encoding="UTF-8") as fp:
			fp.write(item['userid'] + '\t')
			fp.write(item['cominfo'] + '\t')
			fp.write(item['intime'] + '\t')
			fp.write(item['play_count'] + '\t')
			fp.write(item['level'] + '\t')
			fp.write(item['v_time'] + '\t')
			fp.write(item['guanzhu'] + '\t')
			fp.write(item['fensi'] + '\t')
			fp.write(item['fenxiang'] + '\n')
		return item