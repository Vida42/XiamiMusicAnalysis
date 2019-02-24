
import scrapy
from myXspider.items import XiamiItem

class XiamiSpider(scrapy.Spider):
    name = "xiami"
    allowed_domains = ["xiami.com"]
    url = 'http://www.xiami.com'
    medium = '/space/lib-song/u/'
    tail = '/page/'
    start_urls = [url + medium + user_id + tail]

    def parse(self, response):
		#在song_name里找
		for each in responce.xpath('//td[@class="song_name"]'):
			#提取id列表
			musicid = each.xpath('./a[1]/@href').extract()[0]
			#提取名
			musicname = each.xpath('./a[1]/@class="title"]/text()').extract()[0]
			#打印当前页数

            item['musicid'] = musicid.encode('utf-8').replace('http://www.xiami.com/song/', '').strip()
            item['musicname'] = musicname.encode('utf-8')

            yield item

        if responce.xpath('//a[@class="p_num p_curpage"]/text()') is not None
            curpage = responce.xpath('//a[@class="p_num p_curpage"]/text()').extract()[0]
            print('第%s页' %(curpage))

        #条件，判断是否有下一页
        if responce.xpath('//a[@class="p_redirect_l"]') is not None:
            nextpage = responce.xpath('//a[@class="p_redirect_l"]/@href')extract()[0]
            yield scrapy.Request(self.url + str(self.nextpage), callback=self.parse)

    	#while not not soup.find('a', class_='p_redirect_l'):
    	#if response.xpath('//div[@id="not-exists"]/text()').extract_first() is None
