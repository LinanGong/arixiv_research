__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem
import re

class FOCS2011Spider(scrapy.Spider):

    name = "focs2011"
    allowed_domains = ["www.cs.cmu.edu"]
    start_urls = [
        "https://sites.google.com/site/yixincaoresearch/papers/focs-2011"
    ]

    def parse(self, response):

        for record in response.xpath('//tbody//div[@dir=\'ltr\']'):

            item = ConferenceItem()
            data = record.xpath('.//text()').extract()
            print data

            for t in range(0, len(data)):
                if t % 2 == 1:
                    # print 'authors: ', data[t]
                    continue
                else:
                    print data[t]
                    item['year'] = '2011'
                    item['title'] = re.sub('\d+\. ', '', data[t]).strip()
                    authors = data[t+1].split(' and ')
                    print authors
                    item['authors'] = authors
                    yield item