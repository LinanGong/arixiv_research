# -*- coding: utf-8 -*-
__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class PLDI2012Spider(scrapy.Spider):

    name = "pldi2012"
    allowed_domains = ["pldi12.cs.purdue.edu"]
    start_urls = [
        "http://pldi12.cs.purdue.edu/content/list-accepted-papers-论文收录"
    ]

    def parse(self, response):

        print response.xpath('//h1/text()').extract()[0]

        for record in response.xpath('//p'):
            print record
            item = ConferenceItem()
            item['year'] = '2012'
            print record.xpath('text()')
            item['title'] = record.xpath('following::div[1]/text()').extract()[0].strip()

            authors = record.xpath('following::div[2]/text()').extract()
            authors = ''.join(authors).split('\n')[1].split(', ')
            item['authors'] = authors

            yield item
