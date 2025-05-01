from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from kallofem_scraper.spiders.products_spider import ProductsSpider
import logging

def run():
    logging.basicConfig(
        filename="scraper_log.txt",
        format="%(asctime)s [%(levelname)s]: %(message)s", level=logging.INFO
    )
    process = CrawlerProcess(get_project_settings())
    process.crawl(ProductsSpider)
    process.start()
