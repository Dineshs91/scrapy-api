import scrapy

class HomePageNews(scrapy.Item):
    headlines = scrapy.Field()
    stories = scrapy.Field()
    