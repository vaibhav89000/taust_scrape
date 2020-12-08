# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TaustItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nimi = scrapy.Field()
    kood = scrapy.Field()
    address = scrapy.Field()
    telefon = scrapy.Field()
    email = scrapy.Field()

