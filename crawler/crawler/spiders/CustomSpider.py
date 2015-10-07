
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import logging
import sys
reload(sys)
# for dealing with non-unicode letters
sys.setdefaultencoding("utf-8")








class CustomSpider(CrawlSpider):
	name = "CustomSpider"
	allowed_domains = ["www.yelp.com", "yelp.com"]

	# Start urls
	start_urls = [
		"http://www.yelp.com/biz/blackwood-san-francisco-3"
	]

	rules = [
		Rule(LinkExtractor(allow=('www\.yelp\.com\/biz\/.+')),follow=True,callback="parse_data")
	]



	def parse_data(self, response):
	   print "Inside url {0}".format(response.url)






