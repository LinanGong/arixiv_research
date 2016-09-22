__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class AAMAS2011Spider(scrapy.Spider):

    name = "aamas2010"
    allowed_domains = ["www.aamas-conference.org"]
    start_urls = [
        "http://www.aamas-conference.org/Proceedings/aamas2010/resources/_fullpapers.html"
    ]

    def parse(self, response):

        for record in response.xpath('//div//p'):

            item = ConferenceItem()
            print record
            item['year'] = "2010"
            title = record.xpath('span[@class=\'title\']/a/text()').extract()
            print title
            if title:
                item['title'] = title[0].strip()
            else:
                item['title'] = "Coordination for Uncertain Outcomes using Distributed Neighbor Exchange"

            print record.xpath('span[@class=\'authors\']//text()').extract()
            authors = []
            for a in record.xpath('span[@class=\'authors\']//text()').extract():
                if 'papers' not in a:
                    data = a.split(',')
                    for i in data:
                        if i.lstrip().rstrip():
                            authors.append(i.lstrip().strip())
            item['authors'] = authors

            yield item