# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BricksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	price = scrapy.Field()
	bhk = scrapy.Field()
	address = scrapy.Field()
	bedroom = scrapy.Field()
	area = scrapy.Field()
	pricepersquare = scrapy.Field()
	scociety = scrapy.Field()
	Carpetarea = scrapy.Field()
	superarea = scrapy.Field()
	status = scrapy.Field()
	transaction = scrapy.Field()
	amenities = scrapy.Field()
	connectivity = scrapy.Field()
	descriptitles = scrapy.Field()
	descripvalues = scrapy.Field()
	PropertyID = scrapy.Field()
	propertyinfotitle = scrapy.Field()
	propertyinfovalues = scrapy.Field()
