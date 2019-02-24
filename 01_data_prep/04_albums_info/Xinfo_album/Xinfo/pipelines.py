# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html




from scrapy import signals

class XiamiPipeline(object):
	def process_item(self, item, spider):
		# 从内存以追加的方式打开文件，并写入对应的数据
		with open('genre1' + '.txt', 'a', encoding="UTF-8") as fp:
			fp.write(item['orders'] + '\t')
			fp.write(item['album'] + '\t')
			fp.write(item['lan'] + '\t')
			fp.write(item['releasetime'] + '\t')
			fp.write(item['genre'] + '\n')

		return item
