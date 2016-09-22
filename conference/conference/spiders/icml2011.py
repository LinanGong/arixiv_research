__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class ICML2011Spider(scrapy.Spider):

    name = "icml2011"
    allowed_domains = ["www.icml.com"]
    start_urls = [
        "http://www.icml-2011.org/papers.php"
    ]

    def parse(self, response):

        for record in response.xpath('//a[h3]'):

            item = ConferenceItem()
            print record
            item['year'] = "2011"
            title = record.xpath('h3/text()').extract()
            print title
            item['title'] = title[0].strip()

            authors = record.xpath('span[@class=\'name\']/text()').extract()[0]
            print authors
            authors = authors.split(', ')
            item['authors'] = authors

            yield item