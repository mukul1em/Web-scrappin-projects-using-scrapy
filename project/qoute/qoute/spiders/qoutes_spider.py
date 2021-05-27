import scrapy
from ..items import QouteItem

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/'
    ] 

    def parse(self, response):

        items = QouteItem()

        all_div_qoutes = response.css('div.quote')

        for quote in all_div_qoutes:
            title = quote.css('span.text::text').extract()    
            author = quote.css('.author::text').extract()
            tag = quote.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            yield items

    


         