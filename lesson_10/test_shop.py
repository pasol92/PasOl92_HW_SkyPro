import allure
from login_page import LoginPage
from shop_page import ShopPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.feature("Магазин SauceDemo")
@allure.title("Сквозной сценарий покупки")
@allure.description(
    "Авторизация, добавление товаров и проверка финальной суммы.")
@allure.severity(allure.severity_level.CRITICAL)
def test_shopping_cart(firefox_driver):
    with allure.step("Авторизация"):
        login_page = LoginPage(firefox_driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Выбор товаров"):
        shop_page = ShopPage(firefox_driver)
        products = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]
        for product in products:
            shop_page.add_product_to_cart(product)
        shop_page.go_to_cart()

    with allure.step("Оформление заказа"):
        cart_page = CartPage(firefox_driver)
        cart_page.checkout()
        checkout_page = CheckoutPage(firefox_driver)
        checkout_page.fill_form("Олег", "Пащенко", "124482")

    with allure.step("Валидация суммы"):
        total = checkout_page.get_total()
        assert total == "Total: $58.29"
