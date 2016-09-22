__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class ACL2007Spider(scrapy.Spider):

    name = "acl2006"
    allowed_domains = ["aclweb.org"]
    start_urls = [
        'http://aclanthology.info/volumes/proceedings-of-the-21st-international-conference-on-computational-linguistics-and-44th-annual-meeting-of-the-association-for-computational-linguistics'
    ]

    def parse(self, response):

        for record in response.xpath('//div[@class=\"span12\" and position()=3]//p[position()>1]'):
            print record
            item = ConferenceItem()
            item['year'] = "2006"
            title = record.xpath('strong/a/text()').extract()
            print title
            item['title'] = title[0].strip().lstrip()
            authors = []
            for path in record.xpath('strong/following-sibling::a'):
                authors.append(path.xpath('text()').extract()[0])
            print authors
            item['authors'] = authors
            yield item
