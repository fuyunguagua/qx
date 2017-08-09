#coding=utf-8

import random

from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.downloadermiddlewares.redirect import RedirectMiddleware

class RandomUserAgent(object):
    def __init__(self,agent):
        self.agents = agent

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self,request,spider):
        request.headers.setdefault('User_Agent',random.choice(self.agents))













