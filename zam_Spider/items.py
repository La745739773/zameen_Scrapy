# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZamSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()=
    Title = scrapy.Field()
    Address = scrapy.Field()
    Longitude = scrapy.Field()
    Latitude = scrapy.Field()
    Type = scrapy.Field()
    Price = scrapy.Field()
    Location = scrapy.Field()
    Baths = scrapy.Field()
    Area = scrapy.Field()
    Purpose = scrapy.Field()
    Bedrooms = scrapy.Field()
    Added = scrapy.Field()



    #Details = scrapy.Field()
    pass
