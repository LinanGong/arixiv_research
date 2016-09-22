__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class ICML2009Spider(scrapy.Spider):

    name = "icml2009"
    allowed_domains = ["www.icml.com"]
    start_urls = [
        "http://www.machinelearning.org/archive/icml2009/abstracts.html"
    ]

    def parse(self, response):

        for record in response.xpath('//div[@id=\'main\']//h3[a]'):

            item = ConferenceItem()
            print record
            item['year'] = "2009"
            title = record.xpath('text()').extract()
            print title
            item['title'] = title[0].strip()

            authors = record.xpath('following-sibling::p/i/text()').extract()[0]
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