__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class AAMAS2013Spider(scrapy.Spider):

    name = "aamas2013"
    allowed_domains = ["www.aamas2013.com"]
    start_urls = [
        "http://aamas2013.cs.umn.edu/node/44"
    ]

    def parse(self, response):

        for record in response.xpath('//div//ul//li[em]'):

            item = ConferenceItem()
            print record
            item['year'] = "2013"
            data = record.xpath('text()').extract()[0].strip()
            print data
            data = data.split(': ')
            if len(data) > 2:
                item['title'] = data[1] + ': ' + data[2]
            else:
                item['title'] = data[1]
            authors = record.xpath('em/text()').extract()[0]
            print authors
            authors = authors.split(', ')
            item['authors'] = authors[0:-1]
            item['authors'].append(authors[-1])

            yield item