# _*_ coding:utf-8 _*_ 

import scrapy
from Xinfo.items import XiamiItem

class XiamiSpider(scrapy.Spider):  
	name = "xiami"
	allowed_domains = ["xiami.com"]
	url = 'http://www.xiami.com/artist/'# 待爬地址头
	# 将待爬ID读入列表
	test = [] 
	with open('info_artist1.txt','r',encoding = 'utf-8') as f:
		for each in f:
			test.append(each.strip())
	Dele = list(test)
	a = []
	b = []
	for two in test:
		a.append(two.split('\t')[0])# order of ID of an artist
		b.append(two.split('\t')[1])# ID of an artist
	Dele2 = list(b)


	# 定义初始地址集，urls为初始地址集：所有待爬音乐的专属页面
	def start_requests(self):
		urls = []
		for whichartist in self.b:
			re_url = self.url + str(whichartist)
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
		artistnow = str(response).replace('<200 http://www.xiami.com/artist/', '').replace('>','').strip()
		if artistnow in self.b:
			# 排除掉混在普通音乐人里的虾米音乐人
			index3 = self.b.index(artistnow)
			# print(index3)
			for each in response.xpath('//div[@class="scalable clearfix"]'):
				artist_name = each.xpath('./div[1]/h1/text()').extract()[0]#artist_name
				print(artist_name)

				# 艺人栏按地区，风格，档案排，且地区，风格会缺失，缺失时tr标签也不保留
			for each2 in response.xpath('//div[@id="artist_info"]'):
				genre_address = each2.xpath('./table[1]/tr[2]/td[2]/a[not(@class)]/@href').extract()#get every genre
				# print(genre_address)
				genre0 = []
				for many in genre_address:
					genre0.append(many.replace('/genre/detail/sid/', ',').strip())#去掉多余字段，用，隔开多种风格
				genre = ''.join(genre0).lstrip(',')#拼成一条字符串
				print(genre)
				# print('风格：'+ genre)

			item = XiamiItem()

			item['orders'] = str(self.a[index3])
			item['artist'] = artistnow
			item['artist_name'] = artist_name
			item['genre'] = genre

			yield item
			# index2 = self.Dele2.index(artistnow)
			# self.Dele2.pop(index2)
			# self.Dele.pop(index2)
			# with open ("info_artist1.txt", 'w') as dele_w:
			# 	for i in self.Dele:
			# 		dele_w.write(str(i)+'\n')
			# print(len(self.Dele))