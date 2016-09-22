__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class ACL2013Spider(scrapy.Spider):

    name = "acl2013"
    allowed_domains = ["acl2013.org"]
    start_urls = [
       "http://acl2013.org/site/accepted-papers.html"
    ]

    def parse(self, response):

        for record in response.xpath('//div[@class=\'page\']//a'):

            item = ConferenceItem()
            item['year'] = "2013"
            data = record.xpath('text()').extract()
            item['title'] = data[0].strip().lstrip()
            authors = record.xpath('following::table[1]//em/text()').extract()[0].strip().lstrip()
            if "and" in authors:
                authors = authors.split(', ')
                item['authors'] = authors[0:-1]
                item['authors'].append(authors[-1].split('and')[0].strip())
                item['authors'].append(authors[-1].split('and')[1].lstrip())
            else:
                item['authors'] = [authors]
            yield item




