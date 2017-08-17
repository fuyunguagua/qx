# -*- coding: utf-8 -*-

from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi
from .settings import MYSQL_DBNAME,MYSQL_HOST,MYSQL_PASSWD,MYSQL_USER,MONGO_CONF
from .items import QYURLItem
import pymysql
import pymysql.cursors
from .dupefilter import Dupefilter
from qx.qyxc.utils import Redis_utils
from qx.qyxc.utils import Mongo_utils
from scrapy import log

#处理item,空字段设为无
#去重
class CleanPipeline(object):
    num_of_dupe = 0
    def __init__(self):
        self.has = set()

    def setnone(self, item):
        item['journey_name'] = item['journey_name'][0] if item['journey_name'] else '无'
        item['url'] = 'http:' + item['url'][0] if item['url'] else '无'
        item['line'] = item['line'][0] if item['line'] else '无'
        item['date'] = item['date'][0] if item['date'] else '无'
        item['lable'] = item['lable'][0] if item['lable'] else '无'
        item['day'] = item['day'][0] if item['day'] else 0


    def process_item(self, item, spider):
        if spider.name == 'myspider_qypage':
            self.setnone(item)
            if Dupefilter.request_seen(item['url']):
                self.num_of_dupe += 1
                log.msg(str(self.num_of_dupe)+'has dropped!')
                raise DropItem
            else:
                Redis_utils.server.lpush('myspider:start_urls', item['url'])
        return item


class MySQLPipeline(object):
    def __init__(self):
        dbargs = dict(
            host=MYSQL_HOST,
            db=MYSQL_DBNAME,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            charset='utf8',
            cursorclass = pymysql.cursors.DictCursor,
            use_unicode= True,
        )
        self.dbpool = adbapi.ConnectionPool('pymysql', **dbargs)


    def process_item(self, item, spider):
        fun_name = None
        if spider.name == 'myspider_qypage':
            fun_name = self.__do__insert__xcurl
        elif spider.name == 'qy_con_spider':
            fun_name = self.__do__insert__contry
        d = self.dbpool.runInteraction(fun_name, item, spider)
        d.addBoth(lambda _: item)
        return d

    def __do__insert__contry(self, conn, item, spider):
        conn.execute("insert into contry(name, contry_url, con_id) VALUES (%s,%s,%d)",
                     (item['name'], item['url'], item['con_id']))
    def __do__insert__xcurl(self, conn, item, spider):
        conn.execute("insert into qyxcurl(jounel_name, url, line, date, day, lable) VALUES (%s,%s,%s,%s,%s,%s)",
                     (item['journey_name'], item['url'], item['line'], item['date'], item['day'],item['lable']))



class MongoPipeline(object):

    def process_item(self, item, spider):
        choice  = {'myspider_qypage':'qy_url_info','qy_con_spider':'qy_con_info','qy_xingcheng_spider':'qy_xc_info'}
        collection_name = choice.get(spider.name, None)
        Mongo_utils(db='qyxc', collection=collection_name).insert_data(dict(item))
        return item





