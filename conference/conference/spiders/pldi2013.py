__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class PLDI2013Spider(scrapy.Spider):

    name = "pldi2013"
    allowed_domains = ["pldi2013.ucombinator.org"]
    start_urls = [
        "http://pldi2013.ucombinator.org/accepted.html"
    ]

    def parse(self, response):

        for record in response.xpath('//tr'):

            item = ConferenceItem()
            item['year'] = '2013'
            item['title'] = record.xpath('td/em/text()').extract()[0].strip()

            authors = record.xpath('td[2]/text()').extract()
            print authors
            # authors = authors[0].split('\r\n')
            # print authors
            data = []
            for author in authors:
                author = author.split(',')[0].lstrip()
                print author
                if author != '':
                    data.append(author)

            item['authors'] = data

            yield item
