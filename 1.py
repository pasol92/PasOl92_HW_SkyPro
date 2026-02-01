# 1.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

# Проверьте, существует ли chromedriver
chromedriver_path = '/usr/local/bin/chromedriver'  # Укажите свой путь
if not os.path.exists(chromedriver_path):
    print("Ошибка: chromedriver не найден по пути:", chromedriver_path)
else:
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com")
    print("Заголовок страницы:", driver.title)
    driver.quit()
    