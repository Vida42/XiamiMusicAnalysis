##2017.9.21晚22点
import scrapy
from myXspider.items import XiamiItem

class XiamiSpider(scrapy.Spider):
    name = "xiami"
    allowed_domains = ["xiami.com"]
    url = 'http://www.xiami.com'
    medium = '/space/lib-song/u/'
    tail = '/page/'

    id_list=[] 
    with open('figure3.txt','r') as f2:
        for eachline in f2:
            id_list.append(eachline.strip())
    
    start_urls = [url + medium + str(id_list[0]) + tail]

    def parse(self, response):
        print(self.id_list)
        for user_id in self.id_list:
            yield scrapy.Request(self.url + self.medium + str(user_id) + self.tail, callback=self.parse)
            # 提取用户id
            userid = response.xpath('//a[@class="relate_links"]/@href').extract()[0]
            #在song_name里找
            for each in response.xpath('//td[@class="song_name"]'):

                item = XiamiItem()
                
                #提取id列表
                musicid = each.xpath('./a[1]/@href').extract()[0]
                #提取名
                musicname = each.xpath('./a[1]/text()').extract()[0]

                item['userid'] = userid.replace('/space/collect-fav/u/', '').strip()#.encode('utf-8')
                item['musicid'] = musicid.replace('http://www.xiami.com/song/', '')#.strip().encode('utf-8')
                item['musicname'] = musicname#.encode('utf-8')

                # 打印用户id所在href（检测是否获取到了）
                # print (userid)
                # 打印抽取后的用户id（检测是否获取到了,之前加了encode导致变为bytes版本数据（前有b标识））
                # print(item['userid'])

                yield item


            #如果有当前页数这一项，打印当前页数
            if response.xpath('//a[@class="p_num p_curpage"]/text()') != []:#is not None:
                curpage = response.xpath('//a[@class="p_num p_curpage"]/text()').extract()[0]
                print('第%s页' %(curpage))

            print(response.xpath('//a[@class="p_redirect_l"]'))

            #条件，判断是否有下一页
            if response.xpath('//a[@class="p_redirect_l"]') !=[]:#is not None:
                nextpage = response.xpath('//a[@class="p_redirect_l"]/@href').extract()[0]
                yield scrapy.Request(self.url + str(nextpage), callback=self.parse)

        	#while not not soup.find('a', class_='p_redirect_l'):
        	#if response.xpath('//div[@id="not-exists"]/text()').extract_first() is None