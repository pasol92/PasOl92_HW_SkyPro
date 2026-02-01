from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    images = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "img")))
    third_image_src = images[2].get_attribute("src")
    print(third_image_src)

finally:
    driver.quit()
