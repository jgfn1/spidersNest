import scrapy

class InfoMoneySpider(scrapy.Spider):
    name = 'infoMoney'
    start_urls = ["https://www.infomoney.com.br/"]

    def parse(self, response):
        article_links = response.css('span.hl-title')
        article_links = article_links.xpath('.//a/@href')
        for link in article_links.extract():
            print('\n')
            yield {"links": link}