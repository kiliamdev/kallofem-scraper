from flask import Flask, jsonify, send_file, render_template, redirect, request
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from kallofem_scraper.spiders.products_spider import ProductsSpider
from io import StringIO
import os
import subprocess
import json
import run_spider
import time

app = Flask(__name__)



@app.route("/")
def home():
    from flask import request
    from datetime import datetime

    show_output = request.args.get("show_output") == "1"
    output_preview = None
    has_output = False  # alapból False-ra állítjuk

    last_updated = None
    if has_output:
        ts = os.path.getatime("output.json")
        last_updated = datetime.fromtimestamp(ts).strftime("%Y.%m.%d %H:%M")

    if show_output:
        if os.path.exists("output.json"):
            try:
                with open("output.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list) and len(data) > 0:
                        output_preview = json.dumps(data[:5], ensure_ascii=False, indent=2)
                        has_output = True  # Csak itt lesz True, ha minden rendben!
            except:
                has_output = False

    return render_template("index.html", has_output=has_output, output_preview=output_preview, last_updated=last_updated)


@app.route("/scrape", methods=["POST"])
def run_scraper():
    if os.path.exists("output.json"):
        os.remove("output.json")

    run_spider.run()

    for _ in range(10):
        if os.path.exists("output.json"):
            break
        time.sleep(0.3)

    return redirect("/?show_output=1")

@app.route("/output")
def get_output():
    if os.path.exists("output.json"):
        return send_file("output.json", as_attachment=True)
    return "output.json nem található", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)