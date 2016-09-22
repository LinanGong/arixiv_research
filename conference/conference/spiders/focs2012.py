__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class FOCS2012Spider(scrapy.Spider):

    name = "focs2012"
    allowed_domains = ["www.cs.cmu.edu"]
    start_urls = [
        "https://sites.google.com/site/yixincaoresearch/papers/focs-2012"
    ]

    def parse(self, response):

        for record in response.xpath('//tbody'):


            data = record.xpath('.//text()').extract()[0]
            print data
            data = data.split(' \n\n')
            for d in data:
                item = ConferenceItem()
                item['year'] = '2012'
                title = d.split('\n')[0]
                item['title'] = title
                authors = d.split('\n')[1]
                item['authors'] = authors.split(' and ')
                yield item