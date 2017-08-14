from twisted.internet import reactor,defer
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from qx.qyxc.spiders.qy_url_spider import QYUrlSpider
from qx.qyxc.spiders.qy_con_spider import QYConUrlSpider
from qx.qyxc.spiders.qy_city_spider import QYCityUrlSpider
from qx.qyxc.spiders.qy_consume_spider import QYXingChengSpider




configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
setting = get_project_settings()
runner = CrawlerRunner(setting)

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(QYConUrlSpider)
    yield runner.crawl(QYCityUrlSpider)
    yield runner.crawl(QYUrlSpider)
    reactor.stop()

#runner.crawl(QYConUrlSpider)
#runner.crawl(QYCityUrlSpider)
#runner.crawl(QYUrlSpider)

runner.crawl(QYXingChengSpider)

d = runner.join()
d.addBoth(lambda _: reactor.stop())
reactor.run()