# CNN Scraper Example 🚀

📌 **Простой и быстрый парсер новостей CNN, написанный на Python с использованием Scrapy.**

## ⚙️ Что делает парсер:

- Собирает свежие новости с сайта [CNN](https://edition.cnn.com/).
- Сохраняет собранные данные в удобные форматы: **JSON** и **CSV**.

## 📂 Какие данные собираются:

- ✅ **Заголовок статьи** (`title`)
- ✅ **Дата публикации** (`date`)
- ✅ **Автор статьи** (`author`)
- ✅ **Краткое содержание статьи** (`content`, первые 300 символов)
- ✅ **Ссылка на статью** (`url`)

## 🚀 Как использовать парсер:

### 1. Установи Scrapy

В терминале выполните:

```bash
pip install scrapy
```

### 2. Запуск парсера

Чтобы получить данные в формате JSON:

```bash
scrapy crawl cnn -o cnn_articles.json
```

Чтобы получить данные в формате CSV:

```bash
scrapy crawl cnn -o cnn_articles.csv
```

✅ **После выполнения команды появится файл с результатами.**

## 📌 Примеры собранных данных:

- [Пример JSON-файла](https://github.com/JhonBob999/cnn-scrapper-example/blob/main/cnn_articlesNEW.json)
- [Пример CSV-файла](https://github.com/JhonBob999/cnn-scrapper-example/blob/main/cnn_articles_colon.csv)

## 🔥 Используемые технологии:

- Python
- Scrapy
- JSON / CSV

## 🤝 Как заказать подобный парсер:

Свяжитесь со мной на [Fiverr](https://www.fiverr.com/s/P2XE99g), чтобы обсудить детали и заказать разработку индивидуального парсера для ваших задач!



English Explanation

# CNN Scraper Example 🚀

📌 **Simple and fast CNN news scraper built with Python using Scrapy.**

## ⚙️ What the scraper does:

- Collects the latest news from [CNN](https://edition.cnn.com/).
- Saves the collected data in convenient formats: **JSON** and **CSV**.

## 📂 Collected data includes:

- ✅ **Article Title** (`title`)
- ✅ **Publication Date** (`date`)
- ✅ **Author** (`author`)
- ✅ **Short summary of the article** (`content`, first 300 characters)
- ✅ **Article URL** (`url`)

## 🚀 How to use the scraper:

### 1. Install Scrapy

Run in terminal:

```bash
pip install scrapy
```

### 2. Run the scraper

To get data in JSON format:

```bash
scrapy crawl cnn -o cnn_articles.json
```

To get data in CSV format:

```bash
scrapy crawl cnn -o cnn_articles.csv
```

✅ **After running the command, a file with the scraped data will be generated.**

## 📌 Examples of collected data:

- [JSON file example](https://github.com/JhonBob999/cnn-scrapper-example/blob/main/cnn_articlesNEW.json)
- [CSV file example](https://github.com/JhonBob999/cnn-scrapper-example/blob/main/cnn_articles_colon.csv)

## 🔥 Technologies used:

- Python
- Scrapy
- JSON / CSV

## 🤝 How to order a similar scraper:

Contact me on [Fiverr](https://www.fiverr.com/s/P2XE99g) to discuss details and order a custom scraper tailored for your needs!