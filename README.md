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


ABOUT MEDIUM.PY 

# Python Scraper Project

This project contains various web scrapers built with Python. The latest addition is a **Medium Article Scraper**, which can bypass Cloudflare and extract articles from [Medium](https://medium.com).

---

## 🚀 **Medium Article Scraper**
### **Description**
This script **scrapes articles from Medium** using **Selenium** while bypassing **Cloudflare protections**. It simulates real user behavior, uses stored cookies for authentication, and scrolls down to load more articles.

### **🛠 Features**
- **Bypasses Cloudflare** using real **cookies**.
- **Extracts articles** from the Technology section.
- **Saves results in JSON format** (`medium_articles.json`).
- **Scrolls dynamically** to load more content.
- **Automatically updates cookies** to keep sessions valid.

---

## 📥 **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/JhonBob999/cnn-scrapper-example/tree/main/cnn_scraper/spiders.git
   cd cnn-scrapper-example/tree/main/cnn_scrapper/spiders

2. Install required dependencies:
   ```bash
    pip install -r requirements.txt

3. ⚙️ How to Use
    Running the Medium Scraper
    To run the Medium scraper, use:
    ```bash
    python cnn_scraper/spiders/medium.py

💡 Make sure cookies.json is available. If Cloudflare blocks the scraper, update cookies manually!
### 🔄 Updating Cookies
1. Open **F12 → Application → Storage → Cookies**.
2. Copy cookies for **medium.com** only.
3. Save them in `cookies.json`.

⚠ **IMPORTANT:** Place only cookies that belong to the target website you are parsing.



📊 Example Output (medium_articles.json)
    [
    {
        "title": "AI Is Making SaaS and Business Intelligence Obsolete",
        "url": "https://medium.com/entrepreneur-s-handbook/ai-is-making-saas-and-business-intelligence-obsolete-db38b6617484"
    },
    {
        "title": "Google just confirmed the AI reality many programmers are desperately trying to deny",
        "url": "https://medium.com/coding-beauty/ai-writes-google-codebase-00e6ad35ac7c"
    }
    ]

⚠️ Disclaimer
    This scraper is for educational purposes only. 
    Scraping websites without permission may violate terms of service. 
    Always ensure compliance with website policies.

📌 Contributing
    Pull requests are welcome! 
    If you find issues or have suggestions, open an issue on GitHub.