__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class ICML2014Spider(scrapy.Spider):

    name = "icml2014"
    allowed_domains = ["www.icml.com"]
    start_urls = [
        "http://icml.cc/2014/index/article/15.htm"
    ]

    def parse(self, response):

        for record in response.xpath('//dt'):

            item = ConferenceItem()
            print record
            item['year'] = "2014"
            title = record.xpath('text()').extract()
            print title
            item['title'] = title[0].strip()

            authors = record.xpath('following-sibling::dd[1]/text()').extract()[0]
            print authors
            authors = authors.strip().split(', ')
            item['authors'] = authors

            yield item