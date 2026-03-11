import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ShopPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Добавить товар '{product_name}' в корзину")
    def add_product_to_cart(self, product_name: str) -> None:
        # SauceDemo использует id вида 'add-to-cart-sauce-labs-backpack'
        # Преобразуем название в формат id
        item_id = "add-to-cart-" + product_name.lower().replace(" ", "-")
        self.driver.find_element(By.ID, item_id).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Нажимает на иконку корзины."""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
