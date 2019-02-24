# _*_ coding:utf-8 _*_ 
# 从普通版的音乐人id爬其作为虾米音乐人的id（主页：http://i.xiami.com/gar，都保存下）

# 数据结构：orders，artist
# 结果数据结构：orders，artist，ixiami

from time import sleep
import random
import requests



def crawl():

    headers ={
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    # 'Connection': 'keep-alive',
    # 'Cookie': 'bdshare_firstime=1457956409801; __gads=ID=73e2e181b58fc6ca:T=1458218451:S=ALNI_MZgnmuYI1p51djQ39138Xad_JwhnA; gid=146666627945914; cna=kpNqD0pXzCMCAbeBxeP/NkFD; _unsign_token=e7d551a7e80adc9d4f165493f2bb67df; l=AsvLHF5BJvLL7rKoCjpPxUxG22W0Tt/i; UM_distinctid=15ca6e9fb192a5-039906cad08c76-5393662-1fa400-15ca6e9fb1abfd; XMPLAYER_volumeValue=0.29; _xiamitoken=7560ef23cae9dbe7ae1a9e020fd651ff; CNZZDATA921634=cnzz_eid%3D1794944975-1497448121-null%26ntime%3D1506317558; CNZZDATA2629111=cnzz_eid%3D120392506-1497448882-null%26ntime%3D1506318424; player_opencount=0; __utma=251084815.472418863.1506320932.1506320932.1506320932.1; __utmz=251084815.1506320932.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/note/288039019/; t_sign_auth=1; isg=AqamDWWBw_k4k5Zq1J4yw4659xyElkEP2bZ6gJBP20mmE0Ut5RIlUeehHThl; login_method=emaillogin; member_auth=2DDIGIZJvWlmi6STTN8xcnAe5%2BXWHTHQxopWibV%2BtlRwI9wKa9D%2BwauQQQxK3iWQoGHKgBdLebuakWGIk0B1SBI; user=13726538%22%E5%A4%9A%E7%94%B0%E4%BE%BF%E5%88%A9%E5%B1%8B%22images%2Favatar_new%2F274%2F53%2F13726538%2F13726538_1364534280_1.jpg%220%2210466%22%3Ca+href%3D%27http%3A%2F%2Fwww.xiami.com%2Fwebsitehelp%23help9_3%27+%3ELv7%3C%2Fa%3E%2215%222%2241%22f1046dc45f%221506333864',
    # 'DNT': '1',
    # 'Host': 'www.xiami.com',
    # 'Referer': 'http://www.xiami.com/',
    # 'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
        }


    urls = 'http://www.xiami.com/artist/'

    test=[] 
    with open('info_artist.txt','r', encoding="UTF-8") as f2:
        for each in f2:
            test.append(each.strip())
    a = []
    b = []
    for two in test:
    	a.append(two.split('\t')[0])# order of ID of an artist
    	b.append(two.split('\t')[1])# ID of an artist

    for artist in b:
        urln = urls +  str(artist)
        orders = str(a[b.index(artist)])
        print(artist)
        try:
            rs = requests.get(urln,headers = headers,timeout = 10)
            location = rs.url
            if rs.status_code == 200:
                print(rs.status_code)
                print(location)
                demo = 'i.xiami'
                if demo in location:
                    ixiami = location
                    print(ixiami)
                    with open('302.txt', 'a', encoding="UTF-8") as f:
                        f.write(orders + '\t' + artist + '\t' + ixiami + '\n')
                else:
                    with open('left.txt', 'a', encoding="UTF-8") as f:
                        f.write(orders + '\t' + artist + '\n')
            elif rs.status_code == 404:
                print(rs.status_code)
                print(location)         
                with open('404.txt', 'a', encoding="UTF-8") as f:
                    f.write(orders + '\t' + artist + '\n')


        # 超时，报错
        except requests.exceptions.ConnectionError:#socket.timeout as e:
            NETWORK_STATUS = False
            print(NETWORK_STATUS)
            print('of artist:' + artist)
            with open('timeout.txt', 'a', encoding="UTF-8") as f:
                        f.write(orders + '\t' + artist + '\n')
        except requests.exceptions.ReadTimeout:#socket.timeout as e:
            NETWORK_STATUS = False
            print(NETWORK_STATUS)
            print('of artist:' + artist)
            with open('timeout.txt', 'a', encoding="UTF-8") as f:
                        f.write(orders + '\t' + artist + '\n')

        with open ("info_artist.txt",'r+') as dele_r:
            Dele = dele_r.readlines()
        with open ("info_artist.txt", 'w+') as dele_w:
            dele_w.write(''.join(Dele[1:]))


        sleep(random.uniform(1.6,2.0))


if __name__ == '__main__':
    # for i in range(0,50):
    crawl()