# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseTransactionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class HouseItem(scrapy.Item):
    title_urls = scrapy.Field()
    titles = scrapy.Field()
    moneys = scrapy.Field()
    looks = scrapy.Field()
    sizes = scrapy.Field()
    url_title = scrapy.Field()
    regions1 = scrapy.Field()
    regions2 = scrapy.Field()
    figure_url = scrapy.Field()
    figure_url_path = scrapy.Field()