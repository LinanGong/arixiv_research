__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class ACL2009Spider(scrapy.Spider):

    name = "acl2009"
    allowed_domains = ["acl2009.org"]
    start_urls = [
        "http://www.acl-ijcnlp-2009.org/main/acceptedfullpapers.html",
        "http://www.acl-ijcnlp-2009.org/main/acceptedshortpapers.html"
    ]

    def parse(self, response):

        for record in response.xpath('//p'):

            data = record.xpath('span/text()').extract()
            print data

            if len(data)>0:
                item = ConferenceItem()
                item['year'] = "2009"
                title = record.xpath('br/following::text()').extract()
                item['title'] = title[0].strip().lstrip()
                if record.xpath('span/following::span'):
                    authors = record.xpath('span/text()').extract()[0] + record.xpath('span/following::span/text()').extract()[0]
                else:
                    authors = record.xpath('span/text()').extract()[0].strip().lstrip()
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
