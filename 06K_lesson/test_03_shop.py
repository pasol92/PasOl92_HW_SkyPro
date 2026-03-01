import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.firefox
@pytest.mark.parametrize("first_name, last_name, zip_code, expected_total", [
    ("Екатерина", "Щеглова", "653035", "Total: $58.29")
])
def test_purchase_flow(first_name, last_name, zip_code, expected_total):
    driver = webdriver.Firefox()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://www.saucedemo.com/")

        # Авторизация
        wait.until(EC.element_to_be_clickable((
            By.ID, "user-name"))).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Добавление товаров в корзину
        wait.until(EC.element_to_be_clickable((
            By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        # Переход в корзину и оформление заказа
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        # Заполнение формы
        driver.find_element(By.ID, "first-name").send_keys(first_name)
        driver.find_element(By.ID, "last-name").send_keys(last_name)
        driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        driver.find_element(By.ID, "continue").click()

        # Проверка итоговой суммы
        total_label = wait.until(EC.presence_of_element_located((
            By.CLASS_NAME, "summary_total_label")))
        assert total_label.text == expected_total, f"Ожидаемая сумма {
            expected_total}, но получено {total_label.text}"

        # Завершение покупки
        driver.find_element(By.ID, "finish").click()
        wait.until(EC.element_to_be_clickable((
            By.ID, "back-to-products"))).click()

    finally:
        driver.quit()
