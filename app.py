from flask import Flask, jsonify, send_file, render_template
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from kallofem_scraper.spiders.products_spider import ProductsSpider
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scrape")
def run_scraper():
    from io import StringIO
    import sys

    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO

    process = CrawlerProcess(get_project_settings())
    process.crawl(ProductsSpider)
    process.start()

    sys.stdout = old_stdout

    log_output = mystdout.getvalue()

    return render_template("index.html", log=log_output)

@app.route("/output")
def get_output():
    try:
        return send_file("output.json", as_attachment=True)
    except FileNotFoundError:
        return jsonify({"error": "A fajl meg nem letezik. Futtasd elobb a /scrape vegpontot."}), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)