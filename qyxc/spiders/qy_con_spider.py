
from ..scrapy_redis.spiders import RedisSpider
from ..items import Pbdnof58Loader
from ..redis import Redis
from ..items import ContryItem
import re
from ..utils import Redis_utils
from time import sleep
from scrapy.selector import Selector
from qx.qyxc.utils import Redis_utils

class QYConUrlSpider(RedisSpider):
    name = 'qy_con_spider'
    redis_key = 'myspider:qy_index_urls'

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domans = filter(None, domain.split(','))
        super(QYConUrlSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        selector = Selector(response)
        p1 = re.compile('<ul class="clearfix" style="display:none;">(.*?)</ul>', re.S)  # 这个正则表达式会找的7个匹配<ul></ul>
        rp1 = selector.re(p1)
        p2 = re.compile(u'<a data-id="\d*" data-key="\D*" href="(http://.*)">(.*)</a>')
        r = Redis()
        for index, i in enumerate(rp1):
            rp2 = p2.findall(i)
            for j in rp2:
                con_item = ContryItem()
                con_item['name'] = j[1]
                con_item['url'] = j[0]
                con_item['con_id'] = index+1 #continent ID fk
                Redis_utils.server.lpush('myspider:qyconpage_urls', j[0])
                yield con_item
