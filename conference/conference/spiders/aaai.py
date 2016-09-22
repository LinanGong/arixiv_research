__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class AAAI2015Spider(scrapy.Spider):

    name = "aaai"
    allowed_domains = ["www.aaai.org"]
    start_urls = [
        "http://www.aaai.org/Library/AAAI/aaai15contents.php",
        "http://www.aaai.org/Library/AAAI/aaai14contents.php",
        "http://www.aaai.org/Library/AAAI/aaai13contents.php",
        "http://www.aaai.org/Library/AAAI/aaai12contents.php",
        "http://www.aaai.org/Library/AAAI/aaai11contents.php",
        "http://www.aaai.org/Library/AAAI/aaai10contents.php",
        "http://www.aaai.org/Library/AAAI/aaai08contents.php",
        "http://www.aaai.org/Library/AAAI/aaai07contents.php",
        "http://www.aaai.org/Library/AAAI/aaai06contents.php"
    ]

    def parse(self, response):

        for record in response.xpath('//h4/following::p[@class=\'left\']'):

            item = ConferenceItem()
            print record
            year = response.xpath('//div[@class=\'content\']//p[position()=3]/text()').extract()[0]
            item['year'] = year.split(', ')[1]
            data = record.xpath('a/text()').extract()
            print data
            item['title'] = data[0].strip().lstrip()
            authors = record.xpath('i/text()').extract()[0]
            print authors
            authors = authors.split(', ')
            item['authors'] = authors[0:-1]
            item['authors'].append(authors[-1])

            yield item