# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html




from scrapy import signals

class XiamiPipeline(object):
    def process_item(self, item, spider):
    	with open('1.txt', 'a', encoding="UTF-8") as fp:
    		fp.write(item['content'])
        # user_id + '\t' + m_link + '\t' + m_name + '\n'

        return item
