import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Перейти к оформлению заказа (Checkout)")
    def checkout(self) -> None:
        """Нажимает кнопку Checkout в корзине."""
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()
