# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request

from web_scraper.items import WebScraperItem
from scrapy_djangoitem import DjangoItem

class PakostnikSpider(scrapy.Spider):
    name = 'pakostnik'
    allowed_domains = ['pakostnik.com']
    start_urls = ['https://www.pakostnik.com/en/novi-produkti']

    def parse(self, response):
        products = response.css('.productBox')

        for product in products:
            item = WebScraperItem()
            item['name'] = product.css('.productName::text').extract()[0]
            item['web_url'] = product.css('.viewDetailsBtn').attrib['href']
            item['sku'] = 'None'
            item['price'] = product.css('.price-box .special-price .price::text').extract()[0]
            item['description'] = product.css('.productBoxIMG').attrib['title']
            # print(item)
            item.save()