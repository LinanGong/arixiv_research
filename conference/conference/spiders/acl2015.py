__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class ACL2015Spider(scrapy.Spider):

    name = "acl2015"
    allowed_domains = ["acl2015.org"]
    start_urls = [
       "http://acl2015.org/accepted_papers.html"
    ]

    def parse(self, response):

        for record in response.xpath('//body/div/ul//ul/li'):

            item = ConferenceItem()
            item['year'] = "2015"
            data = record.xpath('text()').extract()
            item['title'] = data[0].strip().lstrip()
            authors = data[1].strip().lstrip()
            if "and" in authors:
                authors = authors.split(', ')
                item['authors'] = authors[0:-1]
                item['authors'].append(authors[-1].split('and')[0].strip())
                item['authors'].append(authors[-1].split('and')[1].lstrip())
            else:
                item['authors'] = [authors]
            yield item
