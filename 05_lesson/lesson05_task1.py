from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/classattr")
    button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()

finally:
    driver.quit()
