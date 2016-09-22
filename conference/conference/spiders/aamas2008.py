__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class AAMAS2008Spider(scrapy.Spider):

    name = "aamas2008"
    allowed_domains = ["www.aamas2008.com"]
    start_urls = [
        "http://ifaamas.org/Proceedings/aamas08/proceedings/mainTrackPapers.htm"
    ]

    def parse(self, response):

        for record in response.xpath('//tr/td[a]'):

            item = ConferenceItem()
            print record
            item['year'] = "2008"
            title = record.xpath('a/text()').extract()
            print title
            item['title'] = title[0]

            authors = record.xpath('i/text()').extract()[0]
            print authors
            authors = authors.split(', ')
            item['authors'] = authors

            yield item