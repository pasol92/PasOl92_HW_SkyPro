# 06K_lesson/test_01_form.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_validation(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    wait = WebDriverWait(driver, 10)
    zip_code_field = wait.until(EC.presence_of_element_located((By.NAME, "zip-code")))
    other_fields = driver.find_elements(By.CSS_SELECTOR, ".form-control:not([name='zip-code'])")
    assert "is-invalid" in zip_code_field.get_attribute("class")
    for field in other_fields:
        assert "is-valid" in field.get_attribute("class")
