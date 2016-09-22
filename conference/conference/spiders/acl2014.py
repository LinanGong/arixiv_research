__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class ACL2014Spider(scrapy.Spider):

    name = "acl2014"
    allowed_domains = ["acl2014.org"]
    start_urls = [
       "http://acl2014.org/Program.htm"
    ]

    def parse(self, response):

        for record in response.xpath('//div[@class=\'main\']//ul/li'):

            item = ConferenceItem()
            item['year'] = "2014"
            title = record.xpath('text()').extract()
            item['title'] = title[0].strip().lstrip()
            authors = record.xpath('i/text()').extract()[0].strip().lstrip()
            if "and" in authors:
                authors = authors.split(', ')
                item['authors'] = authors[0:-1]
                item['authors'].append(authors[-1].split('and')[0].strip())
                item['authors'].append(authors[-1].split('and')[1].lstrip())
            else:
                item['authors'] = [authors]
            yield item
