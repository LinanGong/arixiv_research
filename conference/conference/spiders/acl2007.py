__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class ACL2007Spider(scrapy.Spider):

    name = "acl2007"
    allowed_domains = ["aclweb.org"]
    start_urls = [
       "http://aclweb.org/mirror/acl2007/papers/index.html"
    ]

    def parse(self, response):

        for record in response.xpath('//dt'):

            item = ConferenceItem()
            item['year'] = "2007"
            title = record.xpath('following::dd/text()').extract()
            item['title'] = title[0].strip().lstrip()
            authors = record.xpath('text()').extract()[0].strip().lstrip()
            if "and" in authors:
                authors = authors.split(', ')
                item['authors'] = authors[0:-1]
                item['authors'].append(authors[-1].split('and')[0].strip())
                item['authors'].append(authors[-1].split('and')[1].lstrip())
            else:
                item['authors'] = [authors]
            yield item
