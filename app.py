from flask import Flask, jsonify, send_file, render_template, redirect, request
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from kallofem_scraper.spiders.products_spider import ProductsSpider
from io import StringIO
import os
import subprocess

app = Flask(__name__)

from flask import request

@app.route("/")
def home():
    show_output = request.args.get("show_output") == "1"
    has_output = os.path.exists("output.json")
    output_preview = []

    if show_output and has_output:
        try:
            import json
            with open("output.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    output_preview = data[:5]
        except Exception as e:
            output_preview = [{"hiba": f"Hiba történt a JSON olvasása során: {str(e)}"}]

    return render_template("index.html", has_output=has_output if show_output else False, output_preview=output_preview)


@app.route("/scrape", methods=["POST"])
def run_scraper():
    import run_spider
    import os
    import time

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
    return "output.json nem talalhato", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)