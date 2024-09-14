import time
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import csv

# Устанавливаем драйвер для браузера Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открываем сайт с диванами
url = 'https://www.divan.ru/category/divany'
driver.get(url)

# Подождем несколько секунд, чтобы страница загрузилась
time.sleep(5)

# Парсинг цен с сайта
prices = []
price_elements = driver.find_elements(By.CSS_SELECTOR, 'span.price__value')

for element in price_elements:
    price_text = element.text.replace(' ', '').replace('₽', '').strip()
    if price_text.isdigit():
        prices.append(int(price_text))

# Закрываем браузер после сбора данных
driver.quit()

# Запись цен в CSV файл
with open('sofa_prices_selenium.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])
    for price in prices:
        writer.writerow([price])