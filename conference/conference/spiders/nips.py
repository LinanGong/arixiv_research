__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem

class NIPSSpider(scrapy.Spider):

    name = "nips"
    allowed_domains = ["papers.nips.cc"]
    start_urls = [
        "https://papers.nips.cc/book/advances-in-neural-information-processing-systems-28-2015",
        "https://papers.nips.cc/book/advances-in-neural-information-processing-systems-27-2014",
        "https://papers.nips.cc/book/advances-in-neural-information-processing-systems-26-2013",
        "https://papers.nips.cc/book/advances-in-neural-information-processing-systems-25-2012",
        "https://papers.nips.cc/book/advances-in-neural-information-processing-systems-24-2011",
        "https://papers.nips.cc/book/advances-in-neural-information-processing-systems-23-2010",
        "https://papers.nips.cc/book/advances-in-neural-information-processing-systems-22-2009",
        "https://papers.nips.cc/book/advances-in-neural-information-processing-systems-21-2008",
        "https://papers.nips.cc/book/advances-in-neural-information-processing-systems-20-2007",
        "https://papers.nips.cc/book/advances-in-neural-information-processing-systems-19-2006"
    ]

    def parse(self, response):
        data = response.xpath('/html/head/title/text()').extract()
        year = data[0].split(' ')[1]
        print year

        for record in response.xpath('//body/div[2]//ul/li'):

            item = ConferenceItem()
            item['year'] = year
            item['title'] = record.xpath('a[1]/text()').extract()
            item['authors'] = record.xpath('a[position()>1]/text()').extract()
            yield item
