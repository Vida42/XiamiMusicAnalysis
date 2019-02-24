# _*_ coding:utf-8 _*_ 

import scrapy
from Xinfo.items import XiamiItem

class XiamiSpider(scrapy.Spider):  
	name = "xiami"
	allowed_domains = ["xiami.com"]
	url = 'http://www.xiami.com/u/'# 待爬地址头
	# 将待爬ID读入列表
	test = [] 
	with open('info_user.txt','r',encoding = 'utf-8') as f:
		for each in f:
			test.append(each.strip())
	Dele = list(test)


	# 定义初始地址集，urls为初始地址集：所有待爬音乐的专属页面
	def start_requests(self):
		urls = []
		for whichuser in self.test:
			re_url = self.url + str(whichuser)
			urls.append(re_url)
		for lib_url in urls:
			yield scrapy.Request(url=lib_url, cookies = {
				'bdshare_firstime':'1457956409801',
				'__gads':'ID=73e2e181b58fc6ca:T=1458218451:S=ALNI_MZgnmuYI1p51djQ39138Xad_JwhnA',
				'gid':'146666627945914',
				'cna':'kpNqD0pXzCMCAbeBxeP/NkFD',
				'_unsign_token':'e7d551a7e80adc9d4f165493f2bb67df',
				'l':'AsvLHF5BJvLL7rKoCjpPxUxG22W0Tt/i',
				'UM_distinctid':'15ca6e9fb192a5-039906cad08c76-5393662-1fa400-15ca6e9fb1abfd',
				'XMPLAYER_volumeValue':'0.29',
				'_xiamitoken':'6ade7379783e92438519c0495afe6cd2',
				'CNZZDATA921634':'cnzz_eid%3D1794944975-1497448121-null%26ntime%3D1506220358',
				'CNZZDATA2629111':'cnzz_eid%3D120392506-1497448882-null%26ntime%3D1506215824',
				't_sign_auth':'2',
				'isg':'Amxsu7AdGfiw8Az8YrzY_TD7PUoyNLuBd7RAtsatHpe-0Q_b9TEWXw0jh64T',
				'login_method':'emaillogin',
				'member_auth':'2DDIGIZJvWlmi6STTN8xcnAe5%2BXWHTHQxopWibV%2BtlRwI9wKa9D%2BwauQQQxK3iWQoGHKgBdLebuakWGIk0B1SBI',
				'user':'13726538%22%E5%A4%9A%E7%94%B0%E4%BE%BF%E5%88%A9%E5%B1%8B%22images%2Favatar_new%2F274%2F53%2F13726538%2F13726538_1364534280_1.jpg%220%2210443%22%3Ca+href%3D%27http%3A%2F%2Fwww.xiami.com%2Fwebsitehelp%23help9_3%27+%3ELv7%3C%2Fa%3E%2215%222%2241%22f1046dc45f%221506243142'
				}, callback=self.parse)


	def parse(self, response):
		usernow = str(response).replace('<200 http://www.xiami.com/u/', '').replace('>','').strip()
		if usernow in self.test:
			# 排除掉混在普通音乐人里的虾米音乐人

			for each in response.xpath('//div[@id="p_infoCount" and @class="blank15"]'):
				x1 = each.xpath('./p[1]/text()').extract()[0].strip()#信息
				# print(x1)
				x2 = each.xpath('./p[2]/span/text()').extract()[0]#加入时间
				# print(x2)
				x2x = x2.replace('加入','').strip()
				# print(x2x)
				x3 = each.xpath('./div[@class="play_count blank5 clearfix"]/div/text()').extract()[0]#播放
				# print(x3)
				x4 = each.xpath('./div[@class="p_stat blank5 clearfix"]/div/a/text()').extract()[0]#等级
				# print(x4)
				x5 = each.xpath('./div[@class="p_stat blank5 clearfix"]/text()').extract()[0].strip()# 访问次数
				# print(x5)
				x6 = each.xpath('./ul[@class="counts blank5 clearfix"]/li[1]/a/span/text()').extract()[0]# 关注
				# print(x6)
				x7 = each.xpath('./ul[@class="counts blank5 clearfix"]/li[2]/a/span/text()').extract()[0]# 粉丝
				# print(x7)
				x8 = each.xpath('./ul[@class="counts blank5 clearfix"]/li[3]/a/span/text()').extract()[0]# 分享
				# print(x8)

			item = XiamiItem()

			# 用户id
			item['userid'] = usernow
			# 综合信息
			item['cominfo'] = x1
			# 加入时间
			item['intime'] = x2x
			# 累计播放
			item['play_count'] = x3
			# 等级
			item['level'] = x4
			# 访问次数
			item['v_time'] = x5
			# 关注
			item['guanzhu'] = x6
			# 粉丝
			item['fensi'] = x7
			# 分享
			item['fenxiang'] = x8 

			yield item
			index2 = self.Dele.index(usernow)
			self.Dele.pop(index2)
			with open ("info_user.txt", 'w') as dele_w:
				for i in self.Dele:
					dele_w.write(str(i)+'\n')
			print(len(self.Dele))