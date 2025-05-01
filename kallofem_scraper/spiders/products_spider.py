import scrapy
from kallofem_scraper.items import KallofemScraperItem

class ProductsSpider(scrapy.Spider):
    name = "products"
    start_urls = ["https://kallofem.hu/shop/group/keriteselemek"]

    def parse(self, response):
        products = response.css("article.product-row")
        for product in products:
            item = {
                "Terméknév": product.css("h4::text").get(),
                "Ár": product.css("span.product-price::text").get(),
                "Termékkép URL": response.urljoin(product.css("img::attr(src)").get())
            }
            yield item

        next_page = response.css("li.page-item a[rel='next']::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
