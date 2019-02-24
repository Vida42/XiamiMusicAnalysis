# 虾米爬虫测试版本1

# _*_ coding:utf-8 _*_ 
import urllib 
import numpy
import re 
from bs4 import BeautifulSoup


def crawl(user_id): 
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    urls = 'http://www.xiami.com'
    medium = '/space/lib-song/u/'
    tail = '/page/'
    urln = urls + medium + user_id + tail #+ str(70)
    try:
        request=urllib.request.Request(urln,headers = headers)
        page = urllib.request.urlopen(request) 
        contents = page.read() 
        soup = BeautifulSoup(contents,'lxml') #不清楚为啥要加lxml

        ne_page = soup.find('a', class_='p_redirect_l')
        url = urln


        while not not ne_page:#如果有下一页#判断None能否简洁？
            request=urllib.request.Request(url,headers = headers)
            page = urllib.request.urlopen(request) 
            contents = page.read() 
            soup = BeautifulSoup(contents,'lxml') #不清楚为啥要加lxml
            
            for tag in soup.find_all('td', class_='song_name'): 
                 locate_the_music = tag.find('a')
                 m_link = locate_the_music['href'].replace('http://www.xiami.com/song/', '').strip()
                 m_name = locate_the_music['title']
                 # print("%s\t %s\t %s" % (user_id, m_link, m_name))
                 # with open('666.txt', 'a', encoding="UTF-8") as f:
                 #    f.write(user_id + '\t' + m_link + '\t' + m_name + '\n')
            curpage = soup.find('a', class_='p_num p_curpage').get_text()
            print('第%s页' %(curpage))
            ne_page = soup.find('a', class_='p_redirect_l')
            if not not ne_page:
                id_ne_page = ne_page['href']
                url = urls + str(id_ne_page)
    except urllib.error.HTTPError as e:
        print(e.code)


print(u'我收藏的歌曲:\n  用户id\t 歌曲链接\t 歌曲名 ')

second=[] 
with open('figure3.txt','r') as f2:
	for eachline in f2:
		second.append(eachline.strip()) 
#print(second)


if __name__ == '__main__':
#    third = numpy.loadtxt('figure3.txt',dtype=int)
    for id_x in second:
#    for id_x in range(1,2):
        crawl(str(id_x))
        # crawl(str(5435645))