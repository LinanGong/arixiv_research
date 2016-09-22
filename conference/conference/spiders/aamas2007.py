__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class AAMAS2007Spider(scrapy.Spider):

    name = "aamas2007"
    allowed_domains = ["www.aamas2007.com"]
    start_urls = [
        "http://www.aamas-conference.org/AAMAS/aamas07/acceptedpapers.html"
    ]

    def parse(self, response):

        for record in response.xpath('//span[@class=\'bodyblack\']'):

            data = record.xpath('text()').extract()
            print data
            for line in data:
                if line.strip():
                    paper = line.lstrip().strip().split(', ')
                    item = ConferenceItem()
                    title = paper[0].replace('* \"', '')
                    title = title.replace('\"', '')

                    item['title'] = title
                    authors = paper[1: -1]
                    authors.append(paper[-1])

                    item['authors'] = authors
                    item['year'] = "2007"

                    yield item