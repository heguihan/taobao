# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field


class TaobaoproductItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nid = Field()
    title = Field()
    raw_title = Field()
    detail_url = Field()
    view_price = Field()
    view_fee = Field()
    item_loc = Field()
    view_sales = Field()
    comment_count = Field()
    user_id = Field()
    nick = Field()
    comment_url = Field()
    shopLink = Field()
    
