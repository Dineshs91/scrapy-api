import scrapy
import urllib2
from spiders import (
    EngadgetSpider,
)
from scrapy.http.request import Request
from scrapy.http.response.html import HtmlResponse


class ApiEngine():
    def start(self, spider_name):
        spider = self.find_spider(spider_name)
        url = spider.url
        response = self.download(url)
        res = HtmlResponse(url, '200', body=response)
        items = self.spider(spider, res)
        return list(items)
        
    def find_spider(self, spider_name):
        all_spiders = scrapy.Spider.__subclasses__()
        for spider in all_spiders:
            if spider != scrapy.spider.BaseSpider and spider._get_name() == spider_name:
                return spider()
                
    def download(self, url):
        response = urllib2.urlopen(url)
        body = response.read()
        return body
        
    def spider(self, spider, res):
        ext = spider.parse(res)
        return ext