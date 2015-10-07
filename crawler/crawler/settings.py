# -*- coding: utf-8 -*-

# Scrapy settings for crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html



BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

USER_AGENT = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36"


DUPEFILTER=True




SPIDER_MIDDLEWARES = {}
DOWNLOADER_MIDDLEWARES = {}
CLOSESPIDER_ERRORCOUNT = 0
RETRY_ENABLED = True
RETRY_TIMES = 20
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 401, 402, 403, 408, 404]
REFERER_ENABLED = True
REDIRECT_ENABLED = True



from frontier.settings import *





