import scrapy
from ..items import SpidersNestItem

class InfoMoneySpider(scrapy.Spider):
    name = 'infoMoney'
    start_urls = ["https://www.infomoney.com.br/"]

    def parse(self, response):
        article_links = response.css('span.hl-title')
        article_links = article_links.xpath('.//a/@href')
        for link in article_links.extract():
            yield scrapy.Request(link, self.parse_article)

    def parse_article(self, response):
        title = response.css(".page-title-1::text")[0].extract()
        body = response.css(".article-content").xpath("//p/text()").extract()
        author = response.css("span.author-name a::text").extract()
        date = response.css("time.entry-date::text").extract()
        tags = response.css("ul.article-terms a::text").extract()
        
        items = SpidersNestItem()
        items["title"] = title
        items["body"] = body[6:]
        items["paragraph_count"] = len(body)
        items["word_count"] = len(''.join(body).split(' '))
        items["author"] = list(map(lambda item: item.replace('\t', '').replace('\n', ''), author))
        items["date"] = date 
        items["tags"] = tags 
        items["url"] = response.url
        items["_id"] = response.url
        
        yield items