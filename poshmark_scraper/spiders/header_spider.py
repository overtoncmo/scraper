# poshmark_scraper/spiders/header_spider.py
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class HeaderSpider(CrawlSpider):
    name = "header_spider"

    start_urls = ["https://scrapy.org"]
    allowed_domains = ["scrapy.org"]
    rules = [  # Get all links on start url
        Rule(
            link_extractor=LinkExtractor(
                deny=r"\?",
            ),
            follow=False,
            callback="parse_page",
        )
    ]

    def parse_start_url(self, response):
        return self.parse_page(response)

    def parse_page(self, response):
        header = response.css("h1, h2").extract_first(
        ) or response.css("title").extract_first() or response.url
        return {
            "header": header,
            "url": response.url,
        }