__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class ICML2013Spider(scrapy.Spider):

    name = "icml2013"
    allowed_domains = ["www.icml.com"]
    start_urls = [
        "http://www.jmlr.org/proceedings/papers/v28/"
    ]

    def parse(self, response):

        for record in response.xpath('//div[@class=\'paper\']'):

            item = ConferenceItem()

            item['year'] = "2013"
            title = record.xpath('p[@class=\'title\']//text()').extract()
            print title
            # if record.xpath('p[@class=\'title\']//span'):
            #     title2 = record.xpath('p[@class=\'title\']//span//text()').extract()
            #     print title2
            item['title'] = ''.join(title)

            authors = record.xpath('p/span[@class=\'authors\']//text()').extract()
            authors = ''.join(authors)
            authors = authors.split(',')
            a = []
            for i in authors:
                a.append(i.lstrip().strip())
            item['authors'] = a

            yield item