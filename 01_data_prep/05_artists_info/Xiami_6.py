# _*_ coding:utf-8 _*_ 
# 对从普通艺人分离出的虾米音乐人爬艺人信息
# 数据结构：orders，artist，ixiami
# 结果数据结构：orders，artist，ixiami，ixiami_name，genre

import urllib 
from bs4 import BeautifulSoup
from time import sleep
import random
import socket

def randHeader():
    
    head_connection = ['Keep-Alive']
    head_user_agent = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1', 
        'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10', 
        'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13', 
        'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+', 
        'Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0', 
        'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124', 
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)']
    
    
    header = {
        'Connection': head_connection[0],
        'User-Agent': head_user_agent[random.randrange(0,len(head_user_agent))]
    }
    return header


def crawl():

    headers = randHeader()
    # 读待爬文件
    test=[] 
    with open('302.txt','r', encoding="UTF-8") as f2:
        for each in f2:
            test.append(each.strip())
    # 切为三部分
    a = []# orders
    b = []# artist
    c = []# ixiami
    for two in test[0:50]:
        a.append(two.split('\t')[0])# order of ID of an artist
        b.append(two.split('\t')[1])# ID of an artist
        c.append(two.split('\t')[2])# ID of an ixiami

    for ixiami in c:
        urln = str(ixiami)
        orders = str(a[c.index(ixiami)])
        artist = str(b[c.index(ixiami)])
        # print(ixiami)
        try:
            request=urllib.request.Request(urln,headers = headers)
            page = urllib.request.urlopen(request,timeout = 5)
            contents = page.read()
            soup = BeautifulSoup(contents,'lxml')

            # 如果是虾米音乐人
            if not not soup.find('div', class_='glory-title-wrap'):
                # 获取艺人名
                for tag in soup.find_all('div', class_='glory-title-wrap'): 
                    locate_name = tag.find('h1')
                    ixiami_name = locate_name.get_text()
                    print(ixiami_name)
                # 获取风格
                for tag2 in soup.find_all('div', id='artist_info'): 
                    locate_genre = tag2.find_all('a', class_=None)
                    genre0 = []
                    for many in locate_genre:
                        genre0.append(many['href'].replace('http://www.xiami.com/genre/detail/sid/', ',').strip())#去掉多余字段，用，隔开多种风格
                    genre = ''.join(genre0).lstrip(',')#拼成一条字符串
                # 保存爬取信息
                with open('result.txt', 'a', encoding="UTF-8") as f:
                    f.write(orders + '\t' + artist + '\t' + ixiami + '\t' + ixiami_name + '\t' + genre + '\n')
            # 否则另存
            else:
                with open('left.txt', 'a', encoding="UTF-8") as f:
                    f.write(orders + '\t' + artist + '\t' + ixiami + '\n')

        #该用户被删，报错，另存
        except urllib.error.HTTPError as e:
            print(e)
            with open('404.txt', 'a', encoding="UTF-8") as f:
                f.write(orders + '\t' + artist + '\t' + ixiami + '\n')
        # 超时，报错，另存
        except socket.timeout as e:
            print(e)
            with open('timeout.txt', 'a', encoding="UTF-8") as f:
                f.write(orders + '\t' + artist + '\t' + ixiami + '\n')

        # 爬完的删掉
        with open ("302.txt",'r+') as dele_r:
            Dele = dele_r.readlines()
        with open ("302.txt", 'w+') as dele_w:
            dele_w.write(''.join(Dele[1:]))

        # 设置爬取间隔
        sleep(random.uniform(1.7,2.0))


if __name__ == '__main__':
    for i in range(0,50):
        crawl()