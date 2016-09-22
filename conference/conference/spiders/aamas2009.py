__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class AAMAS2009Spider(scrapy.Spider):

    name = "aamas2009"
    allowed_domains = ["www.aamas2009.com"]
    start_urls = [
        "http://www.aamas-conference.org/Proceedings/aamas09/TOC/01_FP/FP_Session.html"
    ]

    def parse(self, response):

        for record in response.xpath('//p//a[following-sibling::em]'):

            item = ConferenceItem()
            print record
            item['year'] = "2009"
            title = record.xpath('text()').extract()
            print title
            item['title'] = title[0]

            authors = record.xpath('following-sibling::em/text()').extract()[0]
            print authors
            authors = authors.split(', ')
            item['authors'] = authors

            yield item