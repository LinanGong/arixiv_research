__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class ICML2008Spider(scrapy.Spider):

    name = "icml2008"
    allowed_domains = ["www.icml.com"]
    start_urls = [
        "http://icml2008.cs.helsinki.fi/accepted_papers.shtml"
    ]

    def parse(self, response):

        for record in response.xpath('//div[@class=\'content\']//ul//li'):

            item = ConferenceItem()
            print record
            item['year'] = "2008"
            title = record.xpath('text()').extract()
            print title
            item['title'] = title[0].strip()

            authors = record.xpath('i/text()').extract()[0]
            print authors
            data = []
            if ' and ' in authors:
                authors = authors.split(' and ')

                for a in authors:
                    if ',' in a:
                        data.extend(a.split(', '))
                    else:
                        data.append(a)
            else:
                data.append(authors)

            item['authors'] = data

            yield item