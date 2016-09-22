__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class ACL2011Spider(scrapy.Spider):

    name = "acl2011"
    allowed_domains = ["acl2011.org"]
    start_urls = [
       "http://aclweb.org/mirror/acl2011/accepted_papers.shtml.html"
    ]

    def parse(self, response):

        for record in response.xpath('//pre'):
            data = record.xpath('text()').extract()[0].strip().lstrip()

            for paper in data.split('\r\n\r\n'):

                item = ConferenceItem()
                item['year'] = "2011"
                text = paper.split('\r\n')
                if len(text) == 2:
                    item['title'] = text[0]
                    authors = text[1]
                elif ',' in text[1]:
                    item['title'] = text[0]
                    authors = text[1] + ' ' + text[2]
                else:
                    item['title'] = text[0] + ' ' + text[1]
                    if len(text) == 3:
                        authors = text[2]
                    elif len(text) == 4:
                        authors = text[2] + ' ' + text[3]
                    else:
                        authors = text[2] + ' ' + text[3] + ' ' + text[4]

                if "and" in authors:
                    authors = authors.split(', ')
                    item['authors'] = authors[0:-1]
                    item['authors'].append(authors[-1].split('and')[0].strip())
                    item['authors'].append(authors[-1].split('and')[1].lstrip())
                else:
                    item['authors'] = [authors]
                yield item
