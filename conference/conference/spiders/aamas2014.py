__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class AAMAS2014Spider(scrapy.Spider):

    name = "aamas2014"
    allowed_domains = ["aamas2014"]
    start_urls = [
        "http://aamas2014.lip6.fr/papers.php"
    ]

    def parse(self, response):

        for record in response.xpath('//h3/following::li'):

            item = ConferenceItem()
            print record
            item['year'] = "2014"
            data = record.xpath('text()').extract()
            print data
            item['title'] = data[0].strip().lstrip()
            authors = record.xpath('i/text()').extract()[0]
            print authors
            authors = authors.split(', ')
            item['authors'] = authors[0:-1]

            yield item