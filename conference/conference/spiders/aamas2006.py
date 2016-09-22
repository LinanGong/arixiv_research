__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class AAMAS2006Spider(scrapy.Spider):

    name = "aamas2006"
    allowed_domains = ["www.aamas2006.com"]
    start_urls = [
        "http://www.ifaamas.org/AAMAS/aamas06/accepted.html#Full"
    ]

    def parse(self, response):

        for record in response.xpath('//tr'):

            item = ConferenceItem()
            print record
            item['year'] = "2006"
            title = record.xpath('td[strong]/strong/text()').extract()
            print title
            item['title'] = title[0]

            authors = record.xpath('td[strong]/text()').extract()[0]
            print authors
            authors = authors.lstrip().strip().split(', ')
            item['authors'] = authors

            yield item