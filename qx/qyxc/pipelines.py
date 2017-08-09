# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi
from .settings import MYSQL_DBNAME,MYSQL_HOST,MYSQL_PASSWD,MYSQL_USER,MONGO_CONF
from .items import QYURLItem
import pymysql
import pymysql.cursors
import pymongo
from qx.qyxc import redis
from scrapy import log

#处理item,空字段设为无
class CleanPipeline(object):

    def __init__(self):
        self.has = set()

    def process_item(self, item, spider):
        r = redis.Redis()

        def setnone(item):
            item['journey_name'] = item['journey_name'][0] if item['journey_name'] else '无'
            item['url'] = 'http:' + item['url'][0] if item['url'] else '无'
            item['line'] = item['line'][0] if item['line'] else '无'
            item['date'] = item['date'][0] if item['date'] else '无'
            item['lable'] = item['lable'][0] if item['lable'] else '无'
            item['day'] = item['day'][0] if item['day'] else 0
        if spider.name == 'myspider_qypage':
            setnone(item)
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
    def __init__(self):
        self.mongo_host = MONGO_CONF['host']
        self.mongo_port = MONGO_CONF['port']
        self.db_name = MONGO_CONF['db']
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(
            host=self.mongo_host,port=self.mongo_port)
        self.db = self.client[self.db_name]

    def process_item(self, item, spider):
        choice  = {'myspider_qypage':'qy_url_info','qy_con_spider':'qy_con_info'}
        collection_name = choice.get(spider.name, None)
        data= dict(item)
        if isinstance(data,dict):
            self.db[collection_name].insert(dict(data))
        elif isinstance(data,list):
            self.db[collection_name].insert_many(list(data))
        else:
            pass
        return item

    def close_spider(self,spider):
        self.client.close()




