"""Cian.ru spider runner."""

import sys
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from cian.spiders.cianru import CianruSpider
from cian import settings

def _main():
    """Entry point."""
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(CianruSpider)

    process.start()


if __name__ == '__main__':
    sys.exit(_main())
