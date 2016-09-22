__author__ = 'Kay'

import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem
import re

class ACL2008Spider(scrapy.Spider):

    name = "acl2008"
    allowed_domains = ["aclweb.org"]
    start_urls = [
       "http://aclweb.org/mirror/acl2008/accepts.html"
    ]

    def parse(self, response):

        for record in response.xpath('//tr[not(@class)]'):

            item = ConferenceItem()
            item['year'] = "2008"
            title = record.xpath('td[2]/text()').extract()
            item['title'] = re.sub('\n ', '', title[0])
            authors = re.sub('\n ', '', record.xpath('td[1]/text()').extract()[0])
            if "and" in authors:
                authors = authors.split(', ')
                item['authors'] = authors[0:-1]
                item['authors'].append(authors[-1].split('and')[0].strip())
                item['authors'].append(authors[-1].split('and')[1].lstrip())
            else:
                item['authors'] = [authors]
            yield item
