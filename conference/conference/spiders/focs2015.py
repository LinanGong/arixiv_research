__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem
import re

class FOCS2015Spider(scrapy.Spider):

    name = "focs2015"
    allowed_domains = ["www.cs.cmu.edu"]
    start_urls = [
        "http://www.cs.cmu.edu/~venkatg/focs15-acceptedpapers.html"
    ]

    def parse(self, response):

        for record in response.xpath('//ul//li'):

            item = ConferenceItem()
            print record
            item['year'] = "2015"
            title = record.xpath('b/text()').extract()
            print title
            title = title[0].lstrip().strip().replace('\r\n', ' ')
            item['title'] = title

            authors = record.xpath('text()').extract()
            print authors

            authors = authors[0].split(', ')
            data = []
            for a in authors:
                a = re.sub('\(.*\)|\(.*\r\n.*\)', '', a)
                a = a.lstrip().strip()
                print a
                if 'and' in a:
                    data.extend(a.split(' and '))
                else:
                    data.append(a)
            item['authors'] = data

            yield item