__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class AAAI2015Spider(scrapy.Spider):

    name = "aaai2015"
    allowed_domains = ["www.aaai.org"]
    start_urls = [
        "http://www.aaai.org/Library/AAAI/aaai15contents.php"
    ]

    def parse(self, response):

        for record in response.xpath('//p[@class=\'left\']'):

            item = ConferenceItem()
            print record
            item['year'] = "2015"
            data = record.xpath('a/text()').extract()
            print data
            item['title'] = data[0].strip().lstrip()
            authors = record.xpath('i/text()').extract()[0]
            print authors
            authors = authors.split(', ')
            item['authors'] = authors[0:-1]
            item['authors'].append(authors[-1])

            yield item
