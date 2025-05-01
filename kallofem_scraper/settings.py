BOT_NAME = "kallofem_scraper"

SPIDER_MODULES = ["kallofem_scraper.spiders"]
NEWSPIDER_MODULE = "kallofem_scraper.spiders"

ROBOTSTXT_OBEY = True

FEEDS = {
    'output.json': {
        'format': 'json',
        'encoding': 'utf8',
        'indent': 2,
    }
}
