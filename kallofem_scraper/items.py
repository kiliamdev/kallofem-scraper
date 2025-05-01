import scrapy

class KallofemScraperItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    image_url = scrapy.Field()