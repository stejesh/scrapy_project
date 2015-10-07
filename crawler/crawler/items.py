# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy





class POCJob(scrapy.Item):
    POC_source_url = scrapy.Field()
    POC_title = scrapy.Field()
    POC_body = scrapy.Field()
    POC_compensation = scrapy.Field()
    POC_notices = scrapy.Field()

class Business(scrapy.Item):
    meta_data = scrapy.Field()
    business_name = scrapy.Field()
    contact_number = scrapy.Field()
    location_data = scrapy.Field()
    business_email = scrapy.Field()
    raw_business_categories = scrapy.Field()
    restaurant_menu_data = scrapy.Field()
    business_review_data = scrapy.Field()
    business_query_data = scrapy.Field()
    business_hours = scrapy.Field()
    business_description = scrapy.Field()
    business_detailed_description = scrapy.Field()
    business_website = scrapy.Field()
    established_year = scrapy.Field()
    number_of_employees = scrapy.Field()
    payment_methods = scrapy.Field()

#Consumer complaint object
class ReviewObject(scrapy.Item):
    user_name = scrapy.Field()
    user_profile_url = scrapy.Field()
    review_source_url = scrapy.Field()
    review_date = scrapy.Field()
    review_title = scrapy.Field()
    review_content = scrapy.Field()
    review_rating = scrapy.Field()
