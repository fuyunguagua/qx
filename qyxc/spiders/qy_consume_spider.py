from ..scrapy_redis.spiders import RedisSpider
from ..items import TrackItem
from ..restract import Restractor

class QYXingChengSpider(RedisSpider):
    name = 'qy_xingcheng_spider'
    redis_key = 'myspider:start_urls'
    #webdriver.Chrome()
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domans = filter(None, domain.split(','))
        super(QYXingChengSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        item =  TrackItem()
        item['url'] = response.url
        item['data'] = Restractor.restractXCInfo(response)
        return item





