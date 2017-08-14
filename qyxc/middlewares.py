#coding=utf-8

import random
from scrapy.http import HtmlResponse
import selenium
from selenium import webdriver
import time

class RandomUserAgent(object):
    def __init__(self,agent):
        self.agents = agent

    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self,request,spider):
        request.headers.setdefault('User_Agent',random.choice(self.agents))
#执行js代码使页面不断下拉，从而动态加载完成
class CompleteRequste(object):

    @classmethod
    def process_request(self,request,spider):
        if spider.name == 'qy_xingcheng_spider':
            driver = webdriver.PhantomJS()#获得浏览器对象
            driver.get(request.url)

            def execute_times(times):
                for i in range(times + 1):
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(5)

            execute_times(5)
            content = driver.page_source.encode('utf-8')
            driver.quit()
            return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)











