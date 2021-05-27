# -*- coding: utf-8 -*-
import scrapy


class AmazonGrocerySpider(scrapy.Spider):
    name = 'amazon_grocery'
    allowed_domains = ['www.amazon.in/s?k=grocery']
    start_urls = ['http://www.amazon.in/s?k=grocery/']

    def parse(self, response):
        pass
