import scrapy
from items import HomePageNews
from scrapy.selector import Selector


class EngadgetSpider(scrapy.Spider):
    name = 'engadget'
    url = 'http://www.engadget.com/'
    
    @classmethod
    def _get_name(cls):
        return cls.name
        
    @classmethod
    def _get_url(cls):
        return cls.url
        
    def parse(self, response):
        sel = Selector(response)
        item = HomePageNews()
        
        # headlines
        headlines = []
        for sel in response.xpath(".//*[@id='carousel']/ul/li/a/div/span"):
            headline = sel.xpath("text()").extract()
            headlines.extend(headline)
        
        # articles
        stories = []
        for sel in response.xpath(".//header/div/div/h2/a"):
            story = sel.xpath("text()").extract()
            stories.extend(story)
            
        item['headlines'] = headlines
        item['stories'] = stories
        yield item
        