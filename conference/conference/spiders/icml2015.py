__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class ICML2015Spider(scrapy.Spider):

    name = "icml2015"
    allowed_domains = ["www.icml.com"]
    start_urls = [
        "http://jmlr.org/proceedings/papers/v37/"
    ]

    def parse(self, response):

        for record in response.xpath('//div[@class=\'paper\']'):

            item = ConferenceItem()
            print record
            item['year'] = "2015"
            title = record.xpath('p[@class=\'title\']/text()').extract()
            print title
            item['title'] = title[0]

            authors = record.xpath('p/span//text()').extract()[0]
            print authors
            authors = authors.split(',')
            a = []
            for i in authors:
                a.append(i.lstrip().strip())
            item['authors'] = a

            yield item