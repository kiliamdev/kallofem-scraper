from flask import Flask, jsonify, send_file, render_template
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from kallofem_scraper.spiders.products_spider import ProductsSpider
from io import StringIO
import os
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    has_output = os.path.exists("output.json")
    return render_template("index.html", has_output=has_output)

@app.route("/scrape", methods=["POST"])
def run_scraper():
    
    result = subprocess.run(["scrapy", "crawl", "products"], capture_output=True, text=True)

    log_output = result.stdout + "\n\n" + result.stderr
    has_output = os.path.exists("output.json")

    if os.path.exists("output.json"):
        os.remove("output.json")

    return render_template("index.html", log=log_output, has_output=has_output)

    
@app.route("/output")
def get_output():
    if os.path.exists("output.json"):
        return send_file("output.json", as_attachment=True)
    return "output.json nem talalhato", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)