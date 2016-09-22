__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class FOCS2008Spider(scrapy.Spider):

    name = "focs2008"
    allowed_domains = ["www.cs.cmu.edu"]
    start_urls = [
        "http://www.cs.cmu.edu/~FOCS2008/accepted.html"
    ]

    def parse(self, response):

        for record in response.xpath('//span/div//p[position()>1]'):

            item = ConferenceItem()
            data = record.xpath('text()').extract()
            print data
            item['year'] = '2008'
            title = data[1]
            item['title'] = title.lstrip().strip()
            authors = data[0].lstrip().strip('.').split(', ')
            au = []
            for a in authors:
                if 'and' in a:
                    au.extend(a.split(' and '))
                else:
                    au.append(a)

            item['authors'] = au
            yield item