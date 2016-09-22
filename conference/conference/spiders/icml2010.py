__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem
import re

class ICML2010Spider(scrapy.Spider):

    name = "icml2010"
    allowed_domains = ["www.icml.com"]
    start_urls = [
        "http://icml2010.haifa.il.ibm.com/abstracts.html"
    ]

    def parse(self, response):

        for record in response.xpath('//tr/td/h3'):

            item = ConferenceItem()
            print record
            item['year'] = "2010"
            title = record.xpath('text()').extract()
            print title
            item['title'] = title[0].strip()

            authors = record.xpath('following-sibling::p/em/text()').extract()[0]
            print authors
            authors = authors.split('; ')
            data = []
            for a in authors:
                data.append(re.sub('\(.*\)', '', a).strip())

            item['authors'] = data

            yield item