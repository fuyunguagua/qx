from ..scrapy_redis.spiders import RedisSpider
from ..items import Pbdnof58Loader
from ..redis import Redis
from scrapy import log
from ..items import QYURLItem
import re
from ..utils import Redis_utils
from time import sleep
from scrapy.selector import Selector

#pull urls from contry list,restract urls and push to redis
class QYCityUrlSpider(RedisSpider):
    name = 'qy_city_spider'
    redis_key = 'myspider:qyconpage_urls'

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domans = filter(None, domain.split(','))
        super(QYCityUrlSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        selector = Selector(response)
        City_Urls = selector.re(u'{id:\'\d*\',name:\'\D*\',url:\'(http:.*)\'}')
        r = Redis()
        if City_Urls:
            r.lpush('myspider:qycitypage_urls', *City_Urls)