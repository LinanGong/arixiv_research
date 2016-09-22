__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class FOCS2013Spider(scrapy.Spider):

    name = "focs2013"
    allowed_domains = ["www.cs.cmu.edu"]
    start_urls = [
        "https://windowsontheory.org/2013/06/27/focs-2013-accepted-papers/"
    ]

    def parse(self, response):

        for record in response.xpath('//p[position()>2]'):

            item = ConferenceItem()
            item['year'] = '2013'
            data = record.xpath('.//text()').extract()
            data = ''.join(data)
            print data
            if 'by' not in data:
                data = data.split(', ')
            else:
                data = data.split(', by ')
            title = data[0]
            print title
            item['title'] = title
            authors = data[1]
            print authors
            authors = authors.split(', ')
            au = []
            for a in authors:
                if 'and' in a:
                    au.extend(a.split(' and '))
                else:
                    au.append(a)
            item['authors'] = au
            yield item