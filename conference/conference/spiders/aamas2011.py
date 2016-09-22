__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class AAMAS2011Spider(scrapy.Spider):

    name = "aamas2011"
    allowed_domains = ["www.aamas2011.com"]
    start_urls = [
        "http://www.aamas-conference.org/Proceedings/aamas2011/resources/fullpapers.html"
    ]

    def parse(self, response):

        for record in response.xpath('//div//p'):

            item = ConferenceItem()
            print record
            item['year'] = "2011"
            title = record.xpath('span[@class=\'title\']/a/text()').extract()[0].strip()
            print title
            item['title'] = title

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