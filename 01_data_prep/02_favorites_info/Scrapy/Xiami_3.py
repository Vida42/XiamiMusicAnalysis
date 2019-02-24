#2017.9.22下午15点，原名“正确版本虾米”
import scrapy
from myXspider.items import XiamiItem

class XiamiSpider(scrapy.Spider):  
    name = "xiami"
    allowed_domains = ["xiami.com"]
    url = 'http://www.xiami.com'
    # 将待爬ID读入列表
    id_list=[] 
    with open('figure3.txt','r') as f2:
        for eachline in f2:
            id_list.append(eachline.strip())
    Dele = id_list
    print(id_list)
    nextpage = 1

    def start_requests(self):
        
        # url = 'http://www.xiami.com'
        medium = '/space/lib-song/u/'

        
        #urls为初始地址集——所有待爬用户的音乐库页面
        urls = []
        for whichuser in self.id_list:
            re_url = self.url + medium + str(whichuser)
            urls.append(re_url)
        for a in urls:
            print(a)   
        for lib_url in urls:
            yield scrapy.Request(url=lib_url, callback=self.parse)

    def parse(self, response):

        # 提取用户id
        print('i cant believe')
        print(response.xpath('//a[@class="relate_links"]/@href').extract())
        userid_1 = response.xpath('//a[@class="relate_links"]/@href').extract()[0]
        userid = userid_1.replace('/space/collect-fav/u/', '').strip()#.encode('utf-8')
        #在song_name里找
        for each in response.xpath('//td[@class="song_name"]'):

            item = XiamiItem()
            
            #提取id列表
            musicid = each.xpath('./a[1]/@href').extract()[0]
            #提取名
            musicname = each.xpath('./a[1]/text()').extract()[0]

            item['userid'] = userid
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
            self.nextpage += 1
            tonext = 'http://www.xiami.com' + '/space/lib-song/u/' +  str(userid) + '/page/' + str(self.nextpage)
            print(str(self.nextpage))
            print(str(tonext))
            yield scrapy.Request(str(tonext), callback=self.parse)
        # if response.xpath('//a[@class="p_redirect_l"]') !=[]:#is not None:
        #     nextpage = response.xpath('//a[@class="p_redirect_l"]/@href').extract()[0]
        #     tonext = 'http://www.xiami.com' + str(nextpage)
        #     print(str(nextpage))
        #     print(str(tonext))
        #     yield scrapy.Request(str(tonext), callback=self.parse)
        else:
            self.Dele.pop(self.Dele.index(str(userid)))
            with open ("figure3.txt", 'w') as dele_w:
                for i in self.Dele:
                    dele_w.write(str(i)+'\n')
            print(userid)