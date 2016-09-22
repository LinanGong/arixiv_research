__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class SIGKDD2015Spider(scrapy.Spider):

    name = "sigkdd2015"
    allowed_domains = ["www.kdd.org"]
    start_urls = [
        "http://www.kdd.org/kdd2015/program.html"
    ]

    def parse(self, response):

        for record in response.xpath('//section//strong'):

            item = ConferenceItem()
            item['year'] = '2015'
            title = record.xpath('text()').extract()
            item['title'] = title[0]
            authors = record.xpath('following-sibling::text()[1]').extract()
            print authors
            authors = authors[0].split('; ')
            au = []
            for a in authors:
                au.append(a.split(',')[0])
            item['authors'] = au

            yield item