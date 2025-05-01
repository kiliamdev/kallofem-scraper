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
    output_preview = None

    if has_output:
        try:
            import json
            with open("output.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                output_preview = data[:5]
        except Exception as e:
            output_preview = [{"hiba": str(e)}]

    return render_template("index.html", has_output=has_output, output_preview=output_preview)

@app.route("/scrape", methods=["POST"])
def run_scraper():
    import time
    import run_spider
    import sys
    from io import StringIO

    if os.path.exists("output.json"):
        os.remove("output.json")

    old_stdout = sys.stdout
    mystdout = StringIO()
    sys.stdout = mystdout

    try:
        run_spider.run()
    except Exception as e:
        print(f"\nHiba: {e}\n")

    sys.stdout = old_stdout

    log_output = mystdout.getvalue()
    with open("scraper_log.txt", "w", encoding="utf-8") as f:
        f.write(log_output())
    
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