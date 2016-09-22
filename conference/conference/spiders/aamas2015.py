__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class AAMAS2015Spider(scrapy.Spider):

    name = "aamas2015"
    allowed_domains = ["www.aamas2015.com"]
    start_urls = [
        "http://www.aamas2015.com/en/ACCEPTED-PAPERS.html"
    ]

    def parse(self, response):

        for record in response.xpath('//div//ul//li[em]'):

            item = ConferenceItem()
            print record
            item['year'] = "2015"
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