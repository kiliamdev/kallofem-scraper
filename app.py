from flask import Flask, jsonify
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from kallofem_scraper.spiders.products_spider import ProductsSpider
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Kálló-Fém scraper API működik!"

@app.route("/scrape")
def run_scraper():
    process = CrawlerProcess(get_project_settings())
    process.crawl(ProductsSpider)
    process.start()
    return jsonify({"message": "Scraper lefutott, az output.json fájl frissült."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)