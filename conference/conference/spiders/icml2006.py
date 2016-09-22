__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class ICML2006Spider(scrapy.Spider):

    name = "icml2006"
    allowed_domains = ["www.machinelearning.org"]
    start_urls = [
        "http://www.machinelearning.org/icml2006_proc.html"
    ]

    def parse(self, response):

        for record in response.xpath('//table[@class=\'content\']/tbody//tr[position()>1]'):

            item = ConferenceItem()
            print record
            item['year'] = "2006"
            title = record.xpath('td[2]/p//em//text()').extract()
            print title
            if not title:
                title = [u'CN=CPCN']
            title = title[0].lstrip().strip().replace('\n', ' ')
            item['title'] = title

            authors = record.xpath('td[position()=3 and p]/p/sup/sub/text()').extract()
            print authors
            authors = authors[0].split(', ')
            authors[-1] = authors[-1].replace('\n', ' ')
            item['authors'] = authors

            yield item