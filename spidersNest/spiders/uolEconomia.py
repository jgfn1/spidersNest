import scrapy
from ..items import SpidersNestItem

class UolEconomia(scrapy.Spider):
    name = 'uolEconomia'
    start_urls = ["https://economia.uol.com.br/"]

    def parse(self, response):
        article_links = response.css('.thumbnail-standard-wrapper')
        article_links += response.css('.thumbnails-wrapper')
        article_links = article_links.xpath('.//a/@href')
        for link in article_links.extract():
                yield scrapy.Request(link, self.parse_article)

    def parse_article(self, response):
        title = response.css("i.custom-title ::text").extract()
        if(len(title) == 0):
            raise Exception("Article not in standard format, it is going to be ignored.")
        body = response.css("div.text p ::text").extract()
        author = response.css(".single .open-tooltip::text").extract()
        if(len(author) == 0):
            author = response.css("p.p-author ::text").extract()
        if(len(author) == 0):
            raise Exception("Article not in standard format, it is going to be ignored.")
        elif(author[0][0].isalpha()):
            if(len(author) == 2):
                date = author[1]
            elif(len(author) == 3):
                date = author[2]
            author = author[0]
        elif(author[0][0].isdigit()):
            date = author[0]
            author = ["Uol"]
        author = author.split('-')[0]
        tags = response.css("div.cs-entry__tags ::text").extract()
        
        items = SpidersNestItem()
        items["title"] = title
        items["body"] = body
        items["paragraph_count"] = len(body)
        items["word_count"] = len(''.join(body).split(' '))
        items["author"] = author
        items["date"] = date 
        items["tags"] = []
        items["url"] = response.url
        
        yield items