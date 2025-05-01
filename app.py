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
    import time
    for _ in range(10):
        if os.path.exists("scraper_log.txt"):
            break
        time.sleep(0.3)

    has_output = os.path.exists("output.json")
    log_output = None
    if os.path.exists("scraper_log.txt"):
        with open("scraper_log.txt", "r", encoding="utf-8") as f:
            log_output = f.read()[-3000:]
    return render_template("index.html", has_output=has_output, log=log_output)

@app.route("/scrape", methods=["POST"])
def run_scraper():
    import time
    import run_spider

    if os.path.exists("output.json"):
        os.remove("output.json")
    if os.path.exists("scrapper_log.txt"):
        os.remove("scrapper_log.txt")

    import sys
    from io import StringIO
    old_stdout = sys.stdout
    mystdout = StringIO()
    sys.stdout = mystdout

    try:
        run_spider.run()
    except Exception as e:
        mystdout.write(f"\nHiba: {e}\n")

    sys.stdout = old_stdout

    with open("scraper_log.txt", "w", encoding="utf-8") as f:
        f.write(mystdout.getvalue())
    
    for _ in range(10):
        if os.path.exists("output.json"):
            break
        time.sleep(0.5)

    return redirect("/")

    
@app.route("/output")
def get_output():
    if os.path.exists("output.json"):
        return send_file("output.json", as_attachment=True)
    return "output.json nem talalhato", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)