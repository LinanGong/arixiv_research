__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class PLDI2014Spider(scrapy.Spider):

    name = "pldi2014"
    allowed_domains = ["conferences.inf.ed.ac.uk"]
    start_urls = [
        "http://conferences.inf.ed.ac.uk/pldi2014/acceptedpapers.html"
    ]

    def parse(self, response):

        for record in response.xpath('//ul/li'):

            item = ConferenceItem()
            item['year'] = '2014'
            item['title'] = record.xpath('span/text()').extract()[0]

            authors = record.xpath('text()').extract()[0].strip().lstrip('.\n +')
            authors = authors.split(';')
            print authors
            data = []
            for author in authors:
                author = author.split(',')[0].lstrip()
                print author
                if author != '':
                    data.append(author)

            item['authors'] = data

            yield item
