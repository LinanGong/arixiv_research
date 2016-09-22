__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class PLDI2015Spider(scrapy.Spider):

    name = "pldi2015"
    allowed_domains = ["conf.researchr.org"]
    start_urls = [
        "http://conf.researchr.org/track/pldi2015/pldi2015-papers#event-overview"
    ]

    def parse(self, response):

        for record in response.xpath('//div[@id=\'DLcontent\']/h3'):

            item = ConferenceItem()
            item['year'] = '2015'
            item['title'] = record.xpath('a/text()').extract()[0]

            authors = []
            for author in record.xpath('following::ul[1]//li'):
                authors.append(author.xpath('text()').extract()[0])

            item['authors'] = authors

            yield item

