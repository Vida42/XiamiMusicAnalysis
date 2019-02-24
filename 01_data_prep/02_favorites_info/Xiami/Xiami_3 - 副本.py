# _*_ coding:utf-8 _*_ 
# 正改·改
# 在2_1基础上加入间隔延时与未响应处理
import urllib 
from bs4 import BeautifulSoup
from time import sleep
import random
import socket


def crawl():
#    user_agent = [
#    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
#    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
#    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
#    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
#    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
#    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
#    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
#    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
#    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
#    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
#    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
#    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
#    ]
    headers ={    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Connection': 'keep-alive',
    'Cookie': 'bdshare_firstime=1457956409801; __gads=ID=73e2e181b58fc6ca:T=1458218451:S=ALNI_MZgnmuYI1p51djQ39138Xad_JwhnA; gid=146666627945914; cna=kpNqD0pXzCMCAbeBxeP/NkFD; _unsign_token=e7d551a7e80adc9d4f165493f2bb67df; l=AsvLHF5BJvLL7rKoCjpPxUxG22W0Tt/i; UM_distinctid=15ca6e9fb192a5-039906cad08c76-5393662-1fa400-15ca6e9fb1abfd; XMPLAYER_volumeValue=0.29; _xiamitoken=7560ef23cae9dbe7ae1a9e020fd651ff; CNZZDATA921634=cnzz_eid%3D1794944975-1497448121-null%26ntime%3D1506317558; CNZZDATA2629111=cnzz_eid%3D120392506-1497448882-null%26ntime%3D1506318424; player_opencount=0; __utma=251084815.472418863.1506320932.1506320932.1506320932.1; __utmz=251084815.1506320932.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/note/288039019/; t_sign_auth=1; isg=AqamDWWBw_k4k5Zq1J4yw4659xyElkEP2bZ6gJBP20mmE0Ut5RIlUeehHThl; login_method=emaillogin; member_auth=2DDIGIZJvWlmi6STTN8xcnAe5%2BXWHTHQxopWibV%2BtlRwI9wKa9D%2BwauQQQxK3iWQoGHKgBdLebuakWGIk0B1SBI; user=13726538%22%E5%A4%9A%E7%94%B0%E4%BE%BF%E5%88%A9%E5%B1%8B%22images%2Favatar_new%2F274%2F53%2F13726538%2F13726538_1364534280_1.jpg%220%2210466%22%3Ca+href%3D%27http%3A%2F%2Fwww.xiami.com%2Fwebsitehelp%23help9_3%27+%3ELv7%3C%2Fa%3E%2215%222%2241%22f1046dc45f%221506333864',
    'DNT': '1',
    'Host': 'www.xiami.com',
    'Referer': 'http://www.xiami.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
       # user_agent
        }


    urls = 'http://www.xiami.com'
    medium = '/space/lib-song/u/'
    tail = '/page/'

    id_list=[] 
    with open('figure3.txt','r') as f2:
        for eachline in f2:
            id_list.append(eachline.strip())

    for user_id in id_list:

        urln = urls + medium + str(user_id) + tail# + str(11)
        try:
            request=urllib.request.Request(urln,headers = headers)
            page = urllib.request.urlopen(request,timeout = 10) 
            contents = page.read() 
            soup = BeautifulSoup(contents,'lxml') #不清楚为啥要加lxml

            for tag in soup.find_all('td', class_='song_name'): 
                locate_the_music = tag.find('a')
                m_link = locate_the_music['href'].replace('http://www.xiami.com/song/', '').strip()
                m_name = locate_the_music['title']
                # print("%s\t %s\t %s" % (user_id, m_link, m_name))
                with open('test.txt', 'a', encoding="UTF-8") as f:
                    f.write(user_id + '\t' + m_link + '\t' + m_name + '\n')
            if not not soup.find('a', class_='p_num p_curpage'):
                curpage = soup.find('a', class_='p_num p_curpage').get_text()
                print('第%s页' %(curpage))     
            #爬第一页


            while not not soup.find('a', class_='p_redirect_l'):
                ne_page = soup.find('a', class_='p_redirect_l')
                id_ne_page = ne_page['href']
                url = urls + str(id_ne_page)     
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
                     with open('test.txt', 'a', encoding="UTF-8") as f:
                        f.write(user_id + '\t' + m_link + '\t' + m_name + '\n')
                curpage = soup.find('a', class_='p_num p_curpage').get_text()
                print('第%s页' %(curpage))     
                #爬这一页
                sleep(random.uniform(0.2,0.3))

        #该用户被删，报错    
        except urllib.error.HTTPError as e:
            print(e)
        # except socket.timeout as e:
        # 	print(e)
        except Exception as e:
            print(e)
            return
        with open ("figure3.txt",'r+') as dele_r:
            Dele = dele_r.readlines()
        with open ("figure3.txt", 'w+') as dele_w:
            dele_w.write(''.join(Dele[1:]))
        print(user_id)

        sleep(random.uniform(0.3,0.4))

#打印个表头
# print(u'我收藏的歌曲:\n  用户id\t 歌曲链接\t 歌曲名 ')
#读取用户ID列表



if __name__ == '__main__':
    crawl()