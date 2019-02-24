# 虾米爬虫测试版本0

# _*_ coding:utf-8 _*_ 
import urllib 
import re 
from bs4 import BeautifulSoup


def crawl(url): 
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    request=urllib.request.Request(url,headers = headers)
    page = urllib.request.urlopen(request) 
    contents = page.read() 
    soup = BeautifulSoup(contents) 
     
    for tag in soup.find_all('td', class_='song_name'): 
        locate_the_music = tag.find('a')
        m_link = locate_the_music['href'].replace('http://www.xiami.com/song/', '').strip()
        m_name = locate_the_music['title']
        locate_the_band = tag.find('a', class_='artist_name')
#        b_link = locate_the_band['href'].replace('http://www.xiami.com/artist/', '').strip()
        b_name = locate_the_band['title']
        print("%s\t %s\t %s " % (m_link, m_name,  b_name))
#        with open('3.txt', 'a', encoding="UTF-8") as f:
#            f.write(m_link + '\t')
#            f.write(m_name + '\t')
#            f.write(b_link + '\t')
#            f.write(b_name + '\n')
#        print(locate)

print(u'我收藏的歌曲及其歌手:\n  歌曲链接\t 歌曲名\t 歌手名')

if __name__ == '__main__':
    for user_id in range(1,3):
        for page_id in range(1,3):
            crawl('http://www.xiami.com/space/lib-song/u/'+str(user_id)+'/page/'+str(page_id))
    


#artists = body.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'})