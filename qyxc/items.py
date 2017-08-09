# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from sched import scheduler

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join


class QYURLItem(scrapy.Item):
    # define the fields for your item here like:
    journey_name = scrapy.Field()
    url = scrapy.Field()
    day= scrapy.Field()
    line = scrapy.Field()
    date = scrapy.Field()
    lable = scrapy.Field()

class ContryItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    con_id = scrapy.Field()#洲的ID作为外键


class Pbdnof58Loader(ItemLoader):
    default_item_class = QYURLItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()