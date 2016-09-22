__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class ACL2010Spider(scrapy.Spider):

    name = "acl2010"
    allowed_domains = ["acl2010.org"]
    start_urls = [
       "http://acl2010.org/accepted_papers.html"
    ]

    def parse(self, response):

        for record in response.xpath('//div[@id=\'wide_text\']/p'):

            if record.xpath('strong|a') or not len(record.xpath('text()').extract()):
                pass
            else:
                item = ConferenceItem()
                item['year'] = "2010"
                data = record.xpath('text()').extract()
                print data
                if len(data) == 2:
                    item['title'] = data[0].lstrip()
                    authors = data[1].lstrip()

                elif len(data) == 1:
                    item['title'] = data[0].split('LANGUAGES')[0] + "LANGUAGES"
                    authors = data[0].split('LANGUAGES')[1].lstrip()
                    print authors

                elif len(data) == 3:
                    if ',' in data[1]:
                        item['title'] = data[0].lstrip()
                        authors = data[1].lstrip() + ' ' + data[2].lstrip()
                    else:
                        item['title'] = data[0] + ' ' + data[1].lstrip()
                        authors = data[2].lstrip()

                elif len(data) > 3:
                    item['title'] = data[0] + ' ' + data[1].lstrip()
                    authors = data[2].lstrip() + ' ' + data[3].lstrip()
                else:
                    pass

                if "and" in authors:
                    authors = authors.split(', ')
                    item['authors'] = authors[0:-1]
                    item['authors'].append(authors[-1].split('and')[0].strip())
                    item['authors'].append(authors[-1].split('and')[1].lstrip())
                else:
                    item['authors'] = [authors]
                yield item
