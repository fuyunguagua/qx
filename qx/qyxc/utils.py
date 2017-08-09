import json
import pymongo

from qx.qyxc import redis
from .settings import MONGO_CONF
class Redis_utils(object):
    @classmethod
    #链接数据库
    def __con_redis(cls):

        return redis.StrictRedis(host='127.0.0.1',port=6379,db=0)

    @classmethod
    #set类型 添加元素
    def insert_url(cls,key,value):
        r = cls.__con_redis()

        return r.sadd(key,value)

    @classmethod
    #key 表  field 域 value 值
    def insert_meta(cls,key,field,value):
        r = cls.__con_redis()
        #将哈希表 key 中的域 field 的值设置为 value ，当且仅当域 field 不存在。若域 field 已经存在，该操作无效。如果 key 不存在，一个新哈希表被创建并执行 HSETNX 命令。
        return r.hsetnx(key,field,value)

    @classmethod
    #hash类型 就是键值对类型 获得键对应的值
    def get_meta(cls,key,field):
        r = cls.__con_redis()
        data = r.hget(key,field)
        return data

    @classmethod
    #得到元素的数量
    def get_count(cls,key):
        r = cls.__con_redis()
        if r.exists(key):
            _type = r.type(key)
            if _type == 'set':
                #返回集合的数量
                count = r.scard(key)
            elif _type == 'list':
                count = r.llen(key)
            elif _type =='hash':
                count = r.hlen(key)
            return count

    @classmethod
    def del_keys(cls,*keynames):
        r = cls.__con_redis()
        #filter(function, sequence)  python的特性
        keys = filter(lambda x: r.exists(x),keynames)
        for key in keys:
            r.delete(key)

    @classmethod
    def get_set_member(cls,key):
        r = cls.__con_redis()
        if r.exists(key) and r.type(key) =='set':
            #smembers  返回所有元素 针对集合
            return r.smembers(key)

    @classmethod
    #对键重命名
    def rename_key(cls,field,old_key,new_key):
        r = cls.__con_redis()
        if r.hexists(field,old_key):
            value = r.hget(field,old_key)
            r.hdel(field,old_key)
            r.hset(field,new_key,value)

    @classmethod
    #统计meta的数量 _id
    def statistic_meta(cls,key,_id):
        count = 0
        r = cls.__con_redis()
        #获得key 对应的所有values
        values = r.hvals(key)
        for value in values:
            parsed_id = json.loads(value).get('meta').get('_id')
            if parsed_id ==id:
                count +=1
            return count
    @classmethod
    #读出meta记录的数量
    def statistic_meta2(cls,key,zone):
        count = 0
        r = cls.__con_redis()
        values = r.hvals(key)
        for value in values:
            if zone ==json.loads(value).get('meta').get('zone'):
                count =json.loads(value).get('meta').get('count')
        return count

class Mongo_utils(object):
    def __init__(self,db=None,collection=None):
        #from ipdb import set_trace
        #set_trace()
        #链接mongo
        self.mongo_host = MONGO_CONF.get('host')
        self.mongo_port = MONGO_CONF.get('port')
        self.mongo_user = MONGO_CONF.get('user',None)
        self.mongo_pass = MONGO_CONF.get('passwd',None)
        self.mongo_client = pymongo.MongoClient(
            host=self.mongo_host,port=self.mongo_port
        )
        if isinstance(db,str):
            self.db = db
            self.mongo_db = self.mongo_client[self.db]
        if isinstance(collection,str):
            self.collection = collection
            self.collection = self.mongo_db['self.collection']

    def get_dbs(self):
        '''获取所有的数据库'''
        return self.mongo_client.database_name()

    def get_collections(self):
        '''
        获取所有的集合
        '''
        return self.mongo_db.collection_names()

    def insert_data(self,data):
        if isinstance(data,list):
            self.collection.insert_many(data)
        elif isinstance(data,dict):
            self.collection.insert(data)
        else:
            pass

    def get_data(self,**condition):
        '''
        获取数据
        '''
        return self.collection.find(condition)

    def delete_data(self,**condition):
        '''
        删除数据
        '''
        return self.collection.remove(condition)

    def get_count(self,**condition):
        '''
        获取数据量
        :param condition:
        :return:
        '''
        return self.collection.find(condition).count()

    def get_max_data(self,key,**condition):
        #desending  表示下降              website    batch
        return self.collection.find_one(condition,sort=[(key,pymongo.DESCENDING)])

    def get_min_data(self,key,**condition):
        #上升
        return self.collection.find_one(condition,sort=[(key,pymongo.ASCENDING)])
