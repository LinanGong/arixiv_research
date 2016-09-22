__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class SIGKDD2014Spider(scrapy.Spider):

    name = "sigkdd2014"
    allowed_domains = ["www.kdd.org"]
    start_urls = [
        "file:///Users/Kay/Project/webpage/kdd14.html"
    ]

    def parse(self, response):
        i = 3
        for x in response.xpath('//table[@class=\'text12\']//tr'):

            record = response.xpath('//table[@class=\'text12\']//tr[position()=%d]'%i)
            if record.xpath('td[2]/span/a[not(@title)]'):
                data = record.xpath('td[2]/span/a[not(@title)]/text()').extract()
                item = ConferenceItem()
                item['year'] = '2014'
                item['title'] = data[0]
                print data
                authors = record.xpath('following-sibling::tr[1]//a/text()').extract()
                print authors
                item['authors'] = authors
                yield item
                i += 2
            else:
                i += 1
