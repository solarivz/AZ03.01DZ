import time

import ChromeDriverManager as ChromeDriverManager
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