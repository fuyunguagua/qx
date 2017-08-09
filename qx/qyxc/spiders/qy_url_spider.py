from ..scrapy_redis.spiders import RedisSpider
from ..items import Pbdnof58Loader
from ..redis import Redis
from scrapy import log
from ..items import QYURLItem
import re
from ..utils import Redis_utils
from time import sleep
from scrapy.selector import Selector
class QYUrlSpider(RedisSpider):
    '''spider that reads urls from redis queue (myspider:start_urls).'''
    name = 'myspider_qypage'
    redis_key = 'myspider:qycitypage_urls'

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domans = filter(None, domain.split(','))
        super(QYUrlSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        selector = Selector(response)
        PageUrl = None
        #抓到下一页URL
        try:
            PageUrl = selector.re("href=\"(http:.*\d)\" class=\"ui_page_item ui_page_next\"")[0]
        except IndexError:
            self.log('One done!'+response.url, level=log.INFO)
        #抓取本页的15个行程概览
        divitems = selector.xpath("//div[@class='items']").extract()
        for item in divitems:
            result = QYURLItem()
            journey_name_pattern = re.compile(u'<dd>(.*)</dd>')
            url_pattern = re.compile('<a href=\"(//.*)\" class.*>')
            day_pattern = re.compile('<strong>(\d*)</strong>')
            line_pattern = re.compile('<p>(.*)</p>')
            date_pattern = re.compile(r'<dt>(20.*) 出发</dt>')
            lable_pattern = re.compile('<strong>(\W*)</strong>')
            result['journey_name'] = journey_name_pattern.findall(item)
            result['url'] = url_pattern.findall(item)
            result['day'] = day_pattern.findall(item)
            result['line'] = line_pattern.findall(item)
            result['date'] = date_pattern.findall(item)
            result['lable'] = lable_pattern.findall(item)
            yield result
       # self.log(PageUrl, level=log.DEBUG)
        r = Redis()
        if PageUrl != None:
            r.lpush('myspider:qycitypage_urls', PageUrl)
            sleep(1)
        urls = response.xpath('//a[contains(@class, "link")]/@href').extract()
        urls = list(filter(lambda x: x.startswith('//'), urls))
        print("长度为：" + str(len(urls)))
        for url in urls:
            r.lpush('myspider:start_urls', 'http:'+url)