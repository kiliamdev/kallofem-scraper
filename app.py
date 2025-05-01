from flask import Flask, jsonify, send_file, render_template, redirect
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
    log_output = None
    if os.path.exists("scraper_log.txt"):
        with open("scraper_log.txt", "r", encoding="utf-8") as f:
            log_output = f.read()[-3000:]  # csak az utolsó 3000 karakter
    return render_template("index.html", has_output=has_output, log=log_output)

@app.route("/scrape", methods=["POST"])
def run_scraper():
    import time

    if os.path.exists("output.json"):
        os.remove("output.json")

    with open("scraper_log.txt", "w", encoding="utf-8") as log_file:
        result = subprocess.run(["scrapy", "crawl", "products"], stdout=log_file, stderr=subprocess.STDOUT, text=True)
    
    for _ in range(10):
        if os.path.exists("output.json"):
            break
        time.sleep(0.5)

    has_output = os.path.exists("output.json") 
    return redirect("/")

    
@app.route("/output")
def get_output():
    if os.path.exists("output.json"):
        return send_file("output.json", as_attachment=True)
    return "output.json nem talalhato", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)