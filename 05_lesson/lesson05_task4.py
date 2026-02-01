from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/login")
    username = driver.find_element(By.ID, "username")
    username.send_keys("tomsmith")
    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")
    login_button = driver.find_element(By.CLASS_NAME, "radius")
    login_button.click()
    flash_message = driver.find_element(By.ID, "flash")
    print("Сообщение:", flash_message.text)

finally:
    driver.quit()
