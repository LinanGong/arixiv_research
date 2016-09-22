__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem
import re

class ACL2012Spider(scrapy.Spider):

    name = "acl2012"
    allowed_domains = ["aclweb.org"]
    start_urls = [
       "http://aclweb.org/mirror/acl2012/program/sub00.asp.html"
    ]

    def parse(self, response):

        for record in response.xpath('//table[@class=\'tbl\']//tr'):

            item = ConferenceItem()
            item['year'] = "2012"
            title = record.xpath('td[2]/p/text()').extract()

            if len(title) > 0:

                item['title'] = re.sub('\r\n +', '', title[0].strip())
                if not record.xpath('td[2]/p[em]'):
                    authors = title[1].strip()
                else:
                    authors = record.xpath('td[2]/p/em/text()').extract()[0].strip().lstrip()
                if "and" in authors:
                    authors = authors.split(', ')
                    item['authors'] = authors[0:-1]
                    item['authors'].append(authors[-1].split('and')[0].strip())
                    item['authors'].append(authors[-1].split('and')[1].lstrip())
                else:
                    item['authors'] = [authors]
                yield item

            else:
                pass
