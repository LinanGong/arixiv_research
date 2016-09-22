__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class ICML2007Spider(scrapy.Spider):

    name = "icml2007"
    allowed_domains = ["www.icml.com"]
    start_urls = [
        "http://oregonstate.edu/conferences/event/icml2007/paperlist.html"
    ]

    def parse(self, response):

        for record in response.xpath('//table//tr[@class=\'header\']'):

            item = ConferenceItem()
            print record
            item['year'] = "2007"
            title = record.xpath('td/a/text()').extract()
            print title
            item['title'] = title[0].lstrip().strip()

            authors = record.xpath('following::tr[1]/td[2]/text()').extract()
            print authors
            data = []
            for a in authors:
                a = a.lstrip().strip().split(' - ')
                if a[0]:
                    data.append(a[0])
            item['authors'] = data

            yield item