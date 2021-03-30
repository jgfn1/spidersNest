import scrapy

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
        yield {
            "title": title,
            "body": body[6:],
            "author": list(map(lambda item: item.replace('\t', '').replace('\n', ''), author)),
            "date": date,
            "tags": tags,
            "url": response.url,
        }