import scrapy
from ..items import SpidersNestItem

class BoletimEconomico(scrapy.Spider):
    name = 'boletimEconomico'
    start_urls = ["https://boletimeconomico.com.br/"]

    def parse(self, response):
        article_links = response.css('.cs-entry__title ')
        article_links = article_links.xpath('.//a/@href')
        for link in article_links.extract():
            yield scrapy.Request(link, self.parse_article)

    def parse_article(self, response):
        title = response.css("h1.cs-entry__title span::text")[0].extract()
        body = response.css("div.entry-content p ::text").extract()
        author = response.css("div.cs-entry__author-meta ::text").extract()
        date = response.css("#primary .cs-meta-date ::text")[0].extract()
        tags = response.css("div.cs-entry__tags ::text").extract()
        
        items = SpidersNestItem()
        items["title"] = title
        items["body"] = body
        items["paragraph_count"] = len(body)
        items["word_count"] = len(''.join(body).split(' '))
        items["author"] = list(map(lambda item: item.replace('\t', '').replace('\n', ''), author))
        items["date"] = date 
        items["tags"] = tags 
        items["url"] = response.url
        
        yield items