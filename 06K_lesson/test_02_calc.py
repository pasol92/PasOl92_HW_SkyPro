import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.chrome
def test_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 60)

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Ввод задержки
        delay_input = wait.until(EC.element_to_be_clickable((By.ID, "delay")))
        delay_input.clear()
        delay_input.send_keys("45")

        # Нажатие кнопок калькулятора
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        # Ожидание результата через 45 секунд
        result_element = wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        assert result_element, "Результат не равен 15"

    finally:
        driver.quit()
