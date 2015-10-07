

import frontera

from frontera.core.manager import FrontierManager



#SPIDER_MIDDLEWARES = {}
#DOWNLOADER_MIDDLEWARES = {}

#BACKEND = 'distributed_frontera.backends.hbase.HBaseBackend'

BACKEND = 'frontera.contrib.backends.sqlalchemy.FIFO'
SQLALCHEMYBACKEND_ENGINE = 'sqlite:///frontier.db'

HTTPCACHE_ENABLED = False
REDIRECT_ENABLED = True
COOKIES_ENABLED = False
#DOWNLOAD_TIMEOUT = 20
RETRY_ENABLED = False

CONCURRENT_REQUESTS = 20
CONCURRENT_REQUESTS_PER_DOMAIN = 20

LOGSTATS_INTERVAL = 10

SPIDER_MIDDLEWARES = {}
DOWNLOADER_MIDDLEWARES = {}





SPIDER_MIDDLEWARES.update({
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerSpiderMiddleware': 699,
})


DOWNLOADER_MIDDLEWARES.update({
    'frontera.contrib.scrapy.middlewares.schedulers.SchedulerDownloaderMiddleware': 1000,
})

SCHEDULER = 'frontera.contrib.scrapy.schedulers.frontier.FronteraScheduler'


# Import distributed_frontera worker settings
