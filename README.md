#爬取穷游网行程信息
###简介
用scrapy-redis做了一个分布式的爬虫。目标是穷游网上的行程信息
###用法：
将项目导入到pycharm中，在本地安装好redis和mongodb，运行run.py
###已实现：
利用selenium和phantomjs抓取动态加载的行程信息。
将爬取到的行程的概览信息存入到mongodb中
将最终的行程信息存入到mongodb中。
###TODO:
实现增量爬取。