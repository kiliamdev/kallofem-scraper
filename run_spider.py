from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from kallofem_scraper.spiders.products_spider import ProductsSpider
from twisted.internet.task import react
import sys

def run_spider_main():
    runner = CrawlerRunner(get_project_settings())

    deferred = runner.crawl(ProductsSpider)
    deferred.addBoth(lambda _: reactor.stop())
    reactor.run()  # blocking call

def run():
    try:
        run_spider_main()
    except RuntimeError:
        pass
