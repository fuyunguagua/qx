#coding=utf-8

import random
from scrapy.http import HtmlResponse
import selenium
from selenium import webdriver
import time
from qx.qyxc import settings
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


#设置代理
class ProxyMiddleware(object):

    def __init__(self):
        self.proxys = settings.PROXY

    def process_request(self,request,spider):
        proxy = 'http://'+self.proxys[0]
        #print(proxy)
        request.meta['proxy'] = proxy

    def process_response(self,request,response,spider):
        print(response.url)
        return response

        #if response.status in [500,503,504,400,403,404,408]:
         #   pass
        #return response


    def process_exception(self,request,exception,spider):
        print(exception)
        new_request = request.copy()
        new_request.meta['proxy'] = 'http://'+random.choice(random.choice(self.proxys))
        return new_request







