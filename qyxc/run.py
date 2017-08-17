from twisted.internet import reactor,defer
import scrapy
import sys
import os
sys.path.insert(0, '/'.join(os.getcwd().split('/')[0:-2]))
from twisted.internet import reactor, defer, task
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from qx.qyxc.spiders.qy_url_spider import QYUrlSpider
from qx.qyxc.spiders.qy_con_spider import QYConUrlSpider
from qx.qyxc.spiders.qy_city_spider import QYCityUrlSpider
from qx.qyxc.spiders.qy_consume_spider import QYXingChengSpider
from qx.qyxc.utils import EmailUtil
from qx.qyxc.utils import Redis_utils
from qx.qyxc.utils import Mongo_utils


def get_statistics_info():
    info = {}
    mongo = Mongo_utils(db='qyxc',collection='qy_xc_info')
    info['urls_num'] = Redis_utils.server.llen('myspider:start_urls')#Redis数据库里待爬取的url数量
    info['urls_requried_num'] = mongo.get_count() #Mongodb已经爬取的url数量
    info = 'Redis still has {} url.\nWe has requested {} url.\n'.format(info['urls_num'],info['urls_requried_num'])
    return info

def main():
    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
    setting = get_project_settings()
    runner = CrawlerRunner(setting)

    # runner.crawl(QYConUrlSpider)
    # runner.crawl(QYCityUrlSpider)
    # runner.crawl(QYUrlSpider)

    runner.crawl(QYXingChengSpider)

    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    lc = task.LoopingCall(EmailUtil.send_email, content_getter_func=get_statistics_info)
    lc.start(interval=5*60*60, now=True)  # 每5小时发送统计信息
    reactor.run()


if __name__ == '__main__':
    main()
