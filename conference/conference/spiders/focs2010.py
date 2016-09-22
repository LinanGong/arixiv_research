__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem
import re

class FOCS2010Spider(scrapy.Spider):

    name = "focs2010"
    allowed_domains = ["www.cs.cmu.edu"]
    start_urls = [
        "http://theory.stanford.edu/focs2010/accepted.html"
    ]

    def parse(self, response):

        for record in response.xpath('//ol//li'):

            item = ConferenceItem()
            item['year'] = "2010"
            title = record.xpath('b/text()').extract()
            print title
            title = title[0].lstrip().strip()
            item['title'] = title

            authors = record.xpath('text()').extract()
            print authors
            item['authors'] = authors
            yield item