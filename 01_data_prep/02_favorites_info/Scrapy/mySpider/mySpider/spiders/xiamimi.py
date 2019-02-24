    # _*_ coding:utf-8 _*_ 
import urllib 
import re 


def crawl(user_id): 
    # headers = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    # }
    # urls = 'http://www.xiami.com'
    # medium = '/space/lib-song/u/'
    # tail = '/page/'
    # urln = urls + medium + user_id + tail
    try:
        # request=urllib.request.Request(urln,headers = headers)
        # page = urllib.request.urlopen(request) 
        # contents = page.read() 
        # soup = BeautifulSoup(contents,'lxml') #不清楚为啥要加lxml

        for tag in soup.find_all('td', class_='song_name'): 
            locate_the_music = tag.find('a')
            m_link = locate_the_music['href'].replace('http://www.xiami.com/song/', '').strip()
            m_name = locate_the_music['title']
            # print("%s\t %s\t %s" % (user_id, m_link, m_name))
            with open('1.txt', 'a', encoding="UTF-8") as f:
                f.write(user_id + '\t' + m_link + '\t' + m_name + '\n')
        if not not soup.find('a', class_='p_num p_curpage'):
            curpage = soup.find('a', class_='p_num p_curpage').get_text()
            print('第%s页' %(curpage))     
        #爬第一页


        while not not soup.find('a', class_='p_redirect_l'):
            ne_page = soup.find('a', class_='p_redirect_l')
            id_ne_page = ne_page['href']
            # url = urls + str(id_ne_page)     
            #如果有下页，进入下一页#判断None能否简洁？
            request=urllib.request.Request(url,headers = headers)
            page = urllib.request.urlopen(request) 
            contents = page.read() 
            soup = BeautifulSoup(contents,'lxml') #不清楚为啥要加lxml
            
            for tag in soup.find_all('td', class_='song_name'): 
                 locate_the_music = tag.find('a')
                 m_link = locate_the_music['href'].replace('http://www.xiami.com/song/', '').strip()
                 m_name = locate_the_music['title']
                 # print("%s\t %s\t %s" % (user_id, m_link, m_name))
                 with open('1.txt', 'a', encoding="UTF-8") as f:
                    f.write(user_id + '\t' + m_link + '\t' + m_name + '\n')
            curpage = soup.find('a', class_='p_num p_curpage').get_text()
            print('第%s页' %(curpage))     
            #爬这一页

    #该用户被删，报错    
    # except urllib.error.HTTPError as e:
    #     print(e)

#打印个表头
print(u'我收藏的歌曲:\n  用户id\t 歌曲链接\t 歌曲名 ')
#读取用户ID列表
id_list=[] 
with open('Xu2_1.txt','r') as f2:
    for eachline in f2:
        id_list.append(eachline.strip())


if __name__ == '__main__':
    for id_x in id_list:
        crawl(str(id_x))
        with open ("Xu2_1.txt",'r+') as dele_r:
            Dele = dele_r.readlines()
        with open ("Xu2_1.txt", 'w+') as dele_w:
            dele_w.write(''.join(Dele[1:]))
        print(id_x)