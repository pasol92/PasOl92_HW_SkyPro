from login_page import LoginPage
from shop_page import ShopPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_shopping_cart(firefox_driver):
    login_page = LoginPage(firefox_driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    shop_page = ShopPage(firefox_driver)
    products = ["Sauce Labs Backpack", 
                "Sauce Labs Bolt T-Shirt", 
                "Sauce Labs Onesie"]
    for product in products:
        shop_page.add_product_to_cart(product)

    shop_page.go_to_cart()
    cart_page = CartPage(firefox_driver)
    cart_page.checkout()

    checkout_page = CheckoutPage(firefox_driver)
    checkout_page.fill_form("Иван", "Иванов", "123456")
    total = checkout_page.get_total()
    assert total == "Total: $58.29"
    