import scrapy
from cnn_scraper.items import CnnScraperItem

class CNNSpider(scrapy.Spider):
    name = "cnn"
    allowed_domains = ["cnn.com"]
    start_urls = ["https://edition.cnn.com/"]

    def parse(self, response):
        # Универсальный селектор для сбора ссылок на статьи CNN
        articles = response.css('a.container__link::attr(href)').getall()

        for article in articles:
            if article.startswith('/'):
                article_url = response.urljoin(article)
                yield scrapy.Request(article_url, callback=self.parse_article)

    def parse_article(self, response):
        item = CnnScraperItem()

        # Заголовок статьи
        item['title'] = response.css('h1.headline__text::text').get(default="N/A").strip()

        # Дата публикации (очищаем от лишних слов и пробелов)
        raw_date = response.css('div.timestamp::text').get(default="N/A").strip()
        item['date'] = raw_date.replace("Published\n", "").replace("Updated\n", "").strip()

        # Автор статьи (обработка пустых полей)
        item['author'] = response.css('span.byline__name::text').get(default="N/A").strip()

        # Контент статьи (первые 300 символов, если пусто - сообщение)
        paragraphs = response.css('div.article__content p::text').getall()
        content = ' '.join(paragraphs).replace('\n', ' ').replace('\r', '').replace(';', ',').replace('"', "'").strip()
        if content:
            item['content'] = (content[:297] + '...') if len(content) > 300 else content
        else:
            item['content'] = "No content available"

        # URL статьи
        item['url'] = response.url

        yield item


