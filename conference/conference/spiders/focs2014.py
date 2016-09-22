__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem
import re

class FOCS2014Spider(scrapy.Spider):

    name = "focs2014"
    allowed_domains = ["www.cs.cmu.edu"]
    start_urls = [
        "https://sites.google.com/site/yixincaoresearch/papers/focs-2014"
    ]

    def parse(self, response):

        for record in response.xpath('//tbody//div[@dir=\'ltr\']'):

            item = ConferenceItem()
            data = record.xpath('.//text()').extract()

            for t in range(0, len(data)):
                if t % 2 == 1:
                    continue
                else:
                    print data[t]
                    item['year'] = '2014'
                    item['title'] = data[t]
                    authors = data[t+1].split(' , ')
                    print authors
                    au = []
                    for a in authors:
                        au.append(re.sub('\(.*\)', '', a).strip())
                    item['authors'] = au
                    yield item