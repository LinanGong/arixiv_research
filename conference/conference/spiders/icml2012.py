__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class ICML2012Spider(scrapy.Spider):

    name = "icml2012"
    allowed_domains = ["www.icml.com"]
    start_urls = [
        "http://icml.cc/2012/papers/"
    ]

    def parse(self, response):

        for record in response.xpath('//div[@class=\'paper\']'):

            item = ConferenceItem()
            print record
            item['year'] = "2012"
            title = record.xpath('h2/text()').extract()
            print title
            item['title'] = title[0]

            authors = record.xpath('p[@class=\'authors\']/text()').extract()[0]
            print authors
            authors = authors.split(',')
            a = []
            for i in authors:
                a.append(i.lstrip().strip())
            item['authors'] = a

            yield item