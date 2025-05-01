BOT_NAME = "kallofem_scraper"

SPIDER_MODULES = ["kallofem_scraper.spiders"]
NEWSPIDER_MODULE = "kallofem_scraper.spiders"

ROBOTSTXT_OBEY = True

FEED_FORMAT = "json"
FEED_URI = "output.json"
FEED_EXPORT_INDENT = 2
FEED_EXPORT_ENCODING = "utf-8"
