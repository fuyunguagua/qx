from ..scrapy_redis.spiders import RedisSpider
from ..items import Pbdnof58Loader
from ..redis import Redis
from qx.qyxc.utils import Redis_utils

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
        if City_Urls:
            Redis_utils.server.lpush('myspider:qycitypage_urls', *City_Urls)