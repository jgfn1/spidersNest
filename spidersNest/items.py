# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class SpidersNestItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    body = scrapy.Field()
    paragraph_count = scrapy.Field()
    word_count = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    tags = scrapy.Field()
    url = scrapy.Field()
    pass
