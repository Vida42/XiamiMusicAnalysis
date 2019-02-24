# tencent.py

from mySpider.items import TencentItem
import scrapy
import re

class TencentSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["hr.tencent.com"]
    start_urls = [
        "http://hr.tencent.com/position.php?&start=0#a"
    ]

    def parse(self, response):
        for each in response.xpath('//*[@class="even"]'):

            item = TencentItem()
            name = each.xpath('./td[1]/a/text()').extract()[0]
            detailLink = each.xpath('./td[1]/a/@href').extract()[0]
            positionInfo = each.xpath('./td[2]/text()').extract()[0]
            peopleNumber = each.xpath('./td[3]/text()').extract()[0]
            workLocation = each.xpath('./td[4]/text()').extract()[0]
            publishTime = each.xpath('./td[5]/text()').extract()[0]

            #print name, detailLink, catalog, peopleNumber, workLocation,publishTime

            item['name'] = name.encode('utf-8')
            item['detailLink'] = detailLink.encode('utf-8')
            item['positionInfo'] = positionInfo.encode('utf-8')
            item['peopleNumber'] = peopleNumber.encode('utf-8')
            item['workLocation'] = workLocation.encode('utf-8')
            item['publishTime'] = publishTime.encode('utf-8')

            curpage = re.search('(\d+)',response.url).group(1)
            page = int(curpage) + 10
            url = re.sub('\d+', str(page), response.url)

            # 发送新的url请求加入待爬队列，并调用回调函数 self.parse
            yield scrapy.Request(url, callback = self.parse)

            # 将获取的数据交给pipeline
            yield item