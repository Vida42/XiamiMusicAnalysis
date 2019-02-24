# -*- coding: utf-8 -*-

# Scrapy settings for Xinfo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import random

BOT_NAME = 'Xinfo'

SPIDER_MODULES = ['Xinfo.spiders']
NEWSPIDER_MODULE = 'Xinfo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_0 like Mac OS X; en-us) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5A347 Safari/525.200'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 7

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = random.uniform(1.1, 1.23)
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 8
CONCURRENT_REQUESTS_PER_IP = 6

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  "Cookie":"bdshare_firstime=1457956409801; __gads=ID=73e2e181b58fc6ca:T=1458218451:S=ALNI_MZgnmuYI1p51djQ39138Xad_JwhnA; gid=146666627945914; cna=kpNqD0pXzCMCAbeBxeP/NkFD; _unsign_token=e7d551a7e80adc9d4f165493f2bb67df; l=AsvLHF5BJvLL7rKoCjpPxUxG22W0Tt/i; UM_distinctid=15ca6e9fb192a5-039906cad08c76-5393662-1fa400-15ca6e9fb1abfd; XMPLAYER_volumeValue=0.29; _xiamitoken=6ade7379783e92438519c0495afe6cd2; join_from=0zqfTI9Kv2Ew3f7BEdw; login_method=emaillogin; member_auth=g2nISIpOuGgzi%2FOUSdxkICEc4bLcEjmDlt9YhuYr4QVwcooBMtarkKuURghN3iSWkY%2BBs2sfeO7RkzbDoQ; user=5435645%22%E7%AE%97%E6%B3%95%E5%AF%BC%E8%AE%BA%22images%2Favatar_new%2F108%2F71%2F5435645%2F5435645_1313412093_1.jpg%220%2241011%22%3Ca+href%3D%27http%3A%2F%2Fwww.xiami.com%2Fwebsitehelp%23help9_3%27+%3ELv9%3C%2Fa%3E%22165%22449%2230467%2241508246aa%221506090257; t_sign_auth=1605; CNZZDATA921634=cnzz_eid%3D1794944975-1497448121-null%26ntime%3D1506085358; CNZZDATA2629111=cnzz_eid%3D120392506-1497448882-null%26ntime%3D1506086224; isg=AoeH6tFzktu4iBdtXYVjvHfCFjv9nfAg0B27x1l0qZY9yKaKYV2jvqyKHL9s"
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   'Xinfo.middlewares.RotateUserAgentMiddleware': 1,
}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Xinfo.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Xinfo.pipelines.XiamiPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5.0
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60.0
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
