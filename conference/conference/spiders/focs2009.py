__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class FOCS2009Spider(scrapy.Spider):

    name = "focs2009"
    allowed_domains = ["www.cs.cmu.edu"]
    start_urls = [
        "http://www.cc.gatech.edu/focs2009/papers.htm"
    ]

    def parse(self, response):

        for record in response.xpath('//ul//li'):

            item = ConferenceItem()
            data = record.xpath('text()').extract()
            print data
            item['year'] = '2009'
            title = data[0]
            item['title'] = title
            authors = data[1].lstrip().strip('. ').split(', ')
            au = []
            for a in authors:
                if 'and' in a:
                    au.extend(a.split(' and '))
                else:
                    au.append(a)

            item['authors'] = au

            yield item