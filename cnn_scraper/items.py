import scrapy

class CnnScraperItem(scrapy.Item):
    title = scrapy.Field()        # Заголовок статьи
    date = scrapy.Field()         # Дата публикации
    author = scrapy.Field()       # Автор статьи
    content = scrapy.Field()      # Текст статьи (первые 300 символов)
    url = scrapy.Field()          # URL статьи
