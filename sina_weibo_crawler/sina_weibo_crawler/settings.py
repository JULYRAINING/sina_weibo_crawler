# -*- coding: utf-8 -*-

# Scrapy settings for sina_weibo_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'sina_weibo_crawler'

SPIDER_MODULES = ['sina_weibo_crawler.spiders']
NEWSPIDER_MODULE = 'sina_weibo_crawler.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sina_weibo_crawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', \
#   'Accept-Encoding':'gzip, deflate, sdch', \
#   'Accept-Language':'zh-CN,zh;q=0.8', \
#   
#   'Cookie':'_T_WM=319cbc22744b116eab733bc7d333db1d; ALF=1478572923; SCF=AthJusqLha77m3xTm_nqdTfXnx3HjL8KdD1gaMmcxsDvgS4pXypRqXO9pRWPq3KW8OqP9wuW3SnOfLbyXTzDPSc.; SUB=_2A256_ZFaDeTxGeBO6FIU8y_IwzuIHXVWAT8SrDV6PUJbktANLVbZkW2RDCimDPVE5o4M07vq2mCnAxgTrw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFwiYgeyUKaOOAT_T6--xQn5JpX5o2p5NHD95Qcehe7SKepShnNWs4Dqcj_i--RiK.ciKnNi--Ni-8hiK.pi--fi-2Xi-2Ni--RiKysiKnpi--NiKnpi-zf; SUHB=0y0JtkK8I0YPZJ; SSOLoginState=1475993866', \
#   'Host':'weibo.cn', \
#   'Proxy-Connection':'keep-alive', \
#   'Referer':'http://weibo.cn/ermanwei', \
#   'Upgrade-Insecure-Requests':'1', \
#   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36' \
#            
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'sina_weibo_crawler.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'sina_weibo_crawler.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'sina_weibo_crawler.pipelines.JsonWriterPipeline': 300,
    'sina_weibo_crawler.pipelines.MongoPipeline': 301,
}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "local"
MONGODB_COLLECTION = "items"



# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
