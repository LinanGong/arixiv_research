__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class FOCS2007Spider(scrapy.Spider):

    name = "focs2007"
    allowed_domains = ["www.cs.cmu.edu"]
    start_urls = [
        "http://www.sciweavers.org/conference/focs-2007"
    ]

    def parse(self, response):

        for record in response.xpath('//tr//div[@class=\'cp_pp\']'):

            item = ConferenceItem()

            item['year'] = '2007'
            title = record.xpath('a/text()').extract()
            print title
            item['title'] = title[0]
            authors = record.xpath('a/@title').extract()
            print authors
            authors = authors[0].split(', ')
            item['authors'] = authors

            yield item