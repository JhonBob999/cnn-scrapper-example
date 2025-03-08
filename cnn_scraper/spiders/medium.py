import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# === ФАЙЛ С КУКАМИ ===
COOKIES_FILE = "cookies.json"

# === 1. Настраиваем браузер ===
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Отключаем обнаружение Selenium
#chrome_options.add_argument("--user-data-dir=selenium_profile")  # Используем реальный профиль
chrome_options.add_argument("--start-maximized")  # Открываем на весь экран
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

# === 2. Запускаем Chrome ===
service = Service("chromedriver.exe")  # Укажи путь к chromedriver, если он не в той же папке
driver = webdriver.Chrome(service=service, options=chrome_options)

# === 3. Переход на Medium ===
driver.get("https://medium.com")

# === 4. Загружаем куки ===
def load_cookies(driver, file_path):
    with open(file_path, "r") as file:
        cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)

time.sleep(5)  # Ждём, чтобы страница загрузилась
print("🔹 Текущий URL:", driver.current_url)
load_cookies(driver, COOKIES_FILE)
driver.refresh()  # Обновляем страницу для применения куков

# === 5. Проверяем, зашли ли мы ===
time.sleep(5)

print("✅ Успешный вход в Medium!")

# === 6. Переходим в раздел 'Technology' ===
driver.get("https://medium.com/tag/technology")
time.sleep(5)

# === 7. Плавный скроллинг для загрузки статей ===
for _ in range(5):  # Прокручиваем страницу вниз 5 раз
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
    time.sleep(2)

# === 8. Парсим статьи ===
articles = driver.find_elements(By.XPATH, "//h2")  # Заголовки статей
parsed_data = []

for article in articles:
    title = article.text
    try:
        link = article.find_element(By.XPATH, "./ancestor::a").get_attribute("href")
    except:
        link = "No link found"
    parsed_data.append({"title": title, "url": link})

# === 9. Сохраняем результат ===
with open("medium_articles.json", "w", encoding="utf-8") as file:
    json.dump(parsed_data, file, indent=4, ensure_ascii=False)

print("✅ Данные сохранены в medium_articles.json")

# === 10. Закрываем браузер ===
driver.quit()
